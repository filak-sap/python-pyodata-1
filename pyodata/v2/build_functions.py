""" Repository of build functions specific to the ODATA V2"""

# pylint: disable=unused-argument, missing-docstring
# All methods by design of 'build_element' accept config, but no all have to use it

import itertools
import logging
from typing import List

import pyodata.config as conf
import pyodata.exceptions as exceptions
import pyodata.policies as policies

import pyodata.model.elements as elements
import pyodata.v2.elements as v2_elements


def modlog():
    """ Logging function for debugging."""
    return logging.getLogger("v2_build_functions")


# pylint: disable=protected-access,too-many-locals, too-many-branches,too-many-statements
# While building schema it is necessary to set few attributes which in the rest of the application should remain
# constant. As for now, splitting build_schema into sub-functions would not add any benefits.
def build_schema(config: conf.Config, schema_nodes):
    schema = v2_elements.Schema(config)

    # Parse Schema nodes by parts to get over the problem of not-yet known
    # entity types referenced by entity sets, function imports and
    # annotations.

    # First, process EnumType, EntityType and ComplexType nodes. They have almost no dependencies on other elements.
    for schema_node in schema_nodes:
        namespace = schema_node.get('Namespace')
        decl = v2_elements.Schema.Declaration(namespace)
        schema._decls[namespace] = decl

        for complex_type in schema_node.xpath('edm:ComplexType', namespaces=config.namespaces):
            decl.add_complex_type(elements.build_element(elements.ComplexType, config, type_node=complex_type,
                                                         schema=schema))

        for entity_type in schema_node.xpath('edm:EntityType', namespaces=config.namespaces):
            decl.add_entity_type(elements.build_element(elements.EntityType, config, type_node=entity_type,
                                                        schema=schema))

    # resolve types of properties
    for stype in itertools.chain(schema.entity_types, schema.complex_types):
        if isinstance(stype, elements.NullType):
            continue

        if stype.kind == elements.Typ.Kinds.Complex:
            # skip collections (no need to assign any types since type of collection
            # items is resolved separately
            if stype.is_collection:
                continue

            for prop in stype.proprties():
                try:
                    prop.typ = schema.get_type(prop.type_info)
                except exceptions.PyODataModelError as ex:
                    config.err_policy(policies.ParserError.PROPERTY).resolve(ex)
                    prop.typ = elements.NullType(prop.type_info.name)

    # pylint: disable=too-many-nested-blocks
    # Then, process Associations nodes because they refer EntityTypes and
    # they are referenced by AssociationSets.
    for schema_node in schema_nodes:
        namespace = schema_node.get('Namespace')
        decl = schema._decls[namespace]

        for association in schema_node.xpath('edm:Association', namespaces=config.namespaces):
            assoc = elements.build_element(v2_elements.Association, config, association_node=association)
            try:
                for end_role in assoc.end_roles:
                    try:
                        # search and assign entity type (it must exist)
                        if end_role.entity_type_info.namespace is None:
                            end_role.entity_type_info.namespace = namespace

                        etype = schema.entity_type(end_role.entity_type_info.name, end_role.entity_type_info.namespace)

                        end_role.entity_type = etype
                    except KeyError:
                        raise exceptions.PyODataModelError(
                            f'EntityType {end_role.entity_type_info.name} does not exist in Schema '
                            f'Namespace {end_role.entity_type_info.namespace}')

                if assoc.referential_constraint is not None:
                    role_names = [end_role.role for end_role in assoc.end_roles]
                    principal_role = assoc.referential_constraint.principal

                    # Check if the role was defined in the current association
                    if principal_role.name not in role_names:
                        raise RuntimeError(
                            'Role {} was not defined in association {}'.format(principal_role.name, assoc.name))

                    # Check if principal role properties exist
                    role_name = principal_role.name
                    entity_type_name = assoc.end_by_role(role_name).entity_type_name
                    schema.check_role_property_names(principal_role, entity_type_name, namespace)

                    dependent_role = assoc.referential_constraint.dependent

                    # Check if the role was defined in the current association
                    if dependent_role.name not in role_names:
                        raise RuntimeError(
                            'Role {} was not defined in association {}'.format(dependent_role.name, assoc.name))

                    # Check if dependent role properties exist
                    role_name = dependent_role.name
                    entity_type_name = assoc.end_by_role(role_name).entity_type_name
                    schema.check_role_property_names(dependent_role, entity_type_name, namespace)
            except (exceptions.PyODataModelError, RuntimeError) as ex:
                config.err_policy(policies.ParserError.ASSOCIATION).resolve(ex)
                decl.associations[assoc.name] = v2_elements.NullAssociation(assoc.name)
            else:
                decl.associations[assoc.name] = assoc

    # resolve navigation properties
    for stype in schema.entity_types:
        # skip null type
        if isinstance(stype, elements.NullType):
            continue

        # skip collections
        if stype.is_collection:
            continue

        for nav_prop in stype.nav_proprties:
            try:
                assoc = schema.association(nav_prop.association_info.name, nav_prop.association_info.namespace)
                nav_prop.association = assoc
            except KeyError as ex:
                config.err_policy(policies.ParserError.ASSOCIATION).resolve(ex)
                nav_prop.association = v2_elements.NullAssociation(nav_prop.association_info.name)

    # Then, process EntitySet, FunctionImport and AssociationSet nodes.
    for schema_node in schema_nodes:
        namespace = schema_node.get('Namespace')
        decl = schema._decls[namespace]

        for entity_set in schema_node.xpath('edm:EntityContainer/edm:EntitySet', namespaces=config.namespaces):
            eset = elements.build_element(elements.EntitySet, config, entity_set_node=entity_set)
            eset.entity_type = schema.entity_type(eset.entity_type_info[1], namespace=eset.entity_type_info[0])
            decl.entity_sets[eset.name] = eset

        for function_import in schema_node.xpath('edm:EntityContainer/edm:FunctionImport',
                                                 namespaces=config.namespaces):
            efn = elements.build_element(elements.FunctionImport, config, function_import_node=function_import)

            # complete type information for return type and parameters
            if efn.return_type_info is not None:
                efn.return_type = schema.get_type(efn.return_type_info)
            for param in efn.parameters:
                param.typ = schema.get_type(param.type_info)
            decl.function_imports[efn.name] = efn

        for association_set in schema_node.xpath('edm:EntityContainer/edm:AssociationSet',
                                                 namespaces=config.namespaces):
            assoc_set = elements.build_element(v2_elements.AssociationSet, config, association_set_node=association_set)
            try:
                try:
                    assoc_set.association_type = schema.association(assoc_set.association_type_name,
                                                                    assoc_set.association_type_namespace)
                except KeyError:
                    raise exceptions.PyODataModelError(
                        f'Association {assoc_set.association_type_name} does not exist in namespace '
                        f'{assoc_set.association_type_namespace}')

                for end in assoc_set.end_roles:
                    # Check if an entity set exists in the current scheme
                    # and add a reference to the corresponding entity set
                    try:
                        entity_set = schema.entity_set(end.entity_set_name, namespace)
                        end.entity_set = entity_set
                    except KeyError:
                        raise exceptions.PyODataModelError('EntitySet {} does not exist in Schema Namespace {}'
                                                           .format(end.entity_set_name, namespace))
                    # Check if role is defined in Association
                    if assoc_set.association_type.end_by_role(end.role) is None:
                        raise exceptions.PyODataModelError('Role {} is not defined in association {}'
                                                           .format(end.role, assoc_set.association_type_name))
            except (exceptions.PyODataModelError, KeyError) as ex:
                config.err_policy(policies.ParserError.ASSOCIATION).resolve(ex)
                decl.association_sets[assoc_set.name] = v2_elements.NullAssociation(assoc_set.name)
            else:
                decl.association_sets[assoc_set.name] = assoc_set

    # Finally, process Annotation nodes when all Scheme nodes are completely processed.
    for schema_node in schema_nodes:
        for annotation_group in schema_node.xpath('edm:Annotations', namespaces=config.annotation_namespace):
            target = annotation_group.get('Target')
            if annotation_group.get('Qualifier'):
                modlog().warning('Ignoring qualified Annotations of %s', target)
                continue

            for annotation_node in annotation_group.xpath('edm:Annotation', namespaces=config.annotation_namespace):

                try:
                    elements.build_annotation(annotation_node.get('Term'), config, target=target,
                                              annotation_node=annotation_node, schema=schema)
                except exceptions.PyODataParserError as ex:
                    config.err_policy(policies.ParserError.ANNOTATION).resolve(ex)
    return schema


