# coding: utf-8

"""
    Connect

    Connect is the best software for distributing your tickets to where your customers already are.  # noqa: E501

    OpenAPI spec version: v1
    Contact: dev@showpass.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InventoryPartnerBasedExpandedEvent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ticket_types': 'list[InventoryPartnerBasedEventExpandedTicketType]',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'short_description': 'str',
        'starts_on': 'datetime',
        'ends_on': 'datetime',
        'ref_id': 'str',
        'location': 'EventLocation',
        'organization': 'NestedOrganization',
        'event_uri': 'str',
        'cover_image': 'str',
        'timezone': 'str',
        'refund_policy': 'str',
        'restrictions': 'str',
        'category': 'str'
    }

    attribute_map = {
        'ticket_types': 'ticket_types',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'short_description': 'short_description',
        'starts_on': 'starts_on',
        'ends_on': 'ends_on',
        'ref_id': 'ref_id',
        'location': 'location',
        'organization': 'organization',
        'event_uri': 'event_uri',
        'cover_image': 'cover_image',
        'timezone': 'timezone',
        'refund_policy': 'refund_policy',
        'restrictions': 'restrictions',
        'category': 'category'
    }

    def __init__(self, ticket_types=None, id=None, name=None, description=None, short_description=None, starts_on=None, ends_on=None, ref_id=None, location=None, organization=None, event_uri=None, cover_image=None, timezone=None, refund_policy=None, restrictions=None, category='OTHER'):  # noqa: E501
        """InventoryPartnerBasedExpandedEvent - a model defined in Swagger"""  # noqa: E501
        self._ticket_types = None
        self._id = None
        self._name = None
        self._description = None
        self._short_description = None
        self._starts_on = None
        self._ends_on = None
        self._ref_id = None
        self._location = None
        self._organization = None
        self._event_uri = None
        self._cover_image = None
        self._timezone = None
        self._refund_policy = None
        self._restrictions = None
        self._category = None
        self.discriminator = None
        self.ticket_types = ticket_types
        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if short_description is not None:
            self.short_description = short_description
        if starts_on is not None:
            self.starts_on = starts_on
        if ends_on is not None:
            self.ends_on = ends_on
        if ref_id is not None:
            self.ref_id = ref_id
        self.location = location
        self.organization = organization
        if event_uri is not None:
            self.event_uri = event_uri
        if cover_image is not None:
            self.cover_image = cover_image
        if timezone is not None:
            self.timezone = timezone
        if refund_policy is not None:
            self.refund_policy = refund_policy
        if restrictions is not None:
            self.restrictions = restrictions
        if category is not None:
            self.category = category

    @property
    def ticket_types(self):
        """Gets the ticket_types of this InventoryPartnerBasedExpandedEvent.  # noqa: E501


        :return: The ticket_types of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: list[InventoryPartnerBasedEventExpandedTicketType]
        """
        return self._ticket_types

    @ticket_types.setter
    def ticket_types(self, ticket_types):
        """Sets the ticket_types of this InventoryPartnerBasedExpandedEvent.


        :param ticket_types: The ticket_types of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: list[InventoryPartnerBasedEventExpandedTicketType]
        """
        if ticket_types is None:
            raise ValueError("Invalid value for `ticket_types`, must not be `None`")  # noqa: E501

        self._ticket_types = ticket_types

    @property
    def id(self):
        """Gets the id of this InventoryPartnerBasedExpandedEvent.  # noqa: E501


        :return: The id of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InventoryPartnerBasedExpandedEvent.


        :param id: The id of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        The name of the Event. This will be displayed on all distribution partners.  # noqa: E501

        :return: The name of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InventoryPartnerBasedExpandedEvent.

        The name of the Event. This will be displayed on all distribution partners.  # noqa: E501

        :param name: The name of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        The event's description, meant to be displayed to the customer. Use this field to optionally store a long form description of the event. Supported HTML tags:  Heading tags: h1, h2, h3, h4, h5, h6 Paragraph tag: p List tags: ul, ol, li Division tag: div Phrase tags: br, strong, em All other tags are unsupported.  # noqa: E501

        :return: The description of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InventoryPartnerBasedExpandedEvent.

        The event's description, meant to be displayed to the customer. Use this field to optionally store a long form description of the event. Supported HTML tags:  Heading tags: h1, h2, h3, h4, h5, h6 Paragraph tag: p List tags: ul, ol, li Division tag: div Phrase tags: br, strong, em All other tags are unsupported.  # noqa: E501

        :param description: The description of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def short_description(self):
        """Gets the short_description of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        An optional shortened description of the event, meant to be displayed to the customer.  # noqa: E501

        :return: The short_description of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this InventoryPartnerBasedExpandedEvent.

        An optional shortened description of the event, meant to be displayed to the customer.  # noqa: E501

        :param short_description: The short_description of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def starts_on(self):
        """Gets the starts_on of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        UTC date time in which the event starts.  # noqa: E501

        :return: The starts_on of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._starts_on

    @starts_on.setter
    def starts_on(self, starts_on):
        """Sets the starts_on of this InventoryPartnerBasedExpandedEvent.

        UTC date time in which the event starts.  # noqa: E501

        :param starts_on: The starts_on of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: datetime
        """

        self._starts_on = starts_on

    @property
    def ends_on(self):
        """Gets the ends_on of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        UTC date time in which the event ends.  # noqa: E501

        :return: The ends_on of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._ends_on

    @ends_on.setter
    def ends_on(self, ends_on):
        """Sets the ends_on of this InventoryPartnerBasedExpandedEvent.

        UTC date time in which the event ends.  # noqa: E501

        :param ends_on: The ends_on of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: datetime
        """

        self._ends_on = ends_on

    @property
    def ref_id(self):
        """Gets the ref_id of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        Meta field to store Partner's object id  # noqa: E501

        :return: The ref_id of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this InventoryPartnerBasedExpandedEvent.

        Meta field to store Partner's object id  # noqa: E501

        :param ref_id: The ref_id of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """

        self._ref_id = ref_id

    @property
    def location(self):
        """Gets the location of this InventoryPartnerBasedExpandedEvent.  # noqa: E501


        :return: The location of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: EventLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this InventoryPartnerBasedExpandedEvent.


        :param location: The location of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: EventLocation
        """
        if location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def organization(self):
        """Gets the organization of this InventoryPartnerBasedExpandedEvent.  # noqa: E501


        :return: The organization of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: NestedOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this InventoryPartnerBasedExpandedEvent.


        :param organization: The organization of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: NestedOrganization
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def event_uri(self):
        """Gets the event_uri of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        URL of the event on the Inventory Partners website, or where else this event can be viewed/purchased.  # noqa: E501

        :return: The event_uri of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._event_uri

    @event_uri.setter
    def event_uri(self, event_uri):
        """Sets the event_uri of this InventoryPartnerBasedExpandedEvent.

        URL of the event on the Inventory Partners website, or where else this event can be viewed/purchased.  # noqa: E501

        :param event_uri: The event_uri of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """

        self._event_uri = event_uri

    @property
    def cover_image(self):
        """Gets the cover_image of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        Banner image for the event. This will be the image associated with the event on distribution channels. 1200 x 628 pixels recommended.  # noqa: E501

        :return: The cover_image of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._cover_image

    @cover_image.setter
    def cover_image(self, cover_image):
        """Sets the cover_image of this InventoryPartnerBasedExpandedEvent.

        Banner image for the event. This will be the image associated with the event on distribution channels. 1200 x 628 pixels recommended.  # noqa: E501

        :param cover_image: The cover_image of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """

        self._cover_image = cover_image

    @property
    def timezone(self):
        """Gets the timezone of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        Timezone of where the Event is located.  # noqa: E501

        :return: The timezone of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this InventoryPartnerBasedExpandedEvent.

        Timezone of where the Event is located.  # noqa: E501

        :param timezone: The timezone of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["Africa/Abidjan", "Africa/Accra", "Africa/Addis_Ababa", "Africa/Algiers", "Africa/Asmara", "Africa/Bamako", "Africa/Bangui", "Africa/Banjul", "Africa/Bissau", "Africa/Blantyre", "Africa/Brazzaville", "Africa/Bujumbura", "Africa/Cairo", "Africa/Casablanca", "Africa/Ceuta", "Africa/Conakry", "Africa/Dakar", "Africa/Dar_es_Salaam", "Africa/Djibouti", "Africa/Douala", "Africa/El_Aaiun", "Africa/Freetown", "Africa/Gaborone", "Africa/Harare", "Africa/Johannesburg", "Africa/Juba", "Africa/Kampala", "Africa/Khartoum", "Africa/Kigali", "Africa/Kinshasa", "Africa/Lagos", "Africa/Libreville", "Africa/Lome", "Africa/Luanda", "Africa/Lubumbashi", "Africa/Lusaka", "Africa/Malabo", "Africa/Maputo", "Africa/Maseru", "Africa/Mbabane", "Africa/Mogadishu", "Africa/Monrovia", "Africa/Nairobi", "Africa/Ndjamena", "Africa/Niamey", "Africa/Nouakchott", "Africa/Ouagadougou", "Africa/Porto-Novo", "Africa/Sao_Tome", "Africa/Tripoli", "Africa/Tunis", "Africa/Windhoek", "America/Adak", "America/Anchorage", "America/Anguilla", "America/Antigua", "America/Araguaina", "America/Argentina/Buenos_Aires", "America/Argentina/Catamarca", "America/Argentina/Cordoba", "America/Argentina/Jujuy", "America/Argentina/La_Rioja", "America/Argentina/Mendoza", "America/Argentina/Rio_Gallegos", "America/Argentina/Salta", "America/Argentina/San_Juan", "America/Argentina/San_Luis", "America/Argentina/Tucuman", "America/Argentina/Ushuaia", "America/Aruba", "America/Asuncion", "America/Atikokan", "America/Bahia", "America/Bahia_Banderas", "America/Barbados", "America/Belem", "America/Belize", "America/Blanc-Sablon", "America/Boa_Vista", "America/Bogota", "America/Boise", "America/Cambridge_Bay", "America/Campo_Grande", "America/Cancun", "America/Caracas", "America/Cayenne", "America/Cayman", "America/Chicago", "America/Chihuahua", "America/Costa_Rica", "America/Creston", "America/Cuiaba", "America/Curacao", "America/Danmarkshavn", "America/Dawson", "America/Dawson_Creek", "America/Denver", "America/Detroit", "America/Dominica", "America/Edmonton", "America/Eirunepe", "America/El_Salvador", "America/Fort_Nelson", "America/Fortaleza", "America/Glace_Bay", "America/Godthab", "America/Goose_Bay", "America/Grand_Turk", "America/Grenada", "America/Guadeloupe", "America/Guatemala", "America/Guayaquil", "America/Guyana", "America/Halifax", "America/Havana", "America/Hermosillo", "America/Indiana/Indianapolis", "America/Indiana/Knox", "America/Indiana/Marengo", "America/Indiana/Petersburg", "America/Indiana/Tell_City", "America/Indiana/Vevay", "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Inuvik", "America/Iqaluit", "America/Jamaica", "America/Juneau", "America/Kentucky/Louisville", "America/Kentucky/Monticello", "America/Kralendijk", "America/La_Paz", "America/Lima", "America/Los_Angeles", "America/Lower_Princes", "America/Maceio", "America/Managua", "America/Manaus", "America/Marigot", "America/Martinique", "America/Matamoros", "America/Mazatlan", "America/Menominee", "America/Merida", "America/Metlakatla", "America/Mexico_City", "America/Miquelon", "America/Moncton", "America/Monterrey", "America/Montevideo", "America/Montserrat", "America/Nassau", "America/New_York", "America/Nipigon", "America/Nome", "America/Noronha", "America/North_Dakota/Beulah", "America/North_Dakota/Center", "America/North_Dakota/New_Salem", "America/Ojinaga", "America/Panama", "America/Pangnirtung", "America/Paramaribo", "America/Phoenix", "America/Port-au-Prince", "America/Port_of_Spain", "America/Porto_Velho", "America/Puerto_Rico", "America/Punta_Arenas", "America/Rainy_River", "America/Rankin_Inlet", "America/Recife", "America/Regina", "America/Resolute", "America/Rio_Branco", "America/Santarem", "America/Santiago", "America/Santo_Domingo", "America/Sao_Paulo", "America/Scoresbysund", "America/Sitka", "America/St_Barthelemy", "America/St_Johns", "America/St_Kitts", "America/St_Lucia", "America/St_Thomas", "America/St_Vincent", "America/Swift_Current", "America/Tegucigalpa", "America/Thule", "America/Thunder_Bay", "America/Tijuana", "America/Toronto", "America/Tortola", "America/Vancouver", "America/Whitehorse", "America/Winnipeg", "America/Yakutat", "America/Yellowknife", "Antarctica/Casey", "Antarctica/Davis", "Antarctica/DumontDUrville", "Antarctica/Macquarie", "Antarctica/Mawson", "Antarctica/McMurdo", "Antarctica/Palmer", "Antarctica/Rothera", "Antarctica/Syowa", "Antarctica/Troll", "Antarctica/Vostok", "Arctic/Longyearbyen", "Asia/Aden", "Asia/Almaty", "Asia/Amman", "Asia/Anadyr", "Asia/Aqtau", "Asia/Aqtobe", "Asia/Ashgabat", "Asia/Atyrau", "Asia/Baghdad", "Asia/Bahrain", "Asia/Baku", "Asia/Bangkok", "Asia/Barnaul", "Asia/Beirut", "Asia/Bishkek", "Asia/Brunei", "Asia/Chita", "Asia/Choibalsan", "Asia/Colombo", "Asia/Damascus", "Asia/Dhaka", "Asia/Dili", "Asia/Dubai", "Asia/Dushanbe", "Asia/Famagusta", "Asia/Gaza", "Asia/Hebron", "Asia/Ho_Chi_Minh", "Asia/Hong_Kong", "Asia/Hovd", "Asia/Irkutsk", "Asia/Jakarta", "Asia/Jayapura", "Asia/Jerusalem", "Asia/Kabul", "Asia/Kamchatka", "Asia/Karachi", "Asia/Kathmandu", "Asia/Khandyga", "Asia/Kolkata", "Asia/Krasnoyarsk", "Asia/Kuala_Lumpur", "Asia/Kuching", "Asia/Kuwait", "Asia/Macau", "Asia/Magadan", "Asia/Makassar", "Asia/Manila", "Asia/Muscat", "Asia/Nicosia", "Asia/Novokuznetsk", "Asia/Novosibirsk", "Asia/Omsk", "Asia/Oral", "Asia/Phnom_Penh", "Asia/Pontianak", "Asia/Pyongyang", "Asia/Qatar", "Asia/Qostanay", "Asia/Qyzylorda", "Asia/Riyadh", "Asia/Sakhalin", "Asia/Samarkand", "Asia/Seoul", "Asia/Shanghai", "Asia/Singapore", "Asia/Srednekolymsk", "Asia/Taipei", "Asia/Tashkent", "Asia/Tbilisi", "Asia/Tehran", "Asia/Thimphu", "Asia/Tokyo", "Asia/Tomsk", "Asia/Ulaanbaatar", "Asia/Urumqi", "Asia/Ust-Nera", "Asia/Vientiane", "Asia/Vladivostok", "Asia/Yakutsk", "Asia/Yangon", "Asia/Yekaterinburg", "Asia/Yerevan", "Atlantic/Azores", "Atlantic/Bermuda", "Atlantic/Canary", "Atlantic/Cape_Verde", "Atlantic/Faroe", "Atlantic/Madeira", "Atlantic/Reykjavik", "Atlantic/South_Georgia", "Atlantic/St_Helena", "Atlantic/Stanley", "Australia/Adelaide", "Australia/Brisbane", "Australia/Broken_Hill", "Australia/Currie", "Australia/Darwin", "Australia/Eucla", "Australia/Hobart", "Australia/Lindeman", "Australia/Lord_Howe", "Australia/Melbourne", "Australia/Perth", "Australia/Sydney", "Canada/Atlantic", "Canada/Central", "Canada/Eastern", "Canada/Mountain", "Canada/Newfoundland", "Canada/Pacific", "Europe/Amsterdam", "Europe/Andorra", "Europe/Astrakhan", "Europe/Athens", "Europe/Belgrade", "Europe/Berlin", "Europe/Bratislava", "Europe/Brussels", "Europe/Bucharest", "Europe/Budapest", "Europe/Busingen", "Europe/Chisinau", "Europe/Copenhagen", "Europe/Dublin", "Europe/Gibraltar", "Europe/Guernsey", "Europe/Helsinki", "Europe/Isle_of_Man", "Europe/Istanbul", "Europe/Jersey", "Europe/Kaliningrad", "Europe/Kiev", "Europe/Kirov", "Europe/Lisbon", "Europe/Ljubljana", "Europe/London", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta", "Europe/Mariehamn", "Europe/Minsk", "Europe/Monaco", "Europe/Moscow", "Europe/Oslo", "Europe/Paris", "Europe/Podgorica", "Europe/Prague", "Europe/Riga", "Europe/Rome", "Europe/Samara", "Europe/San_Marino", "Europe/Sarajevo", "Europe/Saratov", "Europe/Simferopol", "Europe/Skopje", "Europe/Sofia", "Europe/Stockholm", "Europe/Tallinn", "Europe/Tirane", "Europe/Ulyanovsk", "Europe/Uzhgorod", "Europe/Vaduz", "Europe/Vatican", "Europe/Vienna", "Europe/Vilnius", "Europe/Volgograd", "Europe/Warsaw", "Europe/Zagreb", "Europe/Zaporozhye", "Europe/Zurich", "GMT", "Indian/Antananarivo", "Indian/Chagos", "Indian/Christmas", "Indian/Cocos", "Indian/Comoro", "Indian/Kerguelen", "Indian/Mahe", "Indian/Maldives", "Indian/Mauritius", "Indian/Mayotte", "Indian/Reunion", "Pacific/Apia", "Pacific/Auckland", "Pacific/Bougainville", "Pacific/Chatham", "Pacific/Chuuk", "Pacific/Easter", "Pacific/Efate", "Pacific/Enderbury", "Pacific/Fakaofo", "Pacific/Fiji", "Pacific/Funafuti", "Pacific/Galapagos", "Pacific/Gambier", "Pacific/Guadalcanal", "Pacific/Guam", "Pacific/Honolulu", "Pacific/Kiritimati", "Pacific/Kosrae", "Pacific/Kwajalein", "Pacific/Majuro", "Pacific/Marquesas", "Pacific/Midway", "Pacific/Nauru", "Pacific/Niue", "Pacific/Norfolk", "Pacific/Noumea", "Pacific/Pago_Pago", "Pacific/Palau", "Pacific/Pitcairn", "Pacific/Pohnpei", "Pacific/Port_Moresby", "Pacific/Rarotonga", "Pacific/Saipan", "Pacific/Tahiti", "Pacific/Tarawa", "Pacific/Tongatapu", "Pacific/Wake", "Pacific/Wallis", "US/Alaska", "US/Arizona", "US/Central", "US/Eastern", "US/Hawaii", "US/Mountain", "US/Pacific", "UTC"]  # noqa: E501
        if timezone not in allowed_values:
            raise ValueError(
                "Invalid value for `timezone` ({0}), must be one of {1}"  # noqa: E501
                .format(timezone, allowed_values)
            )

        self._timezone = timezone

    @property
    def refund_policy(self):
        """Gets the refund_policy of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        The policy outlining how refunds will be handled for this event. This will be displayed to the ticket buyers. Supported HTML tags: Heading tags: h1, h2, h3, h4, h5, h6 Paragraph tag: p List tags: ul, ol, li Division tag: div Phrase tags: br, strong, em  All other tags are unsupported.  # noqa: E501

        :return: The refund_policy of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._refund_policy

    @refund_policy.setter
    def refund_policy(self, refund_policy):
        """Sets the refund_policy of this InventoryPartnerBasedExpandedEvent.

        The policy outlining how refunds will be handled for this event. This will be displayed to the ticket buyers. Supported HTML tags: Heading tags: h1, h2, h3, h4, h5, h6 Paragraph tag: p List tags: ul, ol, li Division tag: div Phrase tags: br, strong, em  All other tags are unsupported.  # noqa: E501

        :param refund_policy: The refund_policy of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """

        self._refund_policy = refund_policy

    @property
    def restrictions(self):
        """Gets the restrictions of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        Restrictions that apply to this event. Using this field is strongly encouraged to provide clear expectations for customers.Examples may be: 'No Children Allowed', '18+ Event', etc. Supported HTML tags: Paragraph tag: p List tags: ul, ol, li Phrase tags: strong, em All other tags are unsupported.  # noqa: E501

        :return: The restrictions of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this InventoryPartnerBasedExpandedEvent.

        Restrictions that apply to this event. Using this field is strongly encouraged to provide clear expectations for customers.Examples may be: 'No Children Allowed', '18+ Event', etc. Supported HTML tags: Paragraph tag: p List tags: ul, ol, li Phrase tags: strong, em All other tags are unsupported.  # noqa: E501

        :param restrictions: The restrictions of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """

        self._restrictions = restrictions

    @property
    def category(self):
        """Gets the category of this InventoryPartnerBasedExpandedEvent.  # noqa: E501

        The type of the event  # noqa: E501

        :return: The category of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this InventoryPartnerBasedExpandedEvent.

        The type of the event  # noqa: E501

        :param category: The category of this InventoryPartnerBasedExpandedEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["OTHER", "CONCERT", "SPORTS", "THEATRE", "EXHIBIT", "FESTIVAL", "RELIGIOUS", "CONFERENCE", "LECTURE", "FILM", "WORKSHOP", "ART", "BOOK", "FUNDRAISER", "VOLUNTEERING", "FAMILY", "DANCE", "COMEDY", "MEETUP", "FITNESS", "FOOD"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InventoryPartnerBasedExpandedEvent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InventoryPartnerBasedExpandedEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
