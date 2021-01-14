'''
2.
    (a) Write a function called add_excitement that takes a list of strings and adds an excla-
        mation point (!) to the end of each string in the list. The program should modify the
        original list and not return anything.

    (b) Write the same function except that it should not modify the original list and should
        instead return a new list.

'''

#(a)


def add_excitement(s):
    for i in range(len(s)):
        s[i] = s[i] + '!'


add_excitement(['a', 'v', 'c', 'q'])

#(b)


def add_excitement2(s):
    new_s = []
    for i in range(len(s)):
        new_s.append(s[i] + '!')

    print('s --> ', s)
    print('new_s --> ', new_s)
    return new_s


add_excitement2(['a', 'v', 'c', 'q'])
