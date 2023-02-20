import uuid


class BankDetails:
    def __init__(self, account_no, bank_code, name):
        self.id = uuid.uuid4()
        self.name = name
        self.account_no = account_no
        self.bank_code = bank_code
        self.name = name


