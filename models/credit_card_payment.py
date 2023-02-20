from models.payment import Payment
from const import Constant
from process.credit_card_processing_service import CreditCardProcessingService
from fraud_processing_service.fraud_processing_service import FraudProcessingService
from notification_service.NotificationService import NotificationService

class CreditCardPayment(Payment):

    payment_type = Constant.credit_card_payment

    def __init__(self, credit_card, currency, amount, destination, credit_card_processing_service, fraud_processing_service, notification_service):
        self.credit_card = credit_card
        self.destination = destination
        self.status = Constant.in_process
        self.credit_card_processing_service: CreditCardProcessingService = credit_card_processing_service
        self.fraud_processing_service: FraudProcessingService = fraud_processing_service
        self.notification_service: NotificationService = notification_service
        super().__init__(self.payment_type, currency, amount)

    def pay(self):
        status, response = self.credit_card_processing_service.process(self)

        self.add_resulting_response(response)
        if status == Constant.successful:
            if self.fraud_processing_service.is_fraud_transaction(self):
                self.status = Constant.fraud
            else:
                self.status = Constant.successful
        elif status == Constant.failed:
            self.status = Constant.failed
            self.notification_service.notify(self)





