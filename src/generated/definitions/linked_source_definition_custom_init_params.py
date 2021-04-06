#
# Copyright (c) 2019 by Delphix. All rights reserved.
#
from __future__ import absolute_import
from datetime import date, datetime

from generated.definitions.base_model_ import (
    Model, GeneratedClassesError, GeneratedClassesTypeError)
import re
from generated import util

class LinkedSourceDefinitionCustomInitParams(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, property_name='', value='', validate=True):
        """LinkedSourceDefinitionCustomInitParams - a model defined in Swagger. The type of some of these
        attributes can be defined as a List[ERRORUNKNOWN]. This just means they
        are a list of any type.

            :param property_name: The property_name of this LinkedSourceDefinitionCustomInitParams.
            :type property_name: str
            :param value: The value of this LinkedSourceDefinitionCustomInitParams.
            :type value: str
            :param validate: If the validation should be done during init. This
            should only be called internally when calling from_dict.
            :type validate: bool
        """
        self.swagger_types = {
            'property_name': str,
            'value': str
        }

        self.attribute_map = {
            'property_name': 'propertyName',
            'value': 'value'
        }
        
        # Validating the attribute property_name and then saving it.
        if validate and property_name is None:
            raise GeneratedClassesError(
                "The required parameter 'property_name' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(LinkedSourceDefinitionCustomInitParams,
                                                          'property_name',
                                                          property_name,
                                                          str,
                                                          True)
        if validate and type_error:
            raise type_error
        if property_name is not None and len(property_name) > 40:
            raise GeneratedClassesError(
                "Invalid value for 'property_name', length was {} but must be less"
                " than or equal to 40.".format(len(property_name)))
        if (property_name is not None
                and not re.search('^$|^[_a-zA-Z0-9]*$', property_name)):
            raise GeneratedClassesError(
                "Invalid value for 'property_name', was '{}' but must follow the"
                " pattern '^$|^[_a-zA-Z0-9]*$'.".format(property_name))
        self._property_name = property_name

        # Validating the attribute value and then saving it.
        if validate and value is None:
            raise GeneratedClassesError(
                "The required parameter 'value' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(LinkedSourceDefinitionCustomInitParams,
                                                          'value',
                                                          value,
                                                          str,
                                                          True)
        if validate and type_error:
            raise type_error
        if value is not None and len(value) > 100:
            raise GeneratedClassesError(
                "Invalid value for 'value', length was {} but must be less"
                " than or equal to 100.".format(len(value)))
        if (value is not None
                and not re.search('^$|^[_a-zA-Z0-9]*$', value)):
            raise GeneratedClassesError(
                "Invalid value for 'value', was '{}' but must follow the"
                " pattern '^$|^[_a-zA-Z0-9]*$'.".format(value))
        self._value = value
    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The linkedSourceDefinition_customInitParams of this LinkedSourceDefinitionCustomInitParams.
        :rtype: LinkedSourceDefinitionCustomInitParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def property_name(self):
        """Gets the property_name of this LinkedSourceDefinitionCustomInitParams.


        :return: The property_name of this LinkedSourceDefinitionCustomInitParams.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this LinkedSourceDefinitionCustomInitParams.


        :param property_name: The property_name of this LinkedSourceDefinitionCustomInitParams.
        :type property_name: str
        """
        # Validating the attribute property_name and then saving it.
        if property_name is None:
            raise GeneratedClassesError(
                "The required parameter 'property_name' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(LinkedSourceDefinitionCustomInitParams,
                                                          'property_name',
                                                          property_name,
                                                          str,
                                                          True)
        if type_error:
            raise type_error
        if property_name is not None and len(property_name) > 40:
            raise GeneratedClassesError(
                "Invalid value for 'property_name', length was {} but must be less"
                " than or equal to 40.".format(len(property_name)))
        if (property_name is not None
                and not re.search('^$|^[_a-zA-Z0-9]*$', property_name)):
            raise GeneratedClassesError(
                "Invalid value for 'property_name', was '{}' but must follow the"
                " pattern '^$|^[_a-zA-Z0-9]*$'.".format(property_name))
        self._property_name = property_name

    @property
    def value(self):
        """Gets the value of this LinkedSourceDefinitionCustomInitParams.


        :return: The value of this LinkedSourceDefinitionCustomInitParams.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this LinkedSourceDefinitionCustomInitParams.


        :param value: The value of this LinkedSourceDefinitionCustomInitParams.
        :type value: str
        """
        # Validating the attribute value and then saving it.
        if value is None:
            raise GeneratedClassesError(
                "The required parameter 'value' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(LinkedSourceDefinitionCustomInitParams,
                                                          'value',
                                                          value,
                                                          str,
                                                          True)
        if type_error:
            raise type_error
        if value is not None and len(value) > 100:
            raise GeneratedClassesError(
                "Invalid value for 'value', length was {} but must be less"
                " than or equal to 100.".format(len(value)))
        if (value is not None
                and not re.search('^$|^[_a-zA-Z0-9]*$', value)):
            raise GeneratedClassesError(
                "Invalid value for 'value', was '{}' but must follow the"
                " pattern '^$|^[_a-zA-Z0-9]*$'.".format(value))
        self._value = value
