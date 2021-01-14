'''
8.  Write a function called number_of_factors that takes an integer and returns how many
    factors the number has.

'''


def number_of_factors(num: int):

    factors_counter = 0

    for i in range(1, num + 1):

        if(num % i == 0):

            factors_counter += 1

    return factors_counter


# print(number_of_factors(48))
