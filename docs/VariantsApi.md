# showpass_connect.VariantsApi

All URIs are relative to *http://34.102.246.102/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**variants_create**](VariantsApi.md#variants_create) | **POST** /variants | 
[**variants_delete**](VariantsApi.md#variants_delete) | **DELETE** /variants/{id} | 
[**variants_list**](VariantsApi.md#variants_list) | **GET** /variants | 
[**variants_partial_update**](VariantsApi.md#variants_partial_update) | **PATCH** /variants/{id} | 
[**variants_read**](VariantsApi.md#variants_read) | **GET** /variants/{id} | 
[**variants_update**](VariantsApi.md#variants_update) | **PUT** /variants/{id} | 

# **variants_create**
> InventoryPartnerBasedTicketTypeVariant variants_create(body)



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
api_instance = showpass_connect.VariantsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedTicketTypeVariant() # InventoryPartnerBasedTicketTypeVariant | 

try:
    api_response = api_instance.variants_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantsApi->variants_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedTicketTypeVariant**](InventoryPartnerBasedTicketTypeVariant.md)|  | 

### Return type

[**InventoryPartnerBasedTicketTypeVariant**](InventoryPartnerBasedTicketTypeVariant.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_delete**
> variants_delete(id)



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
api_instance = showpass_connect.VariantsApi(showpass_connect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this ticket type variant.

try:
    api_instance.variants_delete(id)
except ApiException as e:
    print("Exception when calling VariantsApi->variants_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ticket type variant. | 

### Return type

void (empty response body)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_list**
> object variants_list(page=page)



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
api_instance = showpass_connect.VariantsApi(showpass_connect.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.variants_list(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantsApi->variants_list: %s\n" % e)
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

# **variants_partial_update**
> InventoryPartnerBasedTicketTypeVariant variants_partial_update(body, id)



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
api_instance = showpass_connect.VariantsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedTicketTypeVariant() # InventoryPartnerBasedTicketTypeVariant | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this ticket type variant.

try:
    api_response = api_instance.variants_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantsApi->variants_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedTicketTypeVariant**](InventoryPartnerBasedTicketTypeVariant.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this ticket type variant. | 

### Return type

[**InventoryPartnerBasedTicketTypeVariant**](InventoryPartnerBasedTicketTypeVariant.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_read**
> InventoryPartnerBasedTicketTypeVariant variants_read(id)



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
api_instance = showpass_connect.VariantsApi(showpass_connect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this ticket type variant.

try:
    api_response = api_instance.variants_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantsApi->variants_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this ticket type variant. | 

### Return type

[**InventoryPartnerBasedTicketTypeVariant**](InventoryPartnerBasedTicketTypeVariant.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variants_update**
> InventoryPartnerBasedTicketTypeVariant variants_update(body, id)



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
api_instance = showpass_connect.VariantsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedTicketTypeVariant() # InventoryPartnerBasedTicketTypeVariant | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this ticket type variant.

try:
    api_response = api_instance.variants_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VariantsApi->variants_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedTicketTypeVariant**](InventoryPartnerBasedTicketTypeVariant.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this ticket type variant. | 

### Return type

[**InventoryPartnerBasedTicketTypeVariant**](InventoryPartnerBasedTicketTypeVariant.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

