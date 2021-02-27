"""
2.  Write a class called Product. The class should have fields called name, amount, and price,
    holding the product’s name, the number of items of that product in stock, and the regular
    price of the product. There should be a method get_price that receives the number of
    items to be bought and returns a the cost of buying that many items, where the regular price
    is charged for orders of less than 10 items, a 10% discount is applied for orders of between
    10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should
    also be a method called make_purchase that receives the number of items to be bought and
    decreases amount by that much.

"""


class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, n):
        if (n <= self.amount):
            if (n < 10):
                value = self.price * n
            elif (n >= 10 and n < 100):
                discount = self.price * n * 0.1
                value = self.price * n - discount
            elif (n >= 100):
                discount = self.price * n * 0.2
                value = self.price * n - discount
            self.make_purchase(n)
            return value
        else:
            return 'This number of items is not found'

    def make_purchase(self, n):
        self.amount = self.amount - n


# p = Product('GR3 2017', 10000, 100)
# print(p.get_price(10))
# print(p.amount)
