import uuid


class Payment:
    def __init__(self, type, currency, amount):
        self.payment_id = uuid.uuid4()
        self.type = type
        self.currency = currency
        self.amount = amount
        self.response = None

    def pay(self):
        raise NotImplementedError

    def add_resulting_response(self, response):
        self.response = response


