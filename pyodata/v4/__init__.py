""" This module represents implementation of ODATA V4 """

from typing import List

import pyodata.config as conf

import pyodata.model.elements as base_elements
import pyodata.v4.elements as v4_elements

import pyodata.model.type_traits as base_traits
import pyodata.v4.type_traits as v4_traits

import pyodata.model.build_functions as base_build_functions
import pyodata.v4.build_functions as v4_build_functions



def build_entity_set_v4(config, entity_set_node, name, et_info, addressable, creatable, updatable, deletable, searchable,
                        countable, pageable, topable, req_filter, label, nav_prop_bins):
    nav_prop_bins = []
    for nav_prop_bin in entity_set_node.xpath('edm:NavigationPropertyBinding', namespaces=config.namespaces):
        nav_prop_bins.append(base_elements.build_element('NavigationPropertyBinding', config, node=nav_prop_bin,
                             et_info=et_info))

    return odata_v4.v4_elements.EntitySet(name, et_info, addressable, creatable, updatable, deletable, searchable,
                                          countable, pageable, topable, req_filter, label, nav_prop_bins)


def build_entity_set_with_v4_builder(config, entity_set_node):
    """Adapter inserting the V4 specific builder"""

    return base_build_functions.build_entity_set(config, entity_set_node, builder=builder)


class ODataV4(conf.ODATAVersion):
    """ Definition of OData V4 """

    @staticmethod
    def build_functions():
        return {
            base_elements.StructTypeProperty: base_build_functions.build_struct_type_property,
            base_elements.StructType: base_build_functions.build_struct_type,
            v4_elements.NavigationTypeProperty: v4_build_functions.build_navigation_type_property,
            v4_elements.NavigationPropertyBinding: v4_build_functions.build_navigation_property_binding,
            base_elements.EnumType: base_build_functions.build_enum_type,
            base_elements.ComplexType: base_build_functions.build_complex_type,
            base_elements.EntityType: base_build_functions.build_entity_type,
            v4_elements.EntitySet: build_entity_set_with_v4_builder,
            base_elements.Typ: v4_build_functions.build_type_definition,
            base_elements.Schema: v4_build_functions.build_schema,
        }

    @staticmethod
    def primitive_types() -> List[base_elements.Typ]:
        # TODO: We currently lack support for:
        #   'Edm.Geometry',
        #   'Edm.GeometryPoint',
        #   'Edm.GeometryLineString',
        #   'Edm.GeometryPolygon',
        #   'Edm.GeometryMultiPoint',
        #   'Edm.GeometryMultiLineString',
        #   'Edm.GeometryMultiPolygon',
        #   'Edm.GeometryCollection',

        return [
            base_elements.Typ('Null', 'null'),
            base_elements.Typ('Edm.Binary', '', v4_traits.EdmDoubleQuotesEncapsulatedTypTraits()),
            base_elements.Typ('Edm.Boolean', 'false', base_traits.EdmBooleanTypTraits()),
            base_elements.Typ('Edm.Byte', '0'),
            base_elements.Typ('Edm.Date', '0000-00-00', v4_traits.EdmDateTypTraits()),
            base_elements.Typ('Edm.Decimal', '0.0'),
            base_elements.Typ('Edm.Double', '0.0'),
            base_elements.Typ('Edm.Duration', 'P', v4_traits.EdmDuration()),
            base_elements.Typ('Edm.Stream', 'null', v4_traits.EdmDoubleQuotesEncapsulatedTypTraits()),
            base_elements.Typ('Edm.Single', '0.0', v4_traits.EdmDoubleQuotesEncapsulatedTypTraits()),
            base_elements.Typ('Edm.Guid', '\"00000000-0000-0000-0000-000000000000\"',
                              v4_traits.EdmDoubleQuotesEncapsulatedTypTraits()),
            base_elements.Typ('Edm.Int16', '0', base_traits.EdmIntTypTraits()),
            base_elements.Typ('Edm.Int32', '0', base_traits.EdmIntTypTraits()),
            base_elements.Typ('Edm.Int64', '0', base_traits.EdmIntTypTraits()),
            base_elements.Typ('Edm.SByte', '0'),
            base_elements.Typ('Edm.String', '\"\"', v4_traits.EdmDoubleQuotesEncapsulatedTypTraits()),
            base_elements.Typ('Edm.TimeOfDay', '00:00:00', v4_traits.EdmTimeOfDay()),
            base_elements.Typ('Edm.DateTimeOffset', '0000-00-00T00:00:00', v4_traits.EdmDateTimeOffsetTypTraits()),
            base_elements.Typ('Edm.Geography', '', v4_traits.GeoTypeTraits()),
            base_elements.Typ('Edm.GeographyPoint', '', v4_traits.GeoTypeTraits()),
            base_elements.Typ('Edm.GeographyLineString', '', v4_traits.GeoTypeTraits()),
            base_elements.Typ('Edm.GeographyPolygon', '', v4_traits.GeoTypeTraits()),
            base_elements.Typ('Edm.GeographyMultiPoint', '', v4_traits.GeoTypeTraits()),
            base_elements.Typ('Edm.GeographyMultiLineString', '', v4_traits.GeoTypeTraits()),
            base_elements.Typ('Edm.GeographyMultiPolygon', '', v4_traits.GeoTypeTraits()),
        ]

    @staticmethod
    def annotations():
        return {
            v4_elements.Unit: v4_build_functions.build_unit_annotation
        }
