from abc import ABC, abstractmethod
from factory import RazorpayFactory, StripeFactory
class Aggregator(ABC):
    def __init__(self, name, processing_fee, payment_factory):
        self.name = name
        self.processing_fee = processing_fee
        self.payment_factory = payment_factory
    @abstractmethod
    def call_get_payment_object(self, method_type, amount, **kwargs):
        pass
class RazorpayAggregator(Aggregator):
    def __init__(self):
        super().__init__("razorpay", 2.0, RazorpayFactory)
    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = self.payment_factory.get_payment_object(method_type, **kwargs)
        if payment:
            return payment.pay(amount)
        return False
class StripeAggregator(Aggregator):
    def __init__(self):
        super().__init__("stripe", 2.9, StripeFactory)
    def call_get_payment_object(self, method_type, amount, **kwargs):
        payment = self.payment_factory.get_payment_object(method_type, **kwargs)
        if payment:
            return payment.pay(amount)
        return False
class AggregatorFactory:
    factory = {"stripe": StripeAggregator, "razorpay": RazorpayAggregator}
    @classmethod
    def get_aggregator_object(cls, aggregator_name):
        aggregator_class = cls.factory.get(aggregator_name)
        if aggregator_class:
            return aggregator_class()
        return None
    @classmethod
    def register_aggregator(cls, aggregator_name, aggregator_class):
        cls.factory[aggregator_name] = aggregator_class
