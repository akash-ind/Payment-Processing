from models.BankTransaction import BankTransaction
from service.bank_detail_service import BankDetailsService

class BankTransferService:

    def __init__(self, bank_detail_service, notification_service, fraud_processing_service,
                 bank_transfer_processing_service):
        self.bank_transfer_processing_service = bank_transfer_processing_service
        self.fraud_processing_service = fraud_processing_service
        self.notification_service = notification_service
        self.bank_detail_service: BankDetailsService = bank_detail_service


    def create_bank_transfer(self, id, currency, amount, destination):

        bank_details = self.bank_detail_service.get_bank_details(id)

        bank_transaction = BankTransaction(bank_details,
                                           currency,
                                           amount,
                                           destination,
                                           self.bank_transfer_processing_service,
                                           self.fraud_processing_service,
                                           self.notification_service)

        bank_transaction.pay()

        return bank_transaction.status

