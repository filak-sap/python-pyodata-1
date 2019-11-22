# pylint: disable=missing-docstring

import re

import pyodata.exceptions as exceptions


class EdmStructTypeSerializer:
    """Basic implementation of (de)serialization for Edm complex types

       All properties existing in related Edm type are taken
       into account, others are ignored

       TODO: it can happen that inifinite recurision occurs for cases
       when property types are referencich each other. We need some research
       here to avoid such cases.
    """

    @staticmethod
    def to_literal(edm_type, value):

        # pylint: disable=no-self-use
        if not edm_type:
            raise exceptions.PyODataException('Cannot encode value {} without complex type information'.format(value))

        result = {}
        for type_prop in edm_type.proprties():
            if type_prop.name in value:
                result[type_prop.name] = type_prop.typ.traits.to_literal(value[type_prop.name])

        return result

    @staticmethod
    def from_json(edm_type, value):

        # pylint: disable=no-self-use
        if not edm_type:
            raise exceptions.PyODataException('Cannot decode value {} without complex type information'.format(value))

        result = {}
        for type_prop in edm_type.proprties():
            if type_prop.name in value:
                result[type_prop.name] = type_prop.typ.traits.from_json(value[type_prop.name])

        return result

    @staticmethod
    def from_literal(edm_type, value):

        # pylint: disable=no-self-use
        if not edm_type:
            raise exceptions.PyODataException('Cannot decode value {} without complex type information'.format(value))

        result = {}
        for type_prop in edm_type.proprties():
            if type_prop.name in value:
                result[type_prop.name] = type_prop.typ.traits.from_literal(value[type_prop.name])

        return result


class TypTraits:
    """Encapsulated differences between types"""

    def __repr__(self):
        return self.__class__.__name__

    # pylint: disable=no-self-use
    def to_literal(self, value):
        return value

    # pylint: disable=no-self-use
    def from_json(self, value):
        return value

    def to_json(self, value):
        return value

    def from_literal(self, value):
        return value


class EdmPrefixedTypTraits(TypTraits):
    """Is good for all types where values have form: prefix'value'"""

    def __init__(self, prefix):
        super(EdmPrefixedTypTraits, self).__init__()
        self._prefix = prefix

    def to_literal(self, value):
        return '{}\'{}\''.format(self._prefix, value)

    def from_literal(self, value):
        matches = re.match("^{}'(.*)'$".format(self._prefix), value)
        if not matches:
            raise exceptions.PyODataModelError(
                "Malformed value {0} for primitive Edm type. Expected format is {1}'value'".format(value, self._prefix))
        return matches.group(1)


class EdmStringTypTraits(TypTraits):
    """Edm.String traits"""

    # pylint: disable=no-self-use
    def to_literal(self, value):
        return '\'%s\'' % (value)

    # pylint: disable=no-self-use
    def from_json(self, value):
        return value.strip('\'')

    def from_literal(self, value):
        return value.strip('\'')


class EdmBooleanTypTraits(TypTraits):
    """Edm.Boolean traits"""

    # pylint: disable=no-self-use
    def to_literal(self, value):
        return 'true' if value else 'false'

    # pylint: disable=no-self-use
    def from_json(self, value):
        return value

    def from_literal(self, value):
        return value == 'true'


class EdmIntTypTraits(TypTraits):
    """All Edm Integer traits"""

    # pylint: disable=no-self-use
    def to_literal(self, value):
        return '%d' % (value)

    # pylint: disable=no-self-use
    def from_json(self, value):
        return int(value)

    def from_literal(self, value):
        return int(value)


class EdmLongIntTypTraits(TypTraits):
    """All Edm Integer for big numbers traits"""

    # pylint: disable=no-self-use
    def to_literal(self, value):
        return '%dL' % (value)

    # pylint: disable=no-self-use
    def from_json(self, value):
        if value[-1] == 'L':
            return int(value[:-1])

        return int(value)

    def from_literal(self, value):
        return self.from_json(value)


class EdmStructTypTraits(TypTraits):
    """Edm structural types (EntityType, ComplexType) traits"""

    def __init__(self, edm_type=None):
        super(EdmStructTypTraits, self).__init__()
        self._edm_type = edm_type

    # pylint: disable=no-self-use
    def to_literal(self, value):
        return EdmStructTypeSerializer.to_literal(self._edm_type, value)

    # pylint: disable=no-self-use
    def from_json(self, value):
        return EdmStructTypeSerializer.from_json(self._edm_type, value)

    def from_literal(self, value):
        return EdmStructTypeSerializer.from_json(self._edm_type, value)


class EnumTypTrait(TypTraits):
    def __init__(self, enum_type):
        self._enum_type = enum_type

    def to_literal(self, value):
        return f'{value.parent.namespace}.{value}'

    def from_json(self, value):
        return getattr(self._enum_type, value)

    def from_literal(self, value):
        # remove namespaces
        enum_value = value.split('.')[-1]
        # remove enum type
        name = enum_value.split("'")[1]
        return getattr(self._enum_type, name)
