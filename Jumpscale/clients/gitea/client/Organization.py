# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for Organization
"""
from six import string_types

from . import client_support


class Organization(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type avatar_url: string_types
        :type description: string_types
        :type full_name: string_types
        :type id: int
        :type location: string_types
        :type username: string_types
        :type website: string_types
        :rtype: Organization
        """

        return Organization(**kwargs)

    def __init__(self, json=None, **kwargs):
        pass
        if json is None and not kwargs:
            raise j.exceptions.Value("No data or kwargs present")

        class_name = "Organization"
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.avatar_url = client_support.set_property(
            "avatar_url", data, data_types, False, [], False, False, class_name
        )
        data_types = [string_types]
        self.description = client_support.set_property(
            "description", data, data_types, False, [], False, False, class_name
        )
        data_types = [string_types]
        self.full_name = client_support.set_property("full_name", data, data_types, False, [], False, False, class_name)
        data_types = [int]
        self.id = client_support.set_property("id", data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.location = client_support.set_property("location", data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.username = client_support.set_property("username", data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.website = client_support.set_property("website", data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
