n = input()
a, b, c = n.split()
a = int(a)
b = int(b)
c = int(c)
x = int(0)
print(a)
print(b)
for i in range(3, c+1):
    if i % 2 == 0:
        x = b - a
    else:
        x = b + a
    a = b
    b = x
    print(x)
