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


class InventoryPartnerBasedExpandedTicketTypeVariant(object):
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
        'ref_id': 'str',
        'inventory': 'int',
        'starts_on': 'datetime',
        'ends_on': 'datetime',
        'minimum_purchase_limit': 'int',
        'purchase_limit': 'int',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ref_id': 'ref_id',
        'inventory': 'inventory',
        'starts_on': 'starts_on',
        'ends_on': 'ends_on',
        'minimum_purchase_limit': 'minimum_purchase_limit',
        'purchase_limit': 'purchase_limit',
        'description': 'description'
    }

    def __init__(self, id=None, ref_id=None, inventory=None, starts_on=None, ends_on=None, minimum_purchase_limit=None, purchase_limit=None, description=None):  # noqa: E501
        """InventoryPartnerBasedExpandedTicketTypeVariant - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._ref_id = None
        self._inventory = None
        self._starts_on = None
        self._ends_on = None
        self._minimum_purchase_limit = None
        self._purchase_limit = None
        self._description = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if ref_id is not None:
            self.ref_id = ref_id
        if inventory is not None:
            self.inventory = inventory
        if starts_on is not None:
            self.starts_on = starts_on
        if ends_on is not None:
            self.ends_on = ends_on
        if minimum_purchase_limit is not None:
            self.minimum_purchase_limit = minimum_purchase_limit
        if purchase_limit is not None:
            self.purchase_limit = purchase_limit
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501


        :return: The id of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryPartnerBasedExpandedTicketTypeVariant.


        :param id: The id of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def ref_id(self):
        """Gets the ref_id of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501

        Meta field to store Partner's object id  # noqa: E501

        :return: The ref_id of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this InventoryPartnerBasedExpandedTicketTypeVariant.

        Meta field to store Partner's object id  # noqa: E501

        :param ref_id: The ref_id of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :type: str
        """

        self._ref_id = ref_id

    @property
    def inventory(self):
        """Gets the inventory of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501

        Indicates the number of tickets of this variant that Connect has permission to sell.  # noqa: E501

        :return: The inventory of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :rtype: int
        """
        return self._inventory

    @inventory.setter
    def inventory(self, inventory):
        """Sets the inventory of this InventoryPartnerBasedExpandedTicketTypeVariant.

        Indicates the number of tickets of this variant that Connect has permission to sell.  # noqa: E501

        :param inventory: The inventory of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :type: int
        """

        self._inventory = inventory

    @property
    def starts_on(self):
        """Gets the starts_on of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501

        The UTC date time of when this variant can begin selling. Default is the time this is created.  # noqa: E501

        :return: The starts_on of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :rtype: datetime
        """
        return self._starts_on

    @starts_on.setter
    def starts_on(self, starts_on):
        """Sets the starts_on of this InventoryPartnerBasedExpandedTicketTypeVariant.

        The UTC date time of when this variant can begin selling. Default is the time this is created.  # noqa: E501

        :param starts_on: The starts_on of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :type: datetime
        """

        self._starts_on = starts_on

    @property
    def ends_on(self):
        """Gets the ends_on of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501

        The UTC date time of when this variant is no longer sellable. Default is the Event's end time.  # noqa: E501

        :return: The ends_on of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :rtype: datetime
        """
        return self._ends_on

    @ends_on.setter
    def ends_on(self, ends_on):
        """Sets the ends_on of this InventoryPartnerBasedExpandedTicketTypeVariant.

        The UTC date time of when this variant is no longer sellable. Default is the Event's end time.  # noqa: E501

        :param ends_on: The ends_on of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :type: datetime
        """

        self._ends_on = ends_on

    @property
    def minimum_purchase_limit(self):
        """Gets the minimum_purchase_limit of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501

        Enforce a minimum number of tickets that must be purchased for this variant.  # noqa: E501

        :return: The minimum_purchase_limit of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :rtype: int
        """
        return self._minimum_purchase_limit

    @minimum_purchase_limit.setter
    def minimum_purchase_limit(self, minimum_purchase_limit):
        """Sets the minimum_purchase_limit of this InventoryPartnerBasedExpandedTicketTypeVariant.

        Enforce a minimum number of tickets that must be purchased for this variant.  # noqa: E501

        :param minimum_purchase_limit: The minimum_purchase_limit of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :type: int
        """

        self._minimum_purchase_limit = minimum_purchase_limit

    @property
    def purchase_limit(self):
        """Gets the purchase_limit of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501

        Enforce a maximum number of tickets that can be purchased for this variant. The default value is 10.  # noqa: E501

        :return: The purchase_limit of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :rtype: int
        """
        return self._purchase_limit

    @purchase_limit.setter
    def purchase_limit(self, purchase_limit):
        """Sets the purchase_limit of this InventoryPartnerBasedExpandedTicketTypeVariant.

        Enforce a maximum number of tickets that can be purchased for this variant. The default value is 10.  # noqa: E501

        :param purchase_limit: The purchase_limit of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :type: int
        """

        self._purchase_limit = purchase_limit

    @property
    def description(self):
        """Gets the description of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501

        The Variant's description, meant to be displayed to the customer. This field will only be displayed on supported Distribution Partners. Supported HTML tags: Heading tags: <h1>, <h2>, <h3>, <h4>, <h5>, <h6> Paragraph tag: <p> List tags: <ul>, <ol>, <li> Division tag: <div> Phrase tags: <br>, <strong>, <em>  All other tags are unsupported.  # noqa: E501

        :return: The description of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InventoryPartnerBasedExpandedTicketTypeVariant.

        The Variant's description, meant to be displayed to the customer. This field will only be displayed on supported Distribution Partners. Supported HTML tags: Heading tags: <h1>, <h2>, <h3>, <h4>, <h5>, <h6> Paragraph tag: <p> List tags: <ul>, <ol>, <li> Division tag: <div> Phrase tags: <br>, <strong>, <em>  All other tags are unsupported.  # noqa: E501

        :param description: The description of this InventoryPartnerBasedExpandedTicketTypeVariant.  # noqa: E501
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
        if issubclass(InventoryPartnerBasedExpandedTicketTypeVariant, dict):
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
        if not isinstance(other, InventoryPartnerBasedExpandedTicketTypeVariant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other