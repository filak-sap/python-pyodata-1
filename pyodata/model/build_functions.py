""" Reusable implementation of build functions for the most of edm elements """

# pylint: disable=unused-argument, missing-docstring, invalid-name
import copy
import logging

import pyodata.config as pyodata
import pyodata.policies as policies
import pyodata.exceptions as exceptions
import pyodata.model.elements as elements

# pylint: disable=cyclic-import
# When using `import xxx as yyy` it is not a problem and we need this dependency
import pyodata.v4 as v4


def modlog():
    return logging.getLogger("callbacks")


def build_struct_type_property(config: pyodata.Config, entity_type_property_node):
    return elements.StructTypeProperty(
        entity_type_property_node.get('Name'),
        elements.Types.parse_type_name(entity_type_property_node.get('Type')),
        entity_type_property_node.get('Nullable'),
        entity_type_property_node.get('MaxLength'),
        entity_type_property_node.get('Precision'),
        entity_type_property_node.get('Scale'),
        # TODO: create a class SAP attributes
        elements.sap_attribute_get_bool(entity_type_property_node, 'unicode', True),
        elements.sap_attribute_get_string(entity_type_property_node, 'label'),
        elements.sap_attribute_get_bool(entity_type_property_node, 'creatable', True),
        elements.sap_attribute_get_bool(entity_type_property_node, 'updatable', True),
        elements.sap_attribute_get_bool(entity_type_property_node, 'sortable', True),
        elements.sap_attribute_get_bool(entity_type_property_node, 'filterable', True),
        elements.sap_attribute_get_string(entity_type_property_node, 'filter-restriction'),
        elements.sap_attribute_get_bool(entity_type_property_node, 'required-in-filter', False),
        elements.sap_attribute_get_string(entity_type_property_node, 'text'),
        elements.sap_attribute_get_bool(entity_type_property_node, 'visible', True),
        elements.sap_attribute_get_string(entity_type_property_node, 'display-format'),
        elements.sap_attribute_get_string(entity_type_property_node, 'value-list'), )


# pylint: disable=protected-access
def build_struct_type(config: pyodata.Config, type_node, typ, schema=None):
    name = type_node.get('Name')
    base_type = type_node.get('BaseType')

    if base_type is None:
        label = elements.sap_attribute_get_string(type_node, 'label')
        is_value_list = elements.sap_attribute_get_bool(type_node, 'value-list', False)
        stype = typ(name, label, is_value_list)
    else:
        base_type = elements.Types.parse_type_name(base_type)

        try:
            stype = copy.deepcopy(schema.get_type(base_type))
        except KeyError:
            raise exceptions.PyODataParserError(f'BaseType \'{base_type.name}\' not found in schema')
        except AttributeError:
            raise exceptions.PyODataParserError(f'\'{base_type.name}\' ')

        stype._name = name

    for proprty in type_node.xpath('edm:Property', namespaces=config.namespaces):
        stp = elements.build_element(elements.StructTypeProperty, config, entity_type_property_node=proprty)

        if stp.name in stype._properties:
            raise KeyError('{0} already has property {1}'.format(stype, stp.name))

        stype._properties[stp.name] = stp

    # We have to update the property when
    # all properites are loaded because
    # there might be links between them.
    for ctp in list(stype._properties.values()):
        if ctp.struct_type is None:  # TODO: Is it correct
            ctp.struct_type = stype

    return stype


def build_complex_type(config: pyodata.Config, type_node, schema=None):
    try:
        return elements.build_element(elements.StructType, config, type_node=type_node, typ=elements.ComplexType,
                                      schema=schema)
    except (exceptions.PyODataException, KeyError, AttributeError) as ex:
        config.err_policy(policies.ParserError.COMPLEX_TYPE).resolve(ex)
        return elements.NullType(type_node.get('Name'))


