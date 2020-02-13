# showpass_connect.OrdersApi

All URIs are relative to *http://34.102.246.102/api/v1/supplier*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_fulfillment**](OrdersApi.md#orders_fulfillment) | **POST** /orders/{id}/fulfillment | 
[**orders_list**](OrdersApi.md#orders_list) | **GET** /orders | 
[**orders_read**](OrdersApi.md#orders_read) | **GET** /orders/{id} | 
[**orders_refund**](OrdersApi.md#orders_refund) | **POST** /orders/{id}/refund | 

# **orders_fulfillment**
> InventoryPartnerBasedOrderItemFulfillment orders_fulfillment(body, id)



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
api_instance = showpass_connect.OrdersApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedOrderItemFulfillment() # InventoryPartnerBasedOrderItemFulfillment | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this Order.

try:
    api_response = api_instance.orders_fulfillment(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_fulfillment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedOrderItemFulfillment**](InventoryPartnerBasedOrderItemFulfillment.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this Order. | 

### Return type

[**InventoryPartnerBasedOrderItemFulfillment**](InventoryPartnerBasedOrderItemFulfillment.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_list**
> object orders_list(page=page)



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
api_instance = showpass_connect.OrdersApi(showpass_connect.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)

try:
    api_response = api_instance.orders_list(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_list: %s\n" % e)
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

# **orders_read**
> InventoryPartnerBasedOrder orders_read(id)



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
api_instance = showpass_connect.OrdersApi(showpass_connect.ApiClient(configuration))
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this Order.

try:
    api_response = api_instance.orders_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| A UUID string identifying this Order. | 

### Return type

[**InventoryPartnerBasedOrder**](InventoryPartnerBasedOrder.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_refund**
> InventoryPartnerBasedOrder orders_refund(body, id)



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
api_instance = showpass_connect.OrdersApi(showpass_connect.ApiClient(configuration))
body = showpass_connect.InventoryPartnerBasedOrder() # InventoryPartnerBasedOrder | 
id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | A UUID string identifying this Order.

try:
    api_response = api_instance.orders_refund(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryPartnerBasedOrder**](InventoryPartnerBasedOrder.md)|  | 
 **id** | [**str**](.md)| A UUID string identifying this Order. | 

### Return type

[**InventoryPartnerBasedOrder**](InventoryPartnerBasedOrder.md)

### Authorization

[header_api_key](../README.md#header_api_key), [query_api_key](../README.md#query_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

