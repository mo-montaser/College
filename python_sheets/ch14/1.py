"""
1.  Write a class called Investment with fields called principal and interest. The construc-
    tor should set the values of those fields. There should be a method called value_after that
    returns the value of the investment after n years. The formula for this is p(1 + i)n , where p is
    the principal, and i is the interest rate. It should also use the special method __str__ so that
    printing the object will result in something like below:

    Principal - $1000.00, Interest rate - 5.12%

"""


class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest

    def value_after(self, n):
        value = self.principal * (1 + self.interest)**n
        return value

    def __str__(self):
        return "Principal - $1000.00, Investment rate - 5.12%"


# I = Investment(10, 50)
# print(I)
# print(I.value_after(2))
