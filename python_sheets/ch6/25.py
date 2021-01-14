
usr_input = '3x+4y'  # input('Enter your expression: ')
input_split = usr_input.split('+')
concat = []
expression = ''

for i in input_split:
    split_2 = list(i)
    concat.append(split_2[0] + '*' + split_2[1])

print(concat)

for i in range(len(concat)):
    expression += concat[i]
    if (i + 1 != len(concat)):
        expression += '+'

print(expression)
