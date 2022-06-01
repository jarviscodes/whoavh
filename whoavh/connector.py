import ovh
import webbrowser


class Currency(object):
    def __init__(self, code, symbol):
        self.code = code
        self.symbol = symbol

    @classmethod
    def from_dictionary(cls, dictionary):
        code = dictionary["code"]
        symbol = dictionary["symbol"]
        return cls(code, symbol)

    def __str__(self):
        return f"[{self.symbol}]({self.code})"


class OVHCustomer(object):
    def __init__(
        self,
        currency,
        company_id_number,
        birthday,
        customer_code,
        spare_email,
        vat_number,
        fax_number,
        address,
        sex,
        email,
        nic_handle,
        ovh_subsidiary,
        legal_form,
        ovh_company,
        phone_number,
        italian_sdi,
        state,
        corporation_type,
        birth_city,
        country,
        city,
        language,
        name,
        national_id_number,
        phone_country,
        zip_code,
        first_name,
        area,
    ):
        self.currency = currency
        self.company_id_number = company_id_number
        self.birthday = birthday
        self.customer_code = customer_code
        self.spare_email = spare_email
        self.vat_number = vat_number
        self.fax_number = fax_number
        self.address = address
        self.sex = sex
        self.email = email
        self.nic_handle = nic_handle
        self.ovh_subsidiary = ovh_subsidiary
        self.legal_form = legal_form
        self.ovh_company = ovh_company
        self.phone_number = phone_number
        self.italian_sdi = italian_sdi
        self.state = state
        self.corporation_type = corporation_type
        self.birth_city = birth_city
        self.country = country
        self.city = city
        self.language = language
        self.name = name
        self.national_id_number = national_id_number
        self.phone_country = phone_country
        self.zip_code = zip_code
        self.first_name = first_name
        self.area = area

    @classmethod
    def from_dictionary(cls, dictionary):
        currency_dict = dictionary.get("currency", None)
        if currency_dict:
            currency = Currency.from_dictionary(currency_dict)
        else:
            currency = currency_dict

        company_id_number = dictionary.get("companyNationalIdentificationNumber", None)
        birthday = dictionary.get("birthDay", None)
        customer_code = dictionary.get("customerCode", None)
        spare_email = dictionary.get("spareEmail", None)
        vat_number = dictionary.get("vat", None)
        fax_number = dictionary.get("fax", None)
        address = dictionary.get("address", None)
        sex = dictionary.get("sex", None)
        email = dictionary.get("email", None)
        nic_handle = dictionary.get("nichandle", None)
        ovh_subsidiary = dictionary.get("ovhSubsidiary", None)
        legal_form = dictionary.get("legalform", None)
        ovh_company = dictionary.get("ovhCompany", None)
        phone_number = dictionary.get("phone", None)
        italian_sdi = dictionary.get("italianSDI", None)
        state = dictionary.get("state", None)
        corporation_type = dictionary.get("corporationType", None)
        birth_city = dictionary.get("birthCity", None)
        country = dictionary.get("country", None)
        city = dictionary.get("city", None)
        language = dictionary.get("language", None)
        name = dictionary.get("name", None)
        national_id_number = dictionary.get("nationalIdentificationNumber", None)
        phone_country = dictionary.get("phoneCountry", None)
        zip_code = dictionary.get("zip", None)
        first_name = dictionary.get("firstname", None)
        area = dictionary.get("area", None)

        return cls(
            currency=currency,
            company_id_number=company_id_number,
            birthday=birthday,
            customer_code=customer_code,
            spare_email=spare_email,
            vat_number=vat_number,
            fax_number=fax_number,
            address=address,
            sex=sex,
            email=email,
            nic_handle=nic_handle,
            ovh_subsidiary=ovh_subsidiary,
            legal_form=legal_form,
            ovh_company=ovh_company,
            phone_number=phone_number,
            italian_sdi=italian_sdi,
            state=state,
            corporation_type=corporation_type,
            birth_city=birth_city,
            country=country,
            city=city,
            language=language,
            name=name,
            national_id_number=national_id_number,
            phone_country=phone_country,
            zip_code=zip_code,
            first_name=first_name,
            area=area,
        )

    def __str__(self):
        return f"[{self.first_name}, {self.name}] ({self.company_id_number})"


class OVHAppConnector(object):
    def __init__(self, from_conf_file=True, new_consumer_key=True):
        # TODO: Add config file parser / validator
        if from_conf_file:
            # The client is the basic endpoint connector
            self.client = ovh.Client()

        if new_consumer_key:
            # The Key_Request is the request that allows your app to access certain paths
            self.key_request = self.client.new_consumer_key_request()

            # Here we request RO Access to the "/me" path.
            self.key_request.add_rules(ovh.API_READ_ONLY, "/me")

            # For the purpose of our App, we'd also need /domain RO for example
            self.key_request.add_rules(ovh.API_READ_ONLY, "/domain")

        self.consumer_key_response = self.key_request.request()

        # Point browser to validation URL
        _validation_url = self.consumer_key_response["validationUrl"]
        webbrowser.open(_validation_url)

    def get_client_data(self):
        client_data = self.client.get("/me")
        print(client_data)

    def get_consumer_key_token(self):
        # TODO: Store Token in .conf file for reuse.
        self.consumer_key = self.consumer_key_response["consumerKey"]
        print(self.consumer_key)
