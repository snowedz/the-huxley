n = int(input())
a = []
b = []
d = 0
x = 0
for n in range(0,n):
    elemento = float(input())
    a = a + [elemento]
a.sort()
print(a[0])
print(a[n])
for n in range(0,n+1):
    if a[n] % 2 == 0:
        b = b + [a[n]]
c = (len(b)/len(a)) * 100
n = len(a)
print('{:.2f}'.format(c))
for x in range(0,n):
    d = d + a[x]
d = d/n
print('{:.2f}'.format(d))
