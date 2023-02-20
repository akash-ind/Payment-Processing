from models.mobile_details import MobileDetails

class MobileDetailService:

    def __init__(self):
        self.mobile_details = dict()

    def add_mobile_details(self, mobile_no, provider):
        mobile_detail = MobileDetails(mobile_no, provider)
        self.mobile_details[mobile_detail.id] = mobile_detail
        return mobile_detail

    def get_mobile_details(self, id):
        # Todo: Null Checks
        return self.mobile_details.get(id)