def build_navigation_type_property(config: conf.Config, node):
    return v2_elements.NavigationTypeProperty(
        node.get('Name'), node.get('FromRole'), node.get('ToRole'), elements.Identifier.parse(node.get('Relationship')))


def build_end_role(config: conf.Config, end_role_node):
    entity_type_info = elements.Types.parse_type_name(end_role_node.get('Type'))
    multiplicity = end_role_node.get('Multiplicity')
    role = end_role_node.get('Role')

    return v2_elements.EndRole(entity_type_info, multiplicity, role)


# pylint: disable=protected-access
def build_association(config: conf.Config, association_node):
    name = association_node.get('Name')
    association = v2_elements.Association(name)

    for end in association_node.xpath('edm:End', namespaces=config.namespaces):
        end_role = elements.build_element(v2_elements.EndRole, config, end_role_node=end)
        if end_role.entity_type_info is None:
            raise RuntimeError('End type is not specified in the association {}'.format(name))
        association._end_roles.append(end_role)

    if len(association._end_roles) != 2:
        raise RuntimeError('Association {} does not have two end roles'.format(name))

    refer = association_node.xpath('edm:ReferentialConstraint', namespaces=config.namespaces)
    if len(refer) > 1:
        raise RuntimeError('In association {} is defined more than one referential constraint'.format(name))

    if not refer:
        referential_constraint = None
    else:
        referential_constraint = elements.build_element(v2_elements.ReferentialConstraint, config,
                                                        referential_constraint_node=refer[0])

    association._referential_constraint = referential_constraint

    return association


