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
**description** | **str** | The Ticket Type&#x27;s description, meant to be displayed to the customer. This field will only be displayed on supported Distribution Partners. This will act as a default description for any variants created. Supported HTML tags: Heading tags: h1, h2, h3, h4, h5, h6 Paragraph tag: p List tags: ul, ol, li Division tag: div Phrase tags: br, strong, em  All other tags are unsupported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

