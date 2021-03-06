# InventoryPartnerBasedTicketTypeVariant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**ticket_type** | **str** | Reference to the class of ticket type that this variant is apart of. | 
**ref_id** | **str** | Meta field to store Partner&#x27;s object id | [optional] 
**ref_remaining_inventory** | **int** | The remaining inventory on the Partner&#x27;s system. This helps Connect make smarter inventory requests. | [optional] 
**remaining_inventory** | **str** |  | [optional] 
**inventory** | **int** | Indicates the number of tickets of this variant that Connect has permission to sell. | [optional] 
**starts_on** | **datetime** | The UTC date time of when this variant can begin selling. Default is the time this is created. | [optional] 
**ends_on** | **datetime** | The UTC date time of when this variant is no longer sellable. Default is the Event&#x27;s end time. | [optional] 
**minimum_purchase_limit** | **int** | Enforce a minimum number of tickets that must be purchased for this variant. | [optional] 
**purchase_limit** | **int** | Enforce a maximum number of tickets that can be purchased for this variant. The default value is 10. | [optional] 
**description** | **str** | The Variant&#x27;s description, meant to be displayed to the customer. This field will only be displayed on supported Distribution Partners. This will overwrite any description specified from it&#x27;s Ticket Type. Supported HTML tags: Heading tags: h1, h2, h3, h4, h5, h6 Paragraph tag: p List tags: ul, ol, li Division tag: div Phrase tags: br, strong, em  All other tags are unsupported. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

