from service.credit_card_service import CreditCardService
from process.credit_card_processing_service import CreditCardProcessingService
from notification_service.NotificationService import NotificationService
from fraud_processing_service.fraud_processing_service import FraudProcessingService
from models.credit_card_payment import CreditCardPayment

class CreditCardPaymentService:

    def __init__(self, credit_card_service, credit_card_processing_service, notification_service, fraud_processing_service):
        self.credit_card_service: CreditCardService = credit_card_service
        self.credit_card_processing_service: CreditCardProcessingService= credit_card_processing_service
        self.notification_service: NotificationService = notification_service
        self.fraud_processing_service: FraudProcessingService = fraud_processing_service

    def create_credit_card_payment(self, id, currency, amount, destination, cvv):
        credit_card = self.credit_card_service.get_credit_card(id)
        self.credit_card_service.set_cvv(credit_card, cvv)

        payment = CreditCardPayment(credit_card,
                                    currency,
                                    amount,
                                    destination,
                                    self.credit_card_processing_service,
                                    self.fraud_processing_service,
                                    self.notification_service)

        payment.pay()

        return payment.status
