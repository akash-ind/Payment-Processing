from models.payment import Payment
from const import Constant
from process.mobile_payment_processing_service import MobilePaymentProcessingService
from fraud_processing_service.fraud_processing_service import FraudProcessingService
from notification_service.NotificationService import NotificationService


class MobilePayment(Payment):
    payment_type = Constant.mobile_payment

    def __init__(self, mobile_details, currency, amount, destination, mobile_payment_processing_service,
                 fraud_processing_service, notification_service):
        self.mobile_details = mobile_details
        self.destination = destination
        self.status = Constant.in_process
        self.mobile_payment_processing_service: MobilePaymentProcessingService = mobile_payment_processing_service
        self.fraud_processing_service: FraudProcessingService = fraud_processing_service
        self.notification_service: NotificationService = notification_service
        super().__init__(self.payment_type, currency, amount)

    def pay(self):  # Can abstract it in super class but as these methods won't be very simple hence duplicating
        status, response = self.mobile_payment_processing_service.process(self)

        self.add_resulting_response(response)
        if status == Constant.successful:
            if self.fraud_processing_service.is_fraud_transaction(self):
                self.status = Constant.fraud
            else:
                self.status = Constant.successful
        elif status == Constant.failed:
            self.status = Constant.failed
            self.notification_service.notify(self)
