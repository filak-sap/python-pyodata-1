""" This module represents implementation of ODATA V2 """

import logging
from typing import List

import pyodata.config as conf

import pyodata.model.type_traits as base_traits
import pyodata.v2.type_traits as v2_traits

import pyodata.model.elements as base_elements
import pyodata.v2.elements as v2_elements

import pyodata.model.build_functions as base_build_functions
import pyodata.v2.build_functions as v2_build_functions


def modlog():
    """ Logging function for debugging."""
    return logging.getLogger("v2")


class ODataV2(conf.ODATAVersion):
    """ Definition of OData V2 """

    @staticmethod
    def build_functions():
        return {
            base_elements.StructTypeProperty: base_build_functions.build_struct_type_property,
            base_elements.StructType: base_build_functions.build_struct_type,
            v2_elements.NavigationTypeProperty: v2_build_functions.build_navigation_type_property,
            base_elements.ComplexType: base_build_functions.build_complex_type,
            base_elements.EntityType: base_build_functions.build_entity_type,
            base_elements.EntitySet: base_build_functions.build_entity_set,
            v2_elements.EndRole: v2_build_functions.build_end_role,
            v2_elements.ReferentialConstraint: v2_build_functions.build_referential_constraint,
            v2_elements.Association: v2_build_functions.build_association,
            v2_elements.AssociationSetEndRole: v2_build_functions.build_association_set_end_role,
            v2_elements.AssociationSet: v2_build_functions.build_association_set,
            base_elements.ValueHelperParameter: base_build_functions.build_value_helper_parameter,
            base_elements.FunctionImport: base_build_functions.build_function_import,
            v2_elements.Schema: v2_build_functions.build_schema
        }

    @staticmethod
    def primitive_types() -> List[base_elements.Typ]:
        return [
            base_elements.Typ('Null', 'null'),
            base_elements.Typ('Edm.Binary', 'binary\'\''),
            base_elements.Typ('Edm.Boolean', 'false', base_traits.EdmBooleanTypTraits()),
            base_elements.Typ('Edm.Byte', '0'),
            base_elements.Typ('Edm.DateTime', 'datetime\'2000-01-01T00:00\'', v2_traits.EdmDateTimeTypTraits()),
            base_elements.Typ('Edm.Decimal', '0.0M'),
            base_elements.Typ('Edm.Double', '0.0d'),
            base_elements.Typ('Edm.Single', '0.0f'),
            base_elements.Typ('Edm.Guid', 'guid\'00000000-0000-0000-0000-000000000000\'',
                              base_traits.EdmPrefixedTypTraits('guid')),
            base_elements.Typ('Edm.Int16', '0', base_traits.EdmIntTypTraits()),
            base_elements.Typ('Edm.Int32', '0', base_traits.EdmIntTypTraits()),
            base_elements.Typ('Edm.Int64', '0L', base_traits.EdmLongIntTypTraits()),
            base_elements.Typ('Edm.SByte', '0'),
            base_elements.Typ('Edm.String', '\'\'', base_traits.EdmStringTypTraits()),
            base_elements.Typ('Edm.Time', 'time\'PT00H00M\''),
            base_elements.Typ('Edm.DateTimeOffset', 'datetimeoffset\'0000-00-00T00:00:00\'')
        ]

    @staticmethod
    def annotations():
        return {
            base_elements.ValueHelper: base_build_functions.build_value_helper
        }
