# Showpass Connect Python
Connect is the best software for distributing your tickets to where your customers already are.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.1
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import showpass_connect 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import showpass_connect
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import showpass_connect
from showpass_connect.rest import ApiException
from pprint import pprint

# Configure API key authorization: header_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: query_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = showpass_connect.EventsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedEvent() # InventoryPartnerBasedEvent | 

try:
    api_response = api_instance.events_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_create: %s\n" % e)

# Configure API key authorization: header_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: query_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = showpass_connect.EventsApi(showpass_connect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this event.

try:
    api_instance.events_delete(id)
except ApiException as e:
    print("Exception when calling EventsApi->events_delete: %s\n" % e)

# Configure API key authorization: header_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: query_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = showpass_connect.EventsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedExpandedEvent() # InventoryPartnerBasedExpandedEvent | 

try:
    api_response = api_instance.events_expanded(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_expanded: %s\n" % e)

# Configure API key authorization: header_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: query_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = showpass_connect.EventsApi(showpass_connect.ApiClient(configuration))
organization = 'organization_example' # str |  (optional)
organization__in = 'organization__in_example' # str | Multiple values may be separated by commas. (optional)
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.events_list(organization=organization, organization__in=organization__in, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_list: %s\n" % e)

# Configure API key authorization: header_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: query_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = showpass_connect.EventsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedUpdateEvent() # InventoryPartnerBasedUpdateEvent | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this event.

try:
    api_response = api_instance.events_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_partial_update: %s\n" % e)

# Configure API key authorization: header_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: query_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = showpass_connect.EventsApi(showpass_connect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this event.

try:
    api_response = api_instance.events_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_read: %s\n" % e)

# Configure API key authorization: header_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'
# Configure API key authorization: query_api_key
configuration = showpass_connect.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = showpass_connect.EventsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedUpdateEvent() # InventoryPartnerBasedUpdateEvent | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this event.

try:
    api_response = api_instance.events_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_update: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://34.102.246.102/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EventsApi* | [**events_create**](docs/EventsApi.md#events_create) | **POST** /events | 
*EventsApi* | [**events_delete**](docs/EventsApi.md#events_delete) | **DELETE** /events/{id} | 
*EventsApi* | [**events_expanded**](docs/EventsApi.md#events_expanded) | **POST** /events/expanded | 
*EventsApi* | [**events_list**](docs/EventsApi.md#events_list) | **GET** /events | 
*EventsApi* | [**events_partial_update**](docs/EventsApi.md#events_partial_update) | **PATCH** /events/{id} | 
*EventsApi* | [**events_read**](docs/EventsApi.md#events_read) | **GET** /events/{id} | 
*EventsApi* | [**events_update**](docs/EventsApi.md#events_update) | **PUT** /events/{id} | 
*OrdersApi* | [**orders_fulfillment**](docs/OrdersApi.md#orders_fulfillment) | **POST** /orders/{id}/fulfillment | 
*OrdersApi* | [**orders_list**](docs/OrdersApi.md#orders_list) | **GET** /orders | 
*OrdersApi* | [**orders_read**](docs/OrdersApi.md#orders_read) | **GET** /orders/{id} | 
*OrdersApi* | [**orders_refund**](docs/OrdersApi.md#orders_refund) | **POST** /orders/{id}/refund | 
*TicketTypesApi* | [**ticket_types_create**](docs/TicketTypesApi.md#ticket_types_create) | **POST** /ticket-types | 
*TicketTypesApi* | [**ticket_types_delete**](docs/TicketTypesApi.md#ticket_types_delete) | **DELETE** /ticket-types/{id} | 
*TicketTypesApi* | [**ticket_types_expanded**](docs/TicketTypesApi.md#ticket_types_expanded) | **POST** /ticket-types/expanded | 
*TicketTypesApi* | [**ticket_types_list**](docs/TicketTypesApi.md#ticket_types_list) | **GET** /ticket-types | 
*TicketTypesApi* | [**ticket_types_partial_update**](docs/TicketTypesApi.md#ticket_types_partial_update) | **PATCH** /ticket-types/{id} | 
*TicketTypesApi* | [**ticket_types_read**](docs/TicketTypesApi.md#ticket_types_read) | **GET** /ticket-types/{id} | 
*TicketTypesApi* | [**ticket_types_update**](docs/TicketTypesApi.md#ticket_types_update) | **PUT** /ticket-types/{id} | 
*VariantsApi* | [**variants_create**](docs/VariantsApi.md#variants_create) | **POST** /variants | 
*VariantsApi* | [**variants_delete**](docs/VariantsApi.md#variants_delete) | **DELETE** /variants/{id} | 
*VariantsApi* | [**variants_list**](docs/VariantsApi.md#variants_list) | **GET** /variants | 
*VariantsApi* | [**variants_partial_update**](docs/VariantsApi.md#variants_partial_update) | **PATCH** /variants/{id} | 
*VariantsApi* | [**variants_read**](docs/VariantsApi.md#variants_read) | **GET** /variants/{id} | 
*VariantsApi* | [**variants_update**](docs/VariantsApi.md#variants_update) | **PUT** /variants/{id} | 

## Documentation For Models

 - [EventLocation](docs/EventLocation.md)
 - [InventoryPartnerBasedEvent](docs/InventoryPartnerBasedEvent.md)
 - [InventoryPartnerBasedEventExpandedTicketType](docs/InventoryPartnerBasedEventExpandedTicketType.md)
 - [InventoryPartnerBasedExpandedEvent](docs/InventoryPartnerBasedExpandedEvent.md)
 - [InventoryPartnerBasedExpandedTicketType](docs/InventoryPartnerBasedExpandedTicketType.md)
 - [InventoryPartnerBasedExpandedTicketTypeVariant](docs/InventoryPartnerBasedExpandedTicketTypeVariant.md)
 - [InventoryPartnerBasedOrder](docs/InventoryPartnerBasedOrder.md)
 - [InventoryPartnerBasedTicketType](docs/InventoryPartnerBasedTicketType.md)
 - [InventoryPartnerBasedTicketTypeVariant](docs/InventoryPartnerBasedTicketTypeVariant.md)
 - [InventoryPartnerBasedUpdateEvent](docs/InventoryPartnerBasedUpdateEvent.md)
 - [NestedOrganization](docs/NestedOrganization.md)
 - [OrderOrganization](docs/OrderOrganization.md)

## Documentation For Authorization


## google_service_account

- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string

## header_api_key

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: HTTP header

## query_api_key

- **Type**: API key
- **API key parameter name**: X-Api-Key
- **Location**: URL query string


## Author

dev@showpass.com
