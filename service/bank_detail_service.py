from models.bank_details import BankDetails

class BankDetailsService:

    def __init__(self):
        self.bank_details = dict()

    def add_bank_details(self, account_no, bank_code):
        bank_details = BankDetails(account_no, bank_code, "")
        self.bank_details[bank_details.id] = bank_details
        return bank_details


    def get_bank_details(self, id):
        return self.bank_details.get(id)