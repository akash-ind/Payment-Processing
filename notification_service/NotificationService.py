class NotificationService:

    # Todo: It is Async
    def notify(self, payment):
        user = payment.get_user() # Assuming we have users
        user.notify()