# pylint: disable=protected-access
def build_entity_type(config: pyodata.Config, type_node, schema=None):
    try:
        etype = elements.build_element(elements.StructType, config, type_node=type_node, typ=elements.EntityType,
                                       schema=schema)

        for proprty in type_node.xpath('edm:Key/edm:PropertyRef', namespaces=config.namespaces):
            etype._key.append(etype.proprty(proprty.get('Name')))

        for proprty in type_node.xpath('edm:NavigationProperty', namespaces=config.namespaces):
            navp = elements.build_element('NavigationTypeProperty', config, node=proprty)

            if navp.name in etype._nav_properties:
                raise KeyError('{0} already has navigation property {1}'.format(etype, navp.name))

            etype._nav_properties[navp.name] = navp

        return etype
    except (KeyError, AttributeError) as ex:
        config.err_policy(policies.ParserError.ENTITY_TYPE).resolve(ex)
        return elements.NullType(type_node.get('Name'))


# pylint: disable=protected-access, too-many-locals
def build_enum_type(config: pyodata.Config, type_node, namespace):
    try:
        ename = type_node.get('Name')
        is_flags = type_node.get('IsFlags')

        # namespace = kwargs['namespace']

        underlying_type = type_node.get('UnderlyingType')

        # https://docs.oasis-open.org/odata/odata-csdl-json/v4.01/csprd04/odata-csdl-json-v4.01-csprd04.html#sec_EnumerationType
        if underlying_type is None:
            underlying_type = 'Edm.Int32'

        valid_types = {
            'Edm.Byte': [0, 2 ** 8 - 1],
            'Edm.Int16': [-2 ** 15, 2 ** 15 - 1],
            'Edm.Int32': [-2 ** 31, 2 ** 31 - 1],
            'Edm.Int64': [-2 ** 63, 2 ** 63 - 1],
            'Edm.SByte': [-2 ** 7, 2 ** 7 - 1]
        }

        if underlying_type not in valid_types:
            raise exceptions.PyODataParserError(
                f'Type {underlying_type} is not valid as underlying type for EnumType - must be one of {valid_types}')

        mtype = elements.Types.from_name(underlying_type, config)
        etype = elements.EnumType(ename, is_flags, mtype, namespace)

        members = type_node.xpath('edm:Member', namespaces=config.namespaces)

        next_value = 0
        for member in members:
            name = member.get('Name')
            value = member.get('Value')

            if value is not None:
                next_value = int(value)

            vtype = valid_types[underlying_type]
            if not vtype[0] < next_value < vtype[1]:
                raise exceptions.PyODataParserError(f'Value {next_value} is out of range for type {underlying_type}')

            emember = elements.EnumMember(etype, name, next_value)
            etype._member.append(emember)

            next_value += 1

        return etype
    except (exceptions.PyODataParserError, AttributeError) as ex:
        config.err_policy(policies.ParserError.ENUM_TYPE).resolve(ex)
        return elements.NullType(type_node.get('Name'))


def build_entity_set(config, entity_set_node):
    name = entity_set_node.get('Name')
    et_info = elements.Types.parse_type_name(entity_set_node.get('EntityType'))

    nav_prop_bins = []
    for nav_prop_bin in entity_set_node.xpath('edm:NavigationPropertyBinding', namespaces=config.namespaces):
        nav_prop_bins.append(elements.build_element('NavigationPropertyBinding', config, node=nav_prop_bin,
                                                    et_info=et_info))

    # TODO: create a class SAP attributes
    addressable = elements.sap_attribute_get_bool(entity_set_node, 'addressable', True)
    creatable = elements.sap_attribute_get_bool(entity_set_node, 'creatable', True)
    updatable = elements.sap_attribute_get_bool(entity_set_node, 'updatable', True)
    deletable = elements.sap_attribute_get_bool(entity_set_node, 'deletable', True)
    searchable = elements.sap_attribute_get_bool(entity_set_node, 'searchable', False)
    countable = elements.sap_attribute_get_bool(entity_set_node, 'countable', True)
    pageable = elements.sap_attribute_get_bool(entity_set_node, 'pageable', True)
    topable = elements.sap_attribute_get_bool(entity_set_node, 'topable', pageable)
    req_filter = elements.sap_attribute_get_bool(entity_set_node, 'requires-filter', False)
    label = elements.sap_attribute_get_string(entity_set_node, 'label')

    if config.odata_version == v4.ODataV4:
        return v4.v4_elements.EntitySet(name, et_info, addressable, creatable, updatable, deletable, searchable,
                                        countable, pageable, topable, req_filter, label, nav_prop_bins)

    return elements.EntitySet(name, et_info, addressable, creatable, updatable, deletable, searchable, countable,
                              pageable, topable, req_filter, label)


