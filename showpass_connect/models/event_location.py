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


class EventLocation(object):
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
        'business_name': 'str',
        'unit_number': 'str',
        'street_number': 'str',
        'street_name': 'str',
        'city': 'str',
        'country': 'str',
        'geographical_region': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'business_name': 'business_name',
        'unit_number': 'unit_number',
        'street_number': 'street_number',
        'street_name': 'street_name',
        'city': 'city',
        'country': 'country',
        'geographical_region': 'geographical_region',
        'postal_code': 'postal_code'
    }

    def __init__(self, business_name=None, unit_number=None, street_number=None, street_name=None, city=None, country=None, geographical_region=None, postal_code=None):  # noqa: E501
        """EventLocation - a model defined in Swagger"""  # noqa: E501
        self._business_name = None
        self._unit_number = None
        self._street_number = None
        self._street_name = None
        self._city = None
        self._country = None
        self._geographical_region = None
        self._postal_code = None
        self.discriminator = None
        self.business_name = business_name
        if unit_number is not None:
            self.unit_number = unit_number
        self.street_number = street_number
        self.street_name = street_name
        self.city = city
        if country is not None:
            self.country = country
        self.geographical_region = geographical_region
        self.postal_code = postal_code

    @property
    def business_name(self):
        """Gets the business_name of this EventLocation.  # noqa: E501

        Name of the business or place.  # noqa: E501

        :return: The business_name of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this EventLocation.

        Name of the business or place.  # noqa: E501

        :param business_name: The business_name of this EventLocation.  # noqa: E501
        :type: str
        """
        if business_name is None:
            raise ValueError("Invalid value for `business_name`, must not be `None`")  # noqa: E501

        self._business_name = business_name

    @property
    def unit_number(self):
        """Gets the unit_number of this EventLocation.  # noqa: E501

        Apartment or building number.  # noqa: E501

        :return: The unit_number of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._unit_number

    @unit_number.setter
    def unit_number(self, unit_number):
        """Sets the unit_number of this EventLocation.

        Apartment or building number.  # noqa: E501

        :param unit_number: The unit_number of this EventLocation.  # noqa: E501
        :type: str
        """

        self._unit_number = unit_number

    @property
    def street_number(self):
        """Gets the street_number of this EventLocation.  # noqa: E501


        :return: The street_number of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._street_number

    @street_number.setter
    def street_number(self, street_number):
        """Sets the street_number of this EventLocation.


        :param street_number: The street_number of this EventLocation.  # noqa: E501
        :type: str
        """
        if street_number is None:
            raise ValueError("Invalid value for `street_number`, must not be `None`")  # noqa: E501

        self._street_number = street_number

    @property
    def street_name(self):
        """Gets the street_name of this EventLocation.  # noqa: E501


        :return: The street_name of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._street_name

    @street_name.setter
    def street_name(self, street_name):
        """Sets the street_name of this EventLocation.


        :param street_name: The street_name of this EventLocation.  # noqa: E501
        :type: str
        """
        if street_name is None:
            raise ValueError("Invalid value for `street_name`, must not be `None`")  # noqa: E501

        self._street_name = street_name

    @property
    def city(self):
        """Gets the city of this EventLocation.  # noqa: E501


        :return: The city of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this EventLocation.


        :param city: The city of this EventLocation.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def country(self):
        """Gets the country of this EventLocation.  # noqa: E501


        :return: The country of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this EventLocation.


        :param country: The country of this EventLocation.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def geographical_region(self):
        """Gets the geographical_region of this EventLocation.  # noqa: E501

        Province or state of where the event occurs.  # noqa: E501

        :return: The geographical_region of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._geographical_region

    @geographical_region.setter
    def geographical_region(self, geographical_region):
        """Sets the geographical_region of this EventLocation.

        Province or state of where the event occurs.  # noqa: E501

        :param geographical_region: The geographical_region of this EventLocation.  # noqa: E501
        :type: str
        """
        if geographical_region is None:
            raise ValueError("Invalid value for `geographical_region`, must not be `None`")  # noqa: E501

        self._geographical_region = geographical_region

    @property
    def postal_code(self):
        """Gets the postal_code of this EventLocation.  # noqa: E501

        Postal code or ZIP code of the event location.  # noqa: E501

        :return: The postal_code of this EventLocation.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this EventLocation.

        Postal code or ZIP code of the event location.  # noqa: E501

        :param postal_code: The postal_code of this EventLocation.  # noqa: E501
        :type: str
        """
        if postal_code is None:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")  # noqa: E501

        self._postal_code = postal_code

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
        if issubclass(EventLocation, dict):
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
        if not isinstance(other, EventLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
