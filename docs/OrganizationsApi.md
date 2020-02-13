# showpass_connect.OrganizationsApi

All URIs are relative to *http://34.102.246.102/api/v1/supplier*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organizations_create**](OrganizationsApi.md#organizations_create) | **POST** /organizations | 
[**organizations_delete**](OrganizationsApi.md#organizations_delete) | **DELETE** /organizations/{id} | 
[**organizations_list**](OrganizationsApi.md#organizations_list) | **GET** /organizations | 
[**organizations_partial_update**](OrganizationsApi.md#organizations_partial_update) | **PATCH** /organizations/{id} | 
[**organizations_read**](OrganizationsApi.md#organizations_read) | **GET** /organizations/{id} | 
[**organizations_update**](OrganizationsApi.md#organizations_update) | **PUT** /organizations/{id} | 

# **organizations_create**
> InventoryPartnerBasedOrganization organizations_create(body)



Create and manage Organizations(s).

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
api_instance = showpass_connect.OrganizationsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedOrganization() # InventoryPartnerBasedOrganization | 

try:
    api_response = api_instance.organizations_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedOrganization**](InventoryPartnerBasedOrganization.md)|  | 

### Return type

[**InventoryPartnerBasedOrganization**](InventoryPartnerBasedOrganization.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_delete**
> organizations_delete(id)



Create and manage Organizations(s).

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
api_instance = showpass_connect.OrganizationsApi(showpass_connect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this organization.

try:
    api_instance.organizations_delete(id)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this organization. | 

### Return type

void (empty response body)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_list**
> object organizations_list(page=page)



Create and manage Organizations(s).

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
api_instance = showpass_connect.OrganizationsApi(showpass_connect.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.organizations_list(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_list: %s\n" % e)
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

# **organizations_partial_update**
> InventoryPartnerBasedOrganization organizations_partial_update(body, id)



Create and manage Organizations(s).

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
api_instance = showpass_connect.OrganizationsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedOrganization() # InventoryPartnerBasedOrganization | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this organization.

try:
    api_response = api_instance.organizations_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedOrganization**](InventoryPartnerBasedOrganization.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this organization. | 

### Return type

[**InventoryPartnerBasedOrganization**](InventoryPartnerBasedOrganization.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_read**
> InventoryPartnerBasedOrganization organizations_read(id)



Create and manage Organizations(s).

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
api_instance = showpass_connect.OrganizationsApi(showpass_connect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this organization.

try:
    api_response = api_instance.organizations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this organization. | 

### Return type

[**InventoryPartnerBasedOrganization**](InventoryPartnerBasedOrganization.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_update**
> InventoryPartnerBasedOrganization organizations_update(body, id)



Create and manage Organizations(s).

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
api_instance = showpass_connect.OrganizationsApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedOrganization() # InventoryPartnerBasedOrganization | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this organization.

try:
    api_response = api_instance.organizations_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->organizations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedOrganization**](InventoryPartnerBasedOrganization.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this organization. | 

### Return type

[**InventoryPartnerBasedOrganization**](InventoryPartnerBasedOrganization.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

