n = int(input())
a = int(1)
den = int(1)
S = a/(den**3)
for n in range(1, n):
    den = den + 2
    if n % 2 == 0:
        S = S + (a/(den**3))
    else:
        S = S - (a/(den**3))
pi = ((S*32))**(1/3)
print('{:.5f}'.format(pi))