def build_value_helper(config, target, annotation_node, schema):
    label = None
    collection_path = None
    search_supported = False
    params_node = None

    for prop_value in annotation_node.xpath('edm:Record/edm:PropertyValue', namespaces=config.annotation_namespace):
        rprop = prop_value.get('Property')
        if rprop == 'Label':
            label = prop_value.get('String')
        elif rprop == 'CollectionPath':
            collection_path = prop_value.get('String')
        elif rprop == 'SearchSupported':
            search_supported = prop_value.get('Bool')
        elif rprop == 'Parameters':
            params_node = prop_value

    value_helper = elements.ValueHelper(target, collection_path, label, search_supported)

    if params_node is not None:
        for prm in params_node.xpath('edm:Collection/edm:Record', namespaces=config.annotation_namespace):
            param = elements.build_element(elements.ValueHelperParameter, config, value_help_parameter_node=prm)
            param.value_helper = value_helper
            value_helper._parameters.append(param)

    try:
        try:
            value_helper.entity_set = schema.entity_set(
                value_helper.collection_path, namespace=value_helper.element_namespace)
        except KeyError:
            raise RuntimeError(f'Entity Set {value_helper.collection_path} '
                               f'for {value_helper} does not exist')

        try:
            vh_type = schema.typ(value_helper.proprty_entity_type_name,
                                 namespace=value_helper.element_namespace)
        except KeyError:
            raise RuntimeError(f'Target Type {value_helper.proprty_entity_type_name} '
                               f'of {value_helper} does not exist')

        try:
            target_proprty = vh_type.proprty(value_helper.proprty_name)
        except KeyError:
            raise RuntimeError(f'Target Property {value_helper.proprty_name} '
                               f'of {vh_type} as defined in {value_helper} does not exist')

        value_helper.proprty = target_proprty
        target_proprty.value_helper = value_helper
    except (RuntimeError, exceptions.PyODataModelError) as ex:
        config.err_policy(policies.ParserError.ANNOTATION).resolve(ex)


def build_value_helper_parameter(config, value_help_parameter_node):
    typ = value_help_parameter_node.get('Type')
    direction = config.sap_value_helper_directions[typ]
    local_prop_name = None
    list_prop_name = None
    for pval in value_help_parameter_node.xpath('edm:PropertyValue', namespaces=config.annotation_namespace):
        pv_name = pval.get('Property')
        if pv_name == 'LocalDataProperty':
            local_prop_name = pval.get('PropertyPath')
        elif pv_name == 'ValueListProperty':
            list_prop_name = pval.get('String')

    return elements.ValueHelperParameter(direction, local_prop_name, list_prop_name)


# pylint: disable=too-many-locals
def build_function_import(config: pyodata.Config, function_import_node):
    name = function_import_node.get('Name')
    entity_set = function_import_node.get('EntitySet')
    http_method = elements.metadata_attribute_get(function_import_node, 'HttpMethod')

    rt_type = function_import_node.get('ReturnType')
    rt_info = None if rt_type is None else elements.Types.parse_type_name(rt_type)
    print(name, rt_type, rt_info)

    parameters = dict()
    for param in function_import_node.xpath('edm:Parameter', namespaces=config.namespaces):
        param_name = param.get('Name')
        param_type_info = elements.Types.parse_type_name(param.get('Type'))
        param_nullable = param.get('Nullable')
        param_max_length = param.get('MaxLength')
        param_precision = param.get('Precision')
        param_scale = param.get('Scale')
        param_mode = param.get('Mode')

        parameters[param_name] = elements.FunctionImportParameter(param_name, param_type_info, param_nullable,
                                                                  param_max_length, param_precision, param_scale,
                                                                  param_mode)

    return elements.FunctionImport(name, rt_info, entity_set, parameters, http_method)
