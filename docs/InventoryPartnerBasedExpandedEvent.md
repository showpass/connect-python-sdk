# InventoryPartnerBasedExpandedEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_types** | [**list[InventoryPartnerBasedEventExpandedTicketType]**](InventoryPartnerBasedEventExpandedTicketType.md) |  | 
**id** | **str** |  | [optional] 
**name** | **str** | The name of the Event. This will be displayed on all distribution partners. | 
**description** | **str** | The event&#x27;s description, meant to be displayed to the customer. Use this field to optionally store a long form description of the event. Supported HTML tags:  Heading tags: h1, h2, h3, h4, h5, h6 Paragraph tag: p List tags: ul, ol, li Division tag: div Phrase tags: br, strong, em All other tags are unsupported. | [optional] 
**short_description** | **str** | An optional shortened description of the event, meant to be displayed to the customer. | [optional] 
**starts_on** | **datetime** | UTC date time in which the event starts. | [optional] 
**ends_on** | **datetime** | UTC date time in which the event ends. | [optional] 
**ref_id** | **str** | Meta field to store Partner&#x27;s object id | [optional] 
**location** | [**EventLocation**](EventLocation.md) |  | 
**organization** | [**NestedOrganization**](NestedOrganization.md) |  | 
**event_uri** | **str** | URL of the event on the Inventory Partners website, or where else this event can be viewed/purchased. | [optional] 
**cover_image** | **str** | Banner image for the event. This will be the image associated with the event on distribution channels. 1200 x 628 pixels recommended. | [optional] 
**timezone** | **str** | Timezone of where the Event is located. | [optional] 
**refund_policy** | **str** | The policy outlining how refunds will be handled for this event. This will be displayed to the ticket buyers. Supported HTML tags: Heading tags: h1, h2, h3, h4, h5, h6 Paragraph tag: p List tags: ul, ol, li Division tag: div Phrase tags: br, strong, em  All other tags are unsupported. | [optional] 
**restrictions** | **str** | Restrictions that apply to this event. Using this field is strongly encouraged to provide clear expectations for customers.Examples may be: &#x27;No Children Allowed&#x27;, &#x27;18+ Event&#x27;, etc. Supported HTML tags: Paragraph tag: p List tags: ul, ol, li Phrase tags: strong, em All other tags are unsupported. | [optional] 
**category** | **str** | The type of the event | [optional] [default to 'OTHER']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

