#
# Copyright (c) 2019 by Delphix. All rights reserved.
#
from __future__ import absolute_import
from datetime import date, datetime

from generated.definitions.base_model_ import (
    Model, GeneratedClassesError, GeneratedClassesTypeError)
from generated import util

class SourceConfigDefinition(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, db_uniq_name=None, db_name=None, db_identity_name=None, validate=True):
        """SourceConfigDefinition - a model defined in Swagger. The type of some of these
        attributes can be defined as a List[ERRORUNKNOWN]. This just means they
        are a list of any type.

            :param db_uniq_name: The db_uniq_name of this SourceConfigDefinition.
            :type db_uniq_name: str
            :param db_name: The db_name of this SourceConfigDefinition.
            :type db_name: str
            :param db_identity_name: The db_identity_name of this SourceConfigDefinition.
            :type db_identity_name: str
            :param validate: If the validation should be done during init. This
            should only be called internally when calling from_dict.
            :type validate: bool
        """
        self.swagger_types = {
            'db_uniq_name': str,
            'db_name': str,
            'db_identity_name': str
        }

        self.attribute_map = {
            'db_uniq_name': 'dbUniqName',
            'db_name': 'dbName',
            'db_identity_name': 'dbIdentityName'
        }
        
        # Validating the attribute db_uniq_name and then saving it.
        if validate and db_uniq_name is None:
            raise GeneratedClassesError(
                "The required parameter 'db_uniq_name' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(SourceConfigDefinition,
                                                          'db_uniq_name',
                                                          db_uniq_name,
                                                          str,
                                                          True)
        if validate and type_error:
            raise type_error
        self._db_uniq_name = db_uniq_name

        # Validating the attribute db_name and then saving it.
        if validate and db_name is None:
            raise GeneratedClassesError(
                "The required parameter 'db_name' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(SourceConfigDefinition,
                                                          'db_name',
                                                          db_name,
                                                          str,
                                                          True)
        if validate and type_error:
            raise type_error
        self._db_name = db_name

        # Validating the attribute db_identity_name and then saving it.
        if validate and db_identity_name is None:
            raise GeneratedClassesError(
                "The required parameter 'db_identity_name' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(SourceConfigDefinition,
                                                          'db_identity_name',
                                                          db_identity_name,
                                                          str,
                                                          True)
        if validate and type_error:
            raise type_error
        self._db_identity_name = db_identity_name
    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The sourceConfigDefinition of this SourceConfigDefinition.
        :rtype: SourceConfigDefinition
        """
        return util.deserialize_model(dikt, cls)

    @property
    def db_uniq_name(self):
        """Gets the db_uniq_name of this SourceConfigDefinition.

        db_unique_name for staging database

        :return: The db_uniq_name of this SourceConfigDefinition.
        :rtype: str
        """
        return self._db_uniq_name

    @db_uniq_name.setter
    def db_uniq_name(self, db_uniq_name):
        """Sets the db_uniq_name of this SourceConfigDefinition.

        db_unique_name for staging database

        :param db_uniq_name: The db_uniq_name of this SourceConfigDefinition.
        :type db_uniq_name: str
        """
        # Validating the attribute db_uniq_name and then saving it.
        if db_uniq_name is None:
            raise GeneratedClassesError(
                "The required parameter 'db_uniq_name' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(SourceConfigDefinition,
                                                          'db_uniq_name',
                                                          db_uniq_name,
                                                          str,
                                                          True)
        if type_error:
            raise type_error
        self._db_uniq_name = db_uniq_name

    @property
    def db_name(self):
        """Gets the db_name of this SourceConfigDefinition.

        Must match source database db_name including case

        :return: The db_name of this SourceConfigDefinition.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this SourceConfigDefinition.

        Must match source database db_name including case

        :param db_name: The db_name of this SourceConfigDefinition.
        :type db_name: str
        """
        # Validating the attribute db_name and then saving it.
        if db_name is None:
            raise GeneratedClassesError(
                "The required parameter 'db_name' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(SourceConfigDefinition,
                                                          'db_name',
                                                          db_name,
                                                          str,
                                                          True)
        if type_error:
            raise type_error
        self._db_name = db_name

    @property
    def db_identity_name(self):
        """Gets the db_identity_name of this SourceConfigDefinition.

        Identity field

        :return: The db_identity_name of this SourceConfigDefinition.
        :rtype: str
        """
        return self._db_identity_name

    @db_identity_name.setter
    def db_identity_name(self, db_identity_name):
        """Sets the db_identity_name of this SourceConfigDefinition.

        Identity field

        :param db_identity_name: The db_identity_name of this SourceConfigDefinition.
        :type db_identity_name: str
        """
        # Validating the attribute db_identity_name and then saving it.
        if db_identity_name is None:
            raise GeneratedClassesError(
                "The required parameter 'db_identity_name' must not be 'None'.")
        type_error = GeneratedClassesTypeError.type_error(SourceConfigDefinition,
                                                          'db_identity_name',
                                                          db_identity_name,
                                                          str,
                                                          True)
        if type_error:
            raise type_error
        self._db_identity_name = db_identity_name