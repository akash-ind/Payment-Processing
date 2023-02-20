import uuid


class MobileDetails:

    def __init__(self, number, provider):
        self.id = uuid.uuid4()
        self.number = number
        self.provider = provider