from models.mobile_payment import MobilePayment
from service.mobile_detail_service import MobileDetailService


class MobilePaymentService:

    def __init__(self, mobile_detail_service, notification_service, fraud_processing_service, mobile_payment_processing_service):
        self.mobile_payment_processing_service = mobile_payment_processing_service
        self.fraud_processing_service = fraud_processing_service
        self.notification_service = notification_service
        self.mobile_detail_service: MobileDetailService = mobile_detail_service



    def create_mobile_payment(self, id, currency, amount, destination):
        mobile_details = self.mobile_detail_service.get_mobile_details(id)

        mobile_payment = MobilePayment(mobile_details, currency, amount, destination,
                                       self.mobile_payment_processing_service,
                                       self.fraud_processing_service,
                                       self.notification_service)
        mobile_payment.pay()

        return mobile_payment.status

