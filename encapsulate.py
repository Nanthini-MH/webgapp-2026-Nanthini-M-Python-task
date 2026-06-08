class Bank:
    def __init__ (self,name,accid,balance):
        self.name=name
        self._accid=accid
        self.__balance=balance
    def withdraw(self,amount):
        if amount<0:
            return "Balance should be greater than 0"
        if amount>self.__balance:
            return "Insufficient balance"
        self.__balance=self.__balance-amount
        return f'Balance of the Account id -{self._accid} is :{self.__balance}'
    def deposit(self,amount):
        if amount<0:
            return "Amount should be greater than zero"
        self.__balance=self.__balance+amount
        return f'Balance of the Account id -{self._accid} is :{self.__balance}'
    def display(self):
        print("Name :",self.name)
        print("Account id:",self._accid)
        print("Balance :",self.__balance)

b=Bank("Tom","acc01",2000)
print(b.withdraw(1000))
print(b.deposit(500))
b.display()