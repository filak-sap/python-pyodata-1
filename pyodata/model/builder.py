"""Metadata Builder Implementation"""

import io
from lxml import etree

import pyodata.config as pyodata
import pyodata.exceptions as exceptions
import pyodata.model.elements as elements
import pyodata.v2 as odata_v2


ANNOTATION_NAMESPACES = {
    'edm': 'http://docs.oasis-open.org/odata/ns/edm',
    'edmx': 'http://docs.oasis-open.org/odata/ns/edmx'
}

SAP_VALUE_HELPER_DIRECTIONS = {
    'com.sap.vocabularies.Common.v1.ValueListParameterIn': elements.ValueHelperParameter.Direction.In,
    'com.sap.vocabularies.Common.v1.ValueListParameterInOut': elements.ValueHelperParameter.Direction.InOut,
    'com.sap.vocabularies.Common.v1.ValueListParameterOut': elements.ValueHelperParameter.Direction.Out,
    'com.sap.vocabularies.Common.v1.ValueListParameterDisplayOnly': elements.ValueHelperParameter.Direction.DisplayOnly,
    'com.sap.vocabularies.Common.v1.ValueListParameterFilterOnly': elements.ValueHelperParameter.Direction.FilterOnly
}


# pylint: disable=protected-access
class MetadataBuilder:
    """Metadata builder"""

    EDMX_WHITELIST = [
        'http://schemas.microsoft.com/ado/2007/06/edmx',
        'http://docs.oasis-open.org/odata/ns/edmx',
    ]

    EDM_WHITELIST = [
        'http://schemas.microsoft.com/ado/2006/04/edm',
        'http://schemas.microsoft.com/ado/2007/05/edm',
        'http://schemas.microsoft.com/ado/2008/09/edm',
        'http://schemas.microsoft.com/ado/2009/11/edm',
        'http://docs.oasis-open.org/odata/ns/edm'
    ]

    def __init__(self, xml, config=None):
        self._xml = xml

        if config is None:
            config = pyodata.Config(odata_v2.ODataV2)
        self._config = config

    # pylint: disable=missing-docstring
    @property
    def config(self) -> pyodata.Config:
        return self._config

    def build(self):
        """ Build model from the XML metadata"""

        if isinstance(self._xml, str):
            mdf = io.StringIO(self._xml)
        elif isinstance(self._xml, bytes):
            mdf = io.BytesIO(self._xml)
        else:
            raise TypeError('Expected bytes or str type on metadata_xml, got : {0}'.format(type(self._xml)))

        namespaces = self._config.namespaces
        xml = etree.parse(mdf)
        edmx = xml.getroot()

        try:
            dataservices = next((child for child in edmx if etree.QName(child.tag).localname == 'DataServices'))
        except StopIteration:
            raise exceptions.PyODataParserError('Metadata document is missing the element DataServices')

        try:
            schema = next((child for child in dataservices if etree.QName(child.tag).localname == 'Schema'))
        except StopIteration:
            raise exceptions.PyODataParserError('Metadata document is missing the element Schema')

        if 'edmx' not in self._config.namespaces:
            namespace = etree.QName(edmx.tag).namespace

            if namespace not in self.EDMX_WHITELIST:
                raise exceptions.PyODataParserError(f'Unsupported Edmx namespace - {namespace}')

            namespaces['edmx'] = namespace

        if 'edm' not in self._config.namespaces:
            namespace = etree.QName(schema.tag).namespace

            if namespace not in self.EDM_WHITELIST:
                raise exceptions.PyODataParserError(f'Unsupported Schema namespace - {namespace}')

            namespaces['edm'] = namespace

        self._config.namespaces = namespaces

        self._config._sap_value_helper_directions = SAP_VALUE_HELPER_DIRECTIONS
        self._config._annotation_namespaces = ANNOTATION_NAMESPACES

        self.update_alias(self.get_aliases(xml, self._config), self._config)

        edm_schemas = xml.xpath('/edmx:Edmx/edmx:DataServices/edm:Schema', namespaces=self._config.namespaces)
        return elements.build_element(elements.Schema, self._config, schema_nodes=edm_schemas)

    @staticmethod
    def get_aliases(edmx, config: pyodata.Config):
        """Get all aliases"""

        # aliases = collections.defaultdict(set)
        aliases = {}
        edm_root = edmx.xpath('/edmx:Edmx', namespaces=config.namespaces)
        if edm_root:
            edm_ref_includes = edm_root[0].xpath('edmx:Reference/edmx:Include', namespaces=config.annotation_namespace)
            for ref_incl in edm_ref_includes:
                namespace = ref_incl.get('Namespace')
                alias = ref_incl.get('Alias')
                if namespace is not None and alias is not None:
                    aliases[alias] = namespace
                    # aliases[namespace].add(alias)

        return aliases

    @staticmethod
    def update_alias(aliases, config: pyodata.Config):
        """Update config with aliases"""
        config.aliases = aliases
        helper_direction_keys = list(config.sap_value_helper_directions.keys())

        for direction_key in helper_direction_keys:
            namespace, suffix = direction_key.rsplit('.', 1)
            for alias, alias_namespace in aliases.items():
                if alias_namespace == namespace:
                    config._sap_value_helper_directions[alias + '.' + suffix] = \
                        config.sap_value_helper_directions[direction_key]


def schema_from_xml(metadata_xml, namespaces=None):
    """Parses XML data and returns Schema representing OData Metadata"""

    meta = MetadataBuilder(
        metadata_xml,
        config=pyodata.Config(
            odata_v2.ODataV2,
            xml_namespaces=namespaces,
        ))

    return meta.build()
