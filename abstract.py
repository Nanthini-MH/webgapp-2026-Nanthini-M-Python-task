from abc import ABC,abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def charge(self,amount,currency):
        self.amount=amount
        self.currency=currency
    @abstractmethod
    def refund(self,t_id,amount):
        self.t_id=t_id
        self.amount=amount
    def display(self,t_id,amount,currency):
        return f'Transaction id:{t_id}\nAmount:{amount}\nCurrency:{currency}'

class Razorpay(PaymentGateway):
    def charge(self,amount,currency):
        super().charge(amount,currency)
    def refund(self,t_id,amount):
        super().refund(t_id,amount)
    def display(self,t_id,amount,currency):
        print(PaymentGateway.display(self,t_id,amount,currency))

obj=Razorpay()
obj.charge(1000,'rupees')
obj.refund('acc01',1000)
obj.display('acc01',1400,'rupees')


