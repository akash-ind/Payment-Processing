from notification_service.NotificationService import NotificationService


class FraudProcessingService:

    def __init__(self, notification_service):
        self.notification_service: NotificationService = notification_service

    def is_fraud_transaction(self, payment):
        # todo : Check Fraud
        is_fraud = False
        if is_fraud:
            self.notification_service.notify(payment)
        return is_fraud
