def common(a, b):
    count = [a[i] for i in range(5) if a[i] == b[i]]
    return len(count)


l = ['01265', '12171', '23257', '34548', '45970', '56236', '67324', '78084', '89872', '99414']
for i in range(10000, 100000):
    for x in l:
        if common(str(i), x) != 1:
            break
    else:
        print(i)
