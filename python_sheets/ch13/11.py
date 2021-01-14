'''
11. Write a function called matches that takes two strings as arguments and returns how many
    matches there are between the strings. A match is where the two strings have the same char-
    acter at the same index. For instance, 'python' and 'path' match in the first, third, and
    fourth characters, so the function should return 3.
'''

def matches(a: str, b: str):

    match_flag = 0
    a = list(a)
    b = list(b)

    if(len(a) < len(b)):

        for i in range(len(a)):
            if(a[i] == b[i]):
                match_flag += 1
    else:

        for i in range(len(b)):
            if(a[i] == b[i]):
                if(a[i] == b[i]):
                    match_flag += 1

    return match_flag


# print(matches('python', 'path'))
