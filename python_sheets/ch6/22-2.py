import math


encrypted_s = 'msaeesg'  # input("Enter The String to decrypt:")

# j: counter for odd characters

j = math.ceil(len(encrypted_s) / 2)

s = ''  # s: String after decryption

if(len(encrypted_s) % 2 == 0):

    for i in range(math.ceil(len(encrypted_s) / 2)):

        s += encrypted_s[i] + encrypted_s[j]
        j += 1
        if (j == (len(encrypted_s))):
            break

else:

    for i in range(math.ceil(len(encrypted_s) / 2)):

        s += encrypted_s[i] + encrypted_s[j]
        j += 1
        if (j == (len(encrypted_s))):
            s += encrypted_s[i + 1]
            break

print(s)
