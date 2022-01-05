from .address import AddressRequest


class ExternalAccountRequest():
    def __init__(self,
                 account_type:str = None,
                 party_address:AddressRequest = None,
                 idempotency_key:str = None):
        self.account_type = account_type
        self.party_address = party_address
        self.idempotency_key  = f"external_account_{idempotency_key}" if idempotency_key else None

    def to_json(self):
        result = {}
        if self.account_type:
            result['account_type'] = self.account_type
        if self.party_address:
            result['party_address'] = self.party_address.to_json()
        return result
