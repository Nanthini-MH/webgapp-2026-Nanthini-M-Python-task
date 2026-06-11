class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def show(self):
        print("Product name:",self.name)
        print("Product Price:",self.price)

class Discount:
    def discount_calc(self,price,dis_percent):
        discount=price*(dis_percent/100)
        final_amt=price-discount
        return final_amt
    
class Ecommerce(Product,Discount):
    def __init__(self,name,price,dis_percent):
        Product.__init__(self,name,price)
        self.dis_percent=dis_percent
    def display(self):
        self.show()
        print("Final price:",self.discount_calc(self.price,self.dis_percent))

e=Ecommerce("Laptop",2000,10)
e.display()
