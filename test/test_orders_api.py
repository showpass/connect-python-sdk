# coding: utf-8

"""
    Connect

    Connect is the best software for distributing your tickets to where your customers already are.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: dev@showpass.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import showpass_connect
from api.orders_api import OrdersApi  # noqa: E501
from showpass_connect.rest import ApiException


class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self):
        self.api = api.orders_api.OrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_orders_fulfillment(self):
        """Test case for orders_fulfillment

        """
        pass

    def test_orders_list(self):
        """Test case for orders_list

        """
        pass

    def test_orders_read(self):
        """Test case for orders_read

        """
        pass

    def test_orders_refund(self):
        """Test case for orders_refund

        """
        pass


if __name__ == '__main__':
    unittest.main()
