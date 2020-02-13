# coding: utf-8

"""
    Connect

    Connect is the best software for distributing your tickets to where your customers already are.  # noqa: E501

    OpenAPI spec version: v1
    Contact: dev@showpass.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InventoryPartnerBasedOrder(object):
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
        'customer_transaction_id': 'str',
        'taxes': 'str',
        'service_fees': 'str',
        'processing_fees': 'str',
        'settlement_amount': 'str',
        'status': 'str',
        'total': 'str',
        'organization': 'OrderOrganization'
    }

    attribute_map = {
        'id': 'id',
        'customer_transaction_id': 'customer_transaction_id',
        'taxes': 'taxes',
        'service_fees': 'service_fees',
        'processing_fees': 'processing_fees',
        'settlement_amount': 'settlement_amount',
        'status': 'status',
        'total': 'total',
        'organization': 'organization'
    }

    def __init__(self, id=None, customer_transaction_id=None, taxes=None, service_fees=None, processing_fees=None, settlement_amount=None, status=None, total=None, organization=None):  # noqa: E501
        """InventoryPartnerBasedOrder - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._customer_transaction_id = None
        self._taxes = None
        self._service_fees = None
        self._processing_fees = None
        self._settlement_amount = None
        self._status = None
        self._total = None
        self._organization = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if customer_transaction_id is not None:
            self.customer_transaction_id = customer_transaction_id
        if taxes is not None:
            self.taxes = taxes
        if service_fees is not None:
            self.service_fees = service_fees
        if processing_fees is not None:
            self.processing_fees = processing_fees
        if settlement_amount is not None:
            self.settlement_amount = settlement_amount
        if status is not None:
            self.status = status
        if total is not None:
            self.total = total
        if organization is not None:
            self.organization = organization

    @property
    def id(self):
        """Gets the id of this InventoryPartnerBasedOrder.  # noqa: E501


        :return: The id of this InventoryPartnerBasedOrder.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryPartnerBasedOrder.


        :param id: The id of this InventoryPartnerBasedOrder.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def customer_transaction_id(self):
        """Gets the customer_transaction_id of this InventoryPartnerBasedOrder.  # noqa: E501


        :return: The customer_transaction_id of this InventoryPartnerBasedOrder.  # noqa: E501
        :rtype: str
        """
        return self._customer_transaction_id

    @customer_transaction_id.setter
    def customer_transaction_id(self, customer_transaction_id):
        """Sets the customer_transaction_id of this InventoryPartnerBasedOrder.


        :param customer_transaction_id: The customer_transaction_id of this InventoryPartnerBasedOrder.  # noqa: E501
        :type: str
        """

        self._customer_transaction_id = customer_transaction_id

    @property
    def taxes(self):
        """Gets the taxes of this InventoryPartnerBasedOrder.  # noqa: E501


        :return: The taxes of this InventoryPartnerBasedOrder.  # noqa: E501
        :rtype: str
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this InventoryPartnerBasedOrder.


        :param taxes: The taxes of this InventoryPartnerBasedOrder.  # noqa: E501
        :type: str
        """

        self._taxes = taxes

    @property
    def service_fees(self):
        """Gets the service_fees of this InventoryPartnerBasedOrder.  # noqa: E501


        :return: The service_fees of this InventoryPartnerBasedOrder.  # noqa: E501
        :rtype: str
        """
        return self._service_fees

    @service_fees.setter
    def service_fees(self, service_fees):
        """Sets the service_fees of this InventoryPartnerBasedOrder.


        :param service_fees: The service_fees of this InventoryPartnerBasedOrder.  # noqa: E501
        :type: str
        """

        self._service_fees = service_fees

    @property
    def processing_fees(self):
        """Gets the processing_fees of this InventoryPartnerBasedOrder.  # noqa: E501


        :return: The processing_fees of this InventoryPartnerBasedOrder.  # noqa: E501
        :rtype: str
        """
        return self._processing_fees

    @processing_fees.setter
    def processing_fees(self, processing_fees):
        """Sets the processing_fees of this InventoryPartnerBasedOrder.


        :param processing_fees: The processing_fees of this InventoryPartnerBasedOrder.  # noqa: E501
        :type: str
        """

        self._processing_fees = processing_fees

    @property
    def settlement_amount(self):
        """Gets the settlement_amount of this InventoryPartnerBasedOrder.  # noqa: E501


        :return: The settlement_amount of this InventoryPartnerBasedOrder.  # noqa: E501
        :rtype: str
        """
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, settlement_amount):
        """Sets the settlement_amount of this InventoryPartnerBasedOrder.


        :param settlement_amount: The settlement_amount of this InventoryPartnerBasedOrder.  # noqa: E501
        :type: str
        """

        self._settlement_amount = settlement_amount

    @property
    def status(self):
        """Gets the status of this InventoryPartnerBasedOrder.  # noqa: E501


        :return: The status of this InventoryPartnerBasedOrder.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InventoryPartnerBasedOrder.


        :param status: The status of this InventoryPartnerBasedOrder.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def total(self):
        """Gets the total of this InventoryPartnerBasedOrder.  # noqa: E501


        :return: The total of this InventoryPartnerBasedOrder.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InventoryPartnerBasedOrder.


        :param total: The total of this InventoryPartnerBasedOrder.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def organization(self):
        """Gets the organization of this InventoryPartnerBasedOrder.  # noqa: E501


        :return: The organization of this InventoryPartnerBasedOrder.  # noqa: E501
        :rtype: OrderOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this InventoryPartnerBasedOrder.


        :param organization: The organization of this InventoryPartnerBasedOrder.  # noqa: E501
        :type: OrderOrganization
        """

        self._organization = organization

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
        if issubclass(InventoryPartnerBasedOrder, dict):
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
        if not isinstance(other, InventoryPartnerBasedOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
