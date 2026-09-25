from abc import ABC, abstractmethod
from payment import RazorpayCardPayment, RazorpayUPIPayment, StripeCardPayment, StripeUPIPayment
class FactoryPaymentMethod(ABC):
    factory = {}
    @classmethod
    @abstractmethod
    def get_payment_object(cls, method_type, **kwargs):
        payment_class = cls.factory.get(method_type)
        if payment_class:
            return payment_class(**kwargs)
        return None
    @classmethod
    def register_payment_method(cls, method_type, payment_class):
        cls.factory[method_type] = payment_class
class RazorpayFactory(FactoryPaymentMethod):
    factory = {"card": RazorpayCardPayment, "upi": RazorpayUPIPayment}
class StripeFactory(FactoryPaymentMethod):
    factory = {"card": StripeCardPayment, "upi": StripeUPIPayment}
