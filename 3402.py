reta1 = input()
reta2 = input()
A, B = reta1.split()
C, D = reta2.split()
A = float(A)
B = float(B)
C = float(C)
D = float(D)
x = (D-B)/(A-C)
y = (x * C + D)
print('{:.2f}'.format(x), '{:.2f}'.format(y))