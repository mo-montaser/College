'''
In calculus, the derivative of x 4 is 4x 3 . The derivative of x 5 is 5x 4 . The derivative of x 6 is
6x 5 . This pattern continues. Write a program that asks the user for input like x^3 or x^25
and prints the derivative. For example, if the user enters x^3 , the program should print out
3x^2
'''

usr_input = input('Enter the number:')

input_split = usr_input.split('^')

print(input_split)

num = int(input_split[1]) - 1

derivative = input_split[1] + input_split[0] + '^' + str(num)

print(derivative)
