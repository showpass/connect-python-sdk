# showpass_connect.TicketTypesApi

All URIs are relative to *http://34.102.246.102/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ticket_types_create**](TicketTypesApi.md#ticket_types_create) | **POST** /ticket-types | 
[**ticket_types_delete**](TicketTypesApi.md#ticket_types_delete) | **DELETE** /ticket-types/{id} | 
[**ticket_types_expanded**](TicketTypesApi.md#ticket_types_expanded) | **POST** /ticket-types/expanded | 
[**ticket_types_list**](TicketTypesApi.md#ticket_types_list) | **GET** /ticket-types | 
[**ticket_types_partial_update**](TicketTypesApi.md#ticket_types_partial_update) | **PATCH** /ticket-types/{id} | 
[**ticket_types_read**](TicketTypesApi.md#ticket_types_read) | **GET** /ticket-types/{id} | 
[**ticket_types_update**](TicketTypesApi.md#ticket_types_update) | **PUT** /ticket-types/{id} | 

# **ticket_types_create**
> InventoryPartnerBasedTicketType ticket_types_create(body)



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
api_instance = showpass_connect.TicketTypesApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedTicketType() # InventoryPartnerBasedTicketType | 

try:
    api_response = api_instance.ticket_types_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedTicketType**](InventoryPartnerBasedTicketType.md)|  | 

### Return type

[**InventoryPartnerBasedTicketType**](InventoryPartnerBasedTicketType.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_types_delete**
> ticket_types_delete(id)



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
api_instance = showpass_connect.TicketTypesApi(showpass_connect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this ticket type.

try:
    api_instance.ticket_types_delete(id)
except ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ticket type. | 

### Return type

void (empty response body)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_types_expanded**
> InventoryPartnerBasedExpandedTicketType ticket_types_expanded(body)



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
api_instance = showpass_connect.TicketTypesApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedExpandedTicketType() # InventoryPartnerBasedExpandedTicketType | 

try:
    api_response = api_instance.ticket_types_expanded(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_expanded: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedExpandedTicketType**](InventoryPartnerBasedExpandedTicketType.md)|  | 

### Return type

[**InventoryPartnerBasedExpandedTicketType**](InventoryPartnerBasedExpandedTicketType.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_types_list**
> object ticket_types_list(page=page)



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
api_instance = showpass_connect.TicketTypesApi(showpass_connect.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.ticket_types_list(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

**object**

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_types_partial_update**
> InventoryPartnerBasedTicketType ticket_types_partial_update(body, id)



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
api_instance = showpass_connect.TicketTypesApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedTicketType() # InventoryPartnerBasedTicketType | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this ticket type.

try:
    api_response = api_instance.ticket_types_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedTicketType**](InventoryPartnerBasedTicketType.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this ticket type. | 

### Return type

[**InventoryPartnerBasedTicketType**](InventoryPartnerBasedTicketType.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_types_read**
> InventoryPartnerBasedTicketType ticket_types_read(id)



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
api_instance = showpass_connect.TicketTypesApi(showpass_connect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this ticket type.

try:
    api_response = api_instance.ticket_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ticket type. | 

### Return type

[**InventoryPartnerBasedTicketType**](InventoryPartnerBasedTicketType.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ticket_types_update**
> InventoryPartnerBasedTicketType ticket_types_update(body, id)



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
api_instance = showpass_connect.TicketTypesApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedTicketType() # InventoryPartnerBasedTicketType | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this ticket type.

try:
    api_response = api_instance.ticket_types_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketTypesApi->ticket_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedTicketType**](InventoryPartnerBasedTicketType.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this ticket type. | 

### Return type

[**InventoryPartnerBasedTicketType**](InventoryPartnerBasedTicketType.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

