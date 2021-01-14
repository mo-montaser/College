'''
Write a program that removes any repeated items from a list so that each item appears at most
once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0] .
'''

l = [1, 1, 2, 3, 4, 3, 0, 0, 1, 1, 2, 3, 4, 3, 0, 0]
uniqe_l = []

#*************************************************** this new
for i in l:
    if i not in uniqe_l:
        uniqe_l.append(i)
#****************************************************
print(uniqe_l)
