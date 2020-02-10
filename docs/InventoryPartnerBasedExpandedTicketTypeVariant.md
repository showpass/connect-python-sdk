# InventoryPartnerBasedExpandedTicketTypeVariant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ref_id** | **str** | Meta field to store Partner&#x27;s object id | [optional] 
**inventory** | **int** | Indicates the number of tickets of this variant that Connect has permission to sell. | [optional] 
**starts_on** | **datetime** | The UTC date time of when this variant can begin selling. Default is the time this is created. | [optional] 
**ends_on** | **datetime** | The UTC date time of when this variant is no longer sellable. Default is the Event&#x27;s end time. | [optional] 
**minimum_purchase_limit** | **int** | Enforce a minimum number of tickets that must be purchased for this variant. | [optional] 
**purchase_limit** | **int** | Enforce a maximum number of tickets that can be purchased for this variant. The default value is 10. | [optional] 
**description** | **str** | The Variant&#x27;s description, meant to be displayed to the customer. This field will only be displayed on supported Distribution Partners. Supported HTML tags: Heading tags: &lt;h1&gt;, &lt;h2&gt;, &lt;h3&gt;, &lt;h4&gt;, &lt;h5&gt;, &lt;h6&gt; Paragraph tag: &lt;p&gt; List tags: &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt; Division tag: &lt;div&gt; Phrase tags: &lt;br&gt;, &lt;strong&gt;, &lt;em&gt;  All other tags are unsupported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

