# InventoryPartnerBasedExpandedTicketType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variants** | [**list[InventoryPartnerBasedExpandedTicketTypeVariant]**](InventoryPartnerBasedExpandedTicketTypeVariant.md) |  | 
**id** | **str** |  | [optional] 
**name** | **str** | Name of the the class of ticket type. This is meant to be displayed to the customer. Only certain distribution partners support this. | 
**ref_id** | **str** | Meta field to store Partner&#x27;s object id | [optional] 
**unit_price** | **str** | Face value price of the ticket type. This will be used for all variants of this ticket type. | [optional] 
**unit_price_currency** | **str** |  | [optional] 
**fee_settings** | **object** |  | [optional] 
**event** | **str** |  | 
**description** | **str** | The Ticket Type&#x27;s description, meant to be displayed to the customer. This field will only be displayed on supported Distribution Partners. Supported HTML tags: Heading tags: &lt;h1&gt;, &lt;h2&gt;, &lt;h3&gt;, &lt;h4&gt;, &lt;h5&gt;, &lt;h6&gt; Paragraph tag: &lt;p&gt; List tags: &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt; Division tag: &lt;div&gt; Phrase tags: &lt;br&gt;, &lt;strong&gt;, &lt;em&gt;  All other tags are unsupported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

