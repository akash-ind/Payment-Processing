from models.credit_card import CreditCard


class CreditCardService:

    def __init__(self):
        self.credit_cards = dict()

    def add_credit_card(self, credit_card_no, expiry):
        credit_card = CreditCard(credit_card_no, expiry)
        self.credit_cards[credit_card.id] = credit_card
        return credit_card

    def get_credit_card(self, id):
        return self.credit_cards.get(id)

    def set_cvv(self, credit_card, cvv):
        credit_card: CreditCard
        credit_card.set_cvv(cvv)
