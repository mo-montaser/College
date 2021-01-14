'''
3. Write a function called sum_digits that is given an integer num and returns the sum of the
digits of num.

'''

def sum_digits(num):

    num = list(str(num))
    sum = 0

    for i in range(len(num)):
        sum += int(num[i])

    return sum


# print(sum_digits(366))
