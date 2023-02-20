from fraud_processing_service.fraud_processing_service import FraudProcessingService
from notification_service.NotificationService import NotificationService
from process.bank_transfer_processing_service import BankTransferProcessingService
from process.credit_card_processing_service import CreditCardProcessingService
from process.mobile_payment_processing_service import MobilePaymentProcessingService
from service.credit_card_service import CreditCardService
from service.bank_detail_service import BankDetailsService
from service.mobile_detail_service import MobileDetailService
from service.bank_transfer_service import BankTransferService
from service.mobile_payment_service import MobilePaymentService
from service.credit_card_payment_service import CreditCardPaymentService

from const import Constant


class Driver:

    def __init__(self):
        self.notification_service = NotificationService()
        self.fraud_processing_service = FraudProcessingService(self.notification_service)
        self.credit_card_processing_service = CreditCardProcessingService()
        self.bank_transfer_processing_service = BankTransferProcessingService()
        self.mobile_payment_processing_service = MobilePaymentProcessingService()
        self.credit_card_service = CreditCardService()
        self.bank_detail_service = BankDetailsService()
        self.mobile_detail_service = MobileDetailService()
        self.credit_card_payment_service = CreditCardPaymentService(self.credit_card_service,
                                                                    self.credit_card_processing_service,
                                                                    self.notification_service,
                                                                    self.fraud_processing_service)
        self.mobile_payment_service = MobilePaymentService(self.mobile_detail_service,
                                                           self.mobile_payment_processing_service,
                                                           self.notification_service,
                                                           self.fraud_processing_service)
        self.bank_transfer_service = BankTransferService(self.bank_detail_service,
                                                         self.bank_transfer_processing_service,
                                                         self.notification_service,
                                                         self.fraud_processing_service)

    def start(self):

        while True:
            type = input("Payment Type: ")

            amount = input("Amount: ")
            currency = input("Currency: ")

            destination = input("Destination: ")

            if type == Constant.credit_card_payment:
                card_no = input("Card Number: ")
                expiry = input("Expiry: ")
                cvv = input("CVV: ")

                credit_card = self.credit_card_service.add_credit_card(card_no, expiry)

                status = self.credit_card_payment_service.create_credit_card_payment(credit_card.id, currency, amount,
                                                                                     destination, cvv)
                print(status)

            if type == Constant.mobile_payment:
                mobile_no = input("Mobile No: ")
                provider = input("Provider: ")

                mobile_details = self.mobile_detail_service.add_mobile_details(mobile_no, provider)

                status = self.mobile_payment_service.create_mobile_payment(mobile_details.id, currency, amount,
                                                                           destination)

                print(status)

            if type == Constant.bank_transfer:
                account_no = input("Account no: ")
                bank_code = input("Bank Code: ")

                bank_details = self.bank_detail_service.add_bank_details(account_no, bank_code)

                status = self.bank_transfer_service.create_bank_transfer(bank_details.id, currency, amount, destination)

                print(status)

            if type == "exit":
                return


driver = Driver()

driver.start()
