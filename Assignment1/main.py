from payment import PaymentMethod, RazorpayCardPayment, RazorpayUPIPayment, StripeCardPayment, StripeUPIPayment
from factory import FactoryPaymentMethod, RazorpayFactory, StripeFactory
from aggregator import Aggregator, RazorpayAggregator, StripeAggregator, AggregatorFactory
def main():
    while True:
        aggregator_choice = input("enter aggregator (stripe/razorpay): ").strip().lower()
        aggregator = AggregatorFactory.get_aggregator_object(aggregator_choice)
        if aggregator:
            break
        print("invalid choice")
    while True:
        method_choice = input("enter payment method (card/upi): ").strip().lower()
        if method_choice in ["card", "upi"]:
            break
        print("invalid choice")
    details = {}
    if method_choice == "card":
        details["card_number"] = input("enter card number: ").strip()
    elif method_choice == "upi":
        details["upi_id"] = input("enter upi id: ").strip()
    while True:
        try:
            amount = float(input("enter amount: ").strip())
            if amount > 0:
                break
            print("invalid choice")
        except ValueError:
            print("invalid choice")
    result = aggregator.call_get_payment_object(method_choice, amount, **details)
    if result:
        print("payment successful")
    else:
        print("payment failed")
if __name__ == "__main__":
    main()
