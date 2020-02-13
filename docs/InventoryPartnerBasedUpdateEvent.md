# InventoryPartnerBasedUpdateEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The name of the Event. This will be displayed on all distribution partners. | [optional] 
**description** | **str** | The event&#x27;s description, meant to be displayed to the customer. Use this field to optionally store a long form description of the event. Supported HTML tags:  Heading tags: &lt;h1&gt;, &lt;h2&gt;, &lt;h3&gt;, &lt;h4&gt;, &lt;h5&gt;, &lt;h6&gt; Paragraph tag: &lt;p&gt; List tags: &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt; Division tag: &lt;div&gt; Phrase tags: &lt;br&gt;, &lt;strong&gt;, &lt;em&gt;  All other tags are unsupported. | [optional] 
**short_description** | **str** | An optional shortened description of the event, meant to be displayed to the customer. | [optional] 
**starts_on** | **datetime** | UTC date time in which the event starts. | [optional] 
**ends_on** | **datetime** | UTC date time in which the event ends. | [optional] 
**ref_id** | **str** | Meta field to store Partner&#x27;s object id | [optional] 
**location** | [**EventLocation**](EventLocation.md) |  | [optional] 
**organization** | [**NestedOrganization**](NestedOrganization.md) |  | [optional] 
**event_uri** | **str** | URL of the event on the Inventory Partners website, or where else this event can be viewed/purchased. | [optional] 
**cover_image** | **str** | Banner image for the event. This will be the image associated with the event on distribution channels. 1200 x 628 pixels recommended. | [optional] 
**timezone** | **str** | Timezone of where the Event is located. | [optional] 
**refund_policy** | **str** | The policy outlining how refunds will be handled for this event. This will be displayed to the ticket buyers. Supported HTML tags: Heading tags: &lt;h1&gt;, &lt;h2&gt;, &lt;h3&gt;, &lt;h4&gt;, &lt;h5&gt;, &lt;h6&gt; Paragraph tag: &lt;p&gt; List tags: &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt; Division tag: &lt;div&gt; Phrase tags: &lt;br&gt;, &lt;strong&gt;, &lt;em&gt;  All other tags are unsupported. | [optional] 
**restrictions** | **str** | Restrictions that apply to this event. Using this field is strongly encouraged to provide clear expectations for customers.Examples may be: &#x27;No Children Allowed&#x27;, &#x27;18+ Event&#x27;, etc. Supported HTML tags: Paragraph tag: &lt;p&gt; List tags: &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt; Phrase tags: &lt;strong&gt;, &lt;em&gt;  All other tags are unsupported. | [optional] 
**category** | **str** | The type of the event | [optional] [default to 'OTHER']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

