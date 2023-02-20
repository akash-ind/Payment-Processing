import uuid


class CreditCard:

    def __init__(self, credit_card_no, expiry):
        self.id = uuid.uuid4()
        self.credit_card_no = credit_card_no
        self.expiry = expiry
        self.cvv = None

    def set_cvv(self, cvv):
        self.cvv = cvv

