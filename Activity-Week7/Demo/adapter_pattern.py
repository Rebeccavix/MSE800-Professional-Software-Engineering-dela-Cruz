from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, money):
        pass

class ApplePay(PaymentMethod):

    def pay(self, money):
        print(f"Applepay: {money} dollars.")

class GooglePay(PaymentMethod):

    def pay(self, money):
        print(f"Googlepay: {money} dollars.")


class VisaPay:
    
    def cost(self, money):
        print(f"visapay: {money} dollars.")


class VisaAdapter(PaymentMethod, VisaPay):
    
    def pay(self, money):
        self.cost(money)


class MasterPay:

    def cost(self, money):
        print(f"masterpay: {money} dollars.")


class Adapter(PaymentMethod):

    def __init__(self, adaptee=None):
        self.adaptee = adaptee

    def pay(self, money):
        self.adaptee.cost(money)


# client
applepay = ApplePay()
applepay.pay(20)

googlepay = GooglePay()
googlepay.pay(30)

visapay = VisaPay()
visapay = Adapter(visapay)

masterpay = MasterPay()
masterpay = Adapter(masterpay)

visapay.pay(40)
masterpay.pay(50)