def build_association_set_end_role(config: conf.Config, end_node):
    role = end_node.get('Role')
    entity_set = end_node.get('EntitySet')

    return v2_elements.AssociationSetEndRole(role, entity_set)


def build_association_set(config: conf.Config, association_set_node):
    end_roles: List[v2_elements.AssociationSetEndRole] = []
    name = association_set_node.get('Name')
    association = elements.Identifier.parse(association_set_node.get('Association'))

    end_roles_list = association_set_node.xpath('edm:End', namespaces=config.namespaces)
    if len(end_roles) > 2:
        raise exceptions.PyODataModelError('Association {} cannot have more than 2 end roles'.format(name))

    for end_role in end_roles_list:
        end_roles.append(elements.build_element(v2_elements.AssociationSetEndRole, config, end_node=end_role))

    return v2_elements.AssociationSet(name, association.name, association.namespace, end_roles)


def build_referential_constraint(config: conf.Config, referential_constraint_node):
    principal = referential_constraint_node.xpath('edm:Principal', namespaces=config.namespaces)
    if len(principal) != 1:
        raise RuntimeError('Referential constraint must contain exactly one principal element')

    principal_name = principal[0].get('Role')
    if principal_name is None:
        raise RuntimeError('Principal role name was not specified')

    principal_refs = []
    for property_ref in principal[0].xpath('edm:PropertyRef', namespaces=config.namespaces):
        principal_refs.append(property_ref.get('Name'))
    if not principal_refs:
        raise RuntimeError('In role {} should be at least one principal property defined'.format(principal_name))

    dependent = referential_constraint_node.xpath('edm:Dependent', namespaces=config.namespaces)
    if len(dependent) != 1:
        raise RuntimeError('Referential constraint must contain exactly one dependent element')

    dependent_name = dependent[0].get('Role')
    if dependent_name is None:
        raise RuntimeError('Dependent role name was not specified')

    dependent_refs = []
    for property_ref in dependent[0].xpath('edm:PropertyRef', namespaces=config.namespaces):
        dependent_refs.append(property_ref.get('Name'))
    if len(principal_refs) != len(dependent_refs):
        raise RuntimeError('Number of properties should be equal for the principal {} and the dependent {}'
                           .format(principal_name, dependent_name))

    return v2_elements.ReferentialConstraint(
        v2_elements.PrincipalRole(principal_name, principal_refs), v2_elements.DependentRole(dependent_name,
                                                                                             dependent_refs))
