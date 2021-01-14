'''
Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
'''

import random

l = []

for i in range(100):

    s = random.randint(0, 1)
    l.append(s)

longest_run = 0
counter = 0

for i in range(len(l)):

    if (l[i] == 0):
        counter += 1

        if(longest_run < counter):
            longest_run = counter

    else:
        counter = 0

print(l)
print(longest_run)
