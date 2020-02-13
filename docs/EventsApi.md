# showpass_connect.EventsApi

All URIs are relative to *http://34.102.246.102/api/v1/supplier*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_create**](EventsApi.md#events_create) | **POST** /events | 
[**events_delete**](EventsApi.md#events_delete) | **DELETE** /events/{id} | 
[**events_expanded**](EventsApi.md#events_expanded) | **POST** /events/expanded | 
[**events_list**](EventsApi.md#events_list) | **GET** /events | 
[**events_partial_update**](EventsApi.md#events_partial_update) | **PATCH** /events/{id} | 
[**events_read**](EventsApi.md#events_read) | **GET** /events/{id} | 
[**events_update**](EventsApi.md#events_update) | **PUT** /events/{id} | 

# **events_create**
> InventoryPartnerBasedEvent events_create(body)



Create and manage Event(s). The '/expanded' action allows you to create an Event, TicketType, and TicketTypeVariants in one operation

### Example
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedEvent**](InventoryPartnerBasedEvent.md)|  | 

### Return type

[**InventoryPartnerBasedEvent**](InventoryPartnerBasedEvent.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_delete**
> events_delete(id)



Create and manage Event(s). The '/expanded' action allows you to create an Event, TicketType, and TicketTypeVariants in one operation

### Example
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
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this event.

try:
    api_instance.events_delete(id)
except ApiException as e:
    print("Exception when calling EventsApi->events_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this event. | 

### Return type

void (empty response body)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_expanded**
> InventoryPartnerBasedExpandedEvent events_expanded(body)



Create and manage Event(s). The '/expanded' action allows you to create an Event, TicketType, and TicketTypeVariants in one operation

### Example
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
body = showpass_connect.InventoryPartnerBasedExpandedEvent() # InventoryPartnerBasedExpandedEvent | 

try:
    api_response = api_instance.events_expanded(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_expanded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedExpandedEvent**](InventoryPartnerBasedExpandedEvent.md)|  | 

### Return type

[**InventoryPartnerBasedExpandedEvent**](InventoryPartnerBasedExpandedEvent.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_list**
> list[InventoryPartnerBasedEvent] events_list(organization=organization, organization__in=organization__in, page=page)



Create and manage Event(s). The '/expanded' action allows you to create an Event, TicketType, and TicketTypeVariants in one operation

### Example
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
organization = 'organization_example' # str |  (optional)
organization__in = 'organization__in_example' # str | Multiple values may be separated by commas. (optional)
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.events_list(organization=organization, organization__in=organization__in, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | [optional] 
 **organization__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**list[InventoryPartnerBasedEvent]**](InventoryPartnerBasedEvent.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_partial_update**
> InventoryPartnerBasedUpdateEvent events_partial_update(body, id)



Create and manage Event(s). The '/expanded' action allows you to create an Event, TicketType, and TicketTypeVariants in one operation

### Example
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
body = showpass_connect.InventoryPartnerBasedUpdateEvent() # InventoryPartnerBasedUpdateEvent | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this event.

try:
    api_response = api_instance.events_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedUpdateEvent**](InventoryPartnerBasedUpdateEvent.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this event. | 

### Return type

[**InventoryPartnerBasedUpdateEvent**](InventoryPartnerBasedUpdateEvent.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_read**
> InventoryPartnerBasedEvent events_read(id)



Create and manage Event(s). The '/expanded' action allows you to create an Event, TicketType, and TicketTypeVariants in one operation

### Example
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
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this event.

try:
    api_response = api_instance.events_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this event. | 

### Return type

[**InventoryPartnerBasedEvent**](InventoryPartnerBasedEvent.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_update**
> InventoryPartnerBasedUpdateEvent events_update(body, id)



Create and manage Event(s). The '/expanded' action allows you to create an Event, TicketType, and TicketTypeVariants in one operation

### Example
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
body = showpass_connect.InventoryPartnerBasedUpdateEvent() # InventoryPartnerBasedUpdateEvent | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this event.

try:
    api_response = api_instance.events_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedUpdateEvent**](InventoryPartnerBasedUpdateEvent.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this event. | 

### Return type

[**InventoryPartnerBasedUpdateEvent**](InventoryPartnerBasedUpdateEvent.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

