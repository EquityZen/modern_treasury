from modern_treasury.objects.response.account_details import AccountDetailsResponse
from modern_treasury.objects.response.address import AddressResponse
from modern_treasury.objects.response.routing_details import RoutingDetailsResponse


class InternalAccountResponse:
    def __init__(self, json):
        self.json = json

    @property
    def id(self):
        return self.json.get('id')

    @property
    def account_type(self):
        return self.json.get('account_type')

    @property
    def party_name(self):
        return self.json.get('party_name')

    @property
    def party_type(self):
        return self.json.get('party_type')

    @property
    def currency(self):
        return self.json.get('currency')

    @property
    def metadata(self):
        return self.json.get('metadata')

    @property
    def live_mode(self):
        return self.json.get('live_mode')

    @property
    def created_at(self):
        return self.json.get('created_at')

    @property
    def updated_at(self):
        return self.json.get('updated_at')

    @property
    def party_address(self):
        address = self.json.get('party_address')
        if address:
            return AddressResponse(address)
        return None

    @property
    def account_details(self):
        result = self.json.get('account_details')
        if result:
           return AccountDetailsResponse(json=result)
        return None

    @property
    def routing_details(self):
        result = self.json.get('routing_details')
        if result:
            return RoutingDetailsResponse(result)
        return None

    @property
    def connection(self):
        return self.json.get('connection')
