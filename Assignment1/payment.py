from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def get_details(self):
        pass
    @abstractmethod
    def pay(self, amount):
        pass
class RazorpayCardPayment(PaymentMethod):
    def __init__(self, card_number=None, **kwargs):
        self.card_number = card_number
    def get_details(self):
        return f"razorpay card: {self.card_number}"
    def pay(self, amount):
        return True
class RazorpayUPIPayment(PaymentMethod):
    def __init__(self, upi_id=None, **kwargs):
        self.upi_id = upi_id
    def get_details(self):
        return f"razorpay upi: {self.upi_id}"
    def pay(self, amount):
        return True
class StripeCardPayment(PaymentMethod):
    def __init__(self, card_number=None, **kwargs):
        self.card_number = card_number
    def get_details(self):
        return f"stripe card: {self.card_number}"
    def pay(self, amount):
        return True
class StripeUPIPayment(PaymentMethod):
    def __init__(self, upi_id=None, **kwargs):
        self.upi_id = upi_id
    def get_details(self):
        return f"stripe upi: {self.upi_id}"
    def pay(self, amount):
        return True
