dados1 = input()
x1, y1, z1 = dados1.split()
dados2 = input()
x2, y2, z2 = dados2.split()
x1 = float(x1)
y1 = float(y1)
z1 = float(z1)
x2 = float(x2)
y2 = float(y2)
z2 = float(z2)
Dpq = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
print('{:.2f}'.format(Dpq))