from models.payment import Payment
from const import Constant
from process.bank_transfer_processing_service import BankTransferProcessingService
from fraud_processing_service.fraud_processing_service import FraudProcessingService
from notification_service.NotificationService import NotificationService

class BankTransaction(Payment):

    payment_type = Constant.bank_transfer

    # Improvement: Model for Amount destination and currency
    def __init__(self, bank_details, currency, amount, destination, bank_transfer_processing_service, fraud_processing_service, notification_service):
        self.bank_details = bank_details
        self.destination = destination
        self.status = Constant.in_process
        self.bank_transfer_processing_service: BankTransferProcessingService = bank_transfer_processing_service
        self.fraud_processing_service: FraudProcessingService = fraud_processing_service
        self.notification_service: NotificationService = notification_service
        super().__init__(self.payment_type, currency, amount)

    def pay(self):
        status, response = self.bank_transfer_processing_service.process(self)

        self.add_resulting_response(response)
        if status == Constant.successful:
            if self.fraud_processing_service.is_fraud_transaction(self):
                self.status = Constant.fraud
            else:
                self.status = Constant.successful
        elif status == Constant.failed:
            self.status = Constant.failed
            self.notification_service.notify(self)





