""" Repository of build functions specific to the ODATA V4"""

# pylint: disable=unused-argument, missing-docstring,invalid-name
# All methods by design of 'build_element' accept config, but no all have to use it

import itertools
import copy

import pyodata.config as conf
import pyodata.exceptions as exceptions
import pyodata.policies as policies

import pyodata.model.elements as elements
import pyodata.v4.elements as v4_elements


# pylint: disable=protected-access,too-many-locals,too-many-branches,too-many-statements
# While building schema it is necessary to set few attributes which in the rest of the application should remain
# constant. As for now, splitting build_schema into sub-functions would not add any benefits.
def build_schema(config: conf.Config, schema_nodes):
    schema = elements.Schema(config)

    # Parse Schema nodes by parts to get over the problem of not-yet known
    # entity types referenced by entity sets, function imports and
    # annotations.

    # TODO: First, process EnumType, EntityType and ComplexType nodes.
    #  They have almost no dependencies on other elements.
    for schema_node in schema_nodes:
        namespace = schema_node.get('Namespace')
        decl = elements.Schema.Declaration(namespace)
        schema._decls[namespace] = decl

        for type_def in schema_node.xpath('edm:TypeDefinition', namespaces=config.namespaces):
            decl.add_type_definition(elements.build_element(elements.Typ, config, node=type_def))

        for enum_type in schema_node.xpath('edm:EnumType', namespaces=config.namespaces):
            decl.add_enum_type(elements.build_element(elements.EnumType, config, type_node=enum_type,
                                                      namespace=namespace))

        for complex_type in schema_node.xpath('edm:ComplexType', namespaces=config.namespaces):
            decl.add_complex_type(elements.build_element(elements.ComplexType, config, type_node=complex_type,
                                                         schema=schema))

        for entity_type in schema_node.xpath('edm:EntityType', namespaces=config.namespaces):
            decl.add_entity_type(elements.build_element(elements.EntityType, config, type_node=entity_type,
                                                        schema=schema))

    # resolve types of properties
    for stype in itertools.chain(schema.entity_types, schema.complex_types):
        if isinstance(stype, elements.NullType) or stype.is_collection:
            continue

        prop: elements.StructTypeProperty
        for prop in stype.proprties():
            try:
                prop.typ = schema.get_type(prop.type_info)
            except (exceptions.PyODataModelError, AttributeError) as ex:
                config.err_policy(policies.ParserError.PROPERTY).resolve(ex)
                prop.typ = elements.NullType(prop.type_info.name)

        if not isinstance(stype, elements.EntityType):
            continue

        for nav_prop in stype.nav_proprties:
            try:
                nav_prop.typ = schema.get_type(nav_prop.type_info)
            except (exceptions.PyODataModelError, AttributeError) as ex:
                config.err_policy(policies.ParserError.NAVIGATION_PROPERTY).resolve(ex)
                nav_prop.typ = elements.NullType(nav_prop.type_info.name)

    # resolve partners and referential constraints of navigation properties after typ of navigation properties
    # are resolved
    for stype in schema.entity_types:
        if isinstance(stype, elements.NullType) or stype.is_collection:
            continue

        for nav_prop in stype.nav_proprties:
            partner = None
            if nav_prop.partner_info is not None:
                # Navigation properties of nav_prop.typ
                if nav_prop.typ.is_collection:
                    nav_prop_typ_nav_properties = nav_prop.typ.item_type.nav_proprties
                else:
                    nav_prop_typ_nav_properties = nav_prop.typ.nav_proprties
                partner = next(filter(lambda x: x.name == nav_prop.partner_info.name, nav_prop_typ_nav_properties))

            try:
                for ref_con in nav_prop.referential_constraints:
                    ref_con.proprty = stype.proprty(ref_con.proprty_name)
                    ref_con.referenced_proprty = nav_prop.typ.proprty(ref_con.referenced_proprty_name)

                nav_prop.partner = partner
            except (exceptions.PyODataModelError, AttributeError) as ex:
                config.err_policy(policies.ParserError.NAVIGATION_PROPERTY).resolve(ex)
                nav_prop.partner = v4_elements.NullProperty(nav_prop.partner_info.name)

    # Process entity sets
    for schema_node in schema_nodes:
        namespace = schema_node.get('Namespace')
        decl = schema._decls[namespace]

        for entity_set in schema_node.xpath('edm:EntityContainer/edm:EntitySet', namespaces=config.namespaces):
            try:
                eset = elements.build_element(v4_elements.EntitySet, config, entity_set_node=entity_set)
                eset.entity_type = schema.entity_type(eset.entity_type_info[1], namespace=eset.entity_type_info[0])
                decl.entity_sets[eset.name] = eset
            except (exceptions.PyODataParserError, KeyError) as ex:
                config.err_policy(policies.ParserError.ENTITY_SET).resolve(ex)

    # After all entity sets are parsed resolve the individual bindings among them and entity types
    for entity_set in schema.entity_sets:
        for nav_prop_bin in entity_set.navigation_property_bindings:
            path_info = nav_prop_bin.path_info
            try:
                nav_prop_bin.path = schema.entity_type(path_info.type,
                                                       namespace=path_info.namespace).nav_proprty(path_info.proprty)
                nav_prop_bin.target = schema.entity_set(nav_prop_bin.target_info)
            except (exceptions.PyODataModelError, KeyError) as ex:
                config.err_policy(policies.ParserError.NAVIGATION_PROPERTY_BIDING).resolve(ex)
                nav_prop_bin.path = elements.NullType(path_info.type)
                nav_prop_bin.target = elements.NullType(nav_prop_bin.target_info)

    # TODO: Finally, process Annotation nodes when all Scheme nodes are completely processed.
    return schema


def build_navigation_type_property(config: conf.Config, node):
    partner = elements.Types.parse_type_name(node.get('Partner')) if node.get('Partner') else None
    ref_cons = []

    for ref_con in node.xpath('edm:ReferentialConstraint', namespaces=config.namespaces):
        ref_cons.append(v4_elements.ReferentialConstraint(ref_con.get('Property'), ref_con.get('ReferencedProperty')))

    return v4_elements.NavigationTypeProperty(
        node.get('Name'),
        elements.Types.parse_type_name(node.get('Type')),
        node.get('nullable'),
        partner,
        node.get('contains_target'),
        ref_cons)


def build_navigation_property_binding(config: conf.Config, node, et_info):
    return v4_elements.NavigationPropertyBinding(v4_elements.to_path_info(node.get('Path'), et_info),
                                                 node.get('Target'))


def build_unit_annotation(config: conf.Config, target: elements.Typ, annotation_node):
    target.annotation = v4_elements.Unit(f'self.{target.name}', annotation_node.get('String'))


def build_type_definition(config: conf.Config, node):
    typ = copy.deepcopy(elements.Types.from_name(node.get('UnderlyingType'), config))
    typ.name = node.get('Name')

    annotation_nodes = node.xpath('edm:Annotation', namespaces=config.namespaces)
    if annotation_nodes:
        annotation_node = annotation_nodes[0]
        elements.build_annotation(annotation_node.get('Term'), config, target=typ, annotation_node=annotation_node)

    return typ
