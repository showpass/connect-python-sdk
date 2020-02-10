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


class InventoryPartnerBasedTicketType(object):
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
        'id': 'str',
        'name': 'str',
        'ref_id': 'str',
        'unit_price': 'str',
        'unit_price_currency': 'str',
        'fee_settings': 'object',
        'event': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ref_id': 'ref_id',
        'unit_price': 'unit_price',
        'unit_price_currency': 'unit_price_currency',
        'fee_settings': 'fee_settings',
        'event': 'event',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, ref_id=None, unit_price=None, unit_price_currency=None, fee_settings=None, event=None, description=None):  # noqa: E501
        """InventoryPartnerBasedTicketType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._ref_id = None
        self._unit_price = None
        self._unit_price_currency = None
        self._fee_settings = None
        self._event = None
        self._description = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        if ref_id is not None:
            self.ref_id = ref_id
        if unit_price is not None:
            self.unit_price = unit_price
        if unit_price_currency is not None:
            self.unit_price_currency = unit_price_currency
        if fee_settings is not None:
            self.fee_settings = fee_settings
        self.event = event
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this InventoryPartnerBasedTicketType.  # noqa: E501


        :return: The id of this InventoryPartnerBasedTicketType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryPartnerBasedTicketType.


        :param id: The id of this InventoryPartnerBasedTicketType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InventoryPartnerBasedTicketType.  # noqa: E501

        Name of the the class of ticket type. This is meant to be displayed to the customer. Only certain distribution partners support this.  # noqa: E501

        :return: The name of this InventoryPartnerBasedTicketType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InventoryPartnerBasedTicketType.

        Name of the the class of ticket type. This is meant to be displayed to the customer. Only certain distribution partners support this.  # noqa: E501

        :param name: The name of this InventoryPartnerBasedTicketType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def ref_id(self):
        """Gets the ref_id of this InventoryPartnerBasedTicketType.  # noqa: E501

        Meta field to store Partner's object id  # noqa: E501

        :return: The ref_id of this InventoryPartnerBasedTicketType.  # noqa: E501
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this InventoryPartnerBasedTicketType.

        Meta field to store Partner's object id  # noqa: E501

        :param ref_id: The ref_id of this InventoryPartnerBasedTicketType.  # noqa: E501
        :type: str
        """

        self._ref_id = ref_id

    @property
    def unit_price(self):
        """Gets the unit_price of this InventoryPartnerBasedTicketType.  # noqa: E501

        Face value price of the ticket type. This will be used for all variants of this ticket type.  # noqa: E501

        :return: The unit_price of this InventoryPartnerBasedTicketType.  # noqa: E501
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this InventoryPartnerBasedTicketType.

        Face value price of the ticket type. This will be used for all variants of this ticket type.  # noqa: E501

        :param unit_price: The unit_price of this InventoryPartnerBasedTicketType.  # noqa: E501
        :type: str
        """

        self._unit_price = unit_price

    @property
    def unit_price_currency(self):
        """Gets the unit_price_currency of this InventoryPartnerBasedTicketType.  # noqa: E501


        :return: The unit_price_currency of this InventoryPartnerBasedTicketType.  # noqa: E501
        :rtype: str
        """
        return self._unit_price_currency

    @unit_price_currency.setter
    def unit_price_currency(self, unit_price_currency):
        """Sets the unit_price_currency of this InventoryPartnerBasedTicketType.


        :param unit_price_currency: The unit_price_currency of this InventoryPartnerBasedTicketType.  # noqa: E501
        :type: str
        """

        self._unit_price_currency = unit_price_currency

    @property
    def fee_settings(self):
        """Gets the fee_settings of this InventoryPartnerBasedTicketType.  # noqa: E501


        :return: The fee_settings of this InventoryPartnerBasedTicketType.  # noqa: E501
        :rtype: object
        """
        return self._fee_settings

    @fee_settings.setter
    def fee_settings(self, fee_settings):
        """Sets the fee_settings of this InventoryPartnerBasedTicketType.


        :param fee_settings: The fee_settings of this InventoryPartnerBasedTicketType.  # noqa: E501
        :type: object
        """

        self._fee_settings = fee_settings

    @property
    def event(self):
        """Gets the event of this InventoryPartnerBasedTicketType.  # noqa: E501


        :return: The event of this InventoryPartnerBasedTicketType.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this InventoryPartnerBasedTicketType.


        :param event: The event of this InventoryPartnerBasedTicketType.  # noqa: E501
        :type: str
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def description(self):
        """Gets the description of this InventoryPartnerBasedTicketType.  # noqa: E501

        The Ticket Type's description, meant to be displayed to the customer. This field will only be displayed on supported Distribution Partners. Supported HTML tags: Heading tags: <h1>, <h2>, <h3>, <h4>, <h5>, <h6> Paragraph tag: <p> List tags: <ul>, <ol>, <li> Division tag: <div> Phrase tags: <br>, <strong>, <em>  All other tags are unsupported.  # noqa: E501

        :return: The description of this InventoryPartnerBasedTicketType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InventoryPartnerBasedTicketType.

        The Ticket Type's description, meant to be displayed to the customer. This field will only be displayed on supported Distribution Partners. Supported HTML tags: Heading tags: <h1>, <h2>, <h3>, <h4>, <h5>, <h6> Paragraph tag: <p> List tags: <ul>, <ol>, <li> Division tag: <div> Phrase tags: <br>, <strong>, <em>  All other tags are unsupported.  # noqa: E501

        :param description: The description of this InventoryPartnerBasedTicketType.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(InventoryPartnerBasedTicketType, dict):
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
        if not isinstance(other, InventoryPartnerBasedTicketType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
