# coding: utf-8

"""
    Connect

    Connect is the best software for distributing your tickets to where your customers already are.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: dev@showpass.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class NestedOrganization(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'id': 'str',
        'ref_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'ref_id': 'ref_id'
    }

    def __init__(self, name=None, id=None, ref_id=None):  # noqa: E501
        """NestedOrganization - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._ref_id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if ref_id is not None:
            self.ref_id = ref_id

    @property
    def name(self):
        """Gets the name of this NestedOrganization.  # noqa: E501

        Name of the organization that hosts the event. This is meant to be displayed to the customer.  # noqa: E501

        :return: The name of this NestedOrganization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NestedOrganization.

        Name of the organization that hosts the event. This is meant to be displayed to the customer.  # noqa: E501

        :param name: The name of this NestedOrganization.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this NestedOrganization.  # noqa: E501


        :return: The id of this NestedOrganization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NestedOrganization.


        :param id: The id of this NestedOrganization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ref_id(self):
        """Gets the ref_id of this NestedOrganization.  # noqa: E501

        Meta field to store Partner's object id  # noqa: E501

        :return: The ref_id of this NestedOrganization.  # noqa: E501
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this NestedOrganization.

        Meta field to store Partner's object id  # noqa: E501

        :param ref_id: The ref_id of this NestedOrganization.  # noqa: E501
        :type: str
        """

        self._ref_id = ref_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NestedOrganization, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NestedOrganization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
