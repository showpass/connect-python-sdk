# coding: utf-8

"""
    Connect

    Connect is the best software for distributing your tickets to where your customers already are.  # noqa: E501

    OpenAPI spec version: v1
    Contact: dev@showpass.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "Showpass Connect Python"
VERSION = "1.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Connect",
    author_email="dev@showpass.com",
    url="",
    keywords=["Swagger", "Connect"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Connect is the best software for distributing your tickets to where your customers already are.  # noqa: E501
    """
)
