# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for WatchInfo
"""
from datetime import datetime
from six import string_types

from . import client_support


class WatchInfo(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type created_at: datetime
        :type ignored: bool
        :type reason: dict
        :type repository_url: string_types
        :type subscribed: bool
        :type url: string_types
        :rtype: WatchInfo
        """

        return WatchInfo(**kwargs)

    def __init__(self, json=None, **kwargs):
        pass
        if json is None and not kwargs:
            raise j.exceptions.Value("No data or kwargs present")

        class_name = "WatchInfo"
        data = json or kwargs

        # set attributes
        data_types = [datetime]
        self.created_at = client_support.set_property(
            "created_at", data, data_types, False, [], False, False, class_name
        )
        data_types = [bool]
        self.ignored = client_support.set_property("ignored", data, data_types, False, [], False, False, class_name)
        data_types = [dict]
        self.reason = client_support.set_property("reason", data, data_types, False, [], False, False, class_name)
        data_types = [string_types]
        self.repository_url = client_support.set_property(
            "repository_url", data, data_types, False, [], False, False, class_name
        )
        data_types = [bool]
        self.subscribed = client_support.set_property(
            "subscribed", data, data_types, False, [], False, False, class_name
        )
        data_types = [string_types]
        self.url = client_support.set_property("url", data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
