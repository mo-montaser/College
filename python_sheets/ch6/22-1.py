
s = 'message'  # input("Enter The String to encrypt:")
odd = ''
even = ''

for i in range(len(s)):

    if(i % 2 == 0):
        even += s[i]

    else:
        odd += s[i]

encrypted_s = even + odd

print(encrypted_s)
