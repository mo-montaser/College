'''
14. Write a function called is_sorted that is given a list and returns True if the list is sorted
    and False otherwise.
'''

def is_sorted(L: list):

    L_copy = L[:]
    L_copy.sort()

    if(L == L_copy):
        return True

    else:
        return False


# listA = [11, 23, 42, 51, 67]
# print(is_sorted(listA))
