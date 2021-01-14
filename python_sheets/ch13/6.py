'''
6. Write a function called binom that takes two integers n and k and returns
    the binomial coefficient. The definition is n!/(k!(n-k)!)

'''

import math

def binom(n, k):

    binomial_coefficient = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

    return binomial_coefficient
