dados = input()
A, B, C = dados.split()
A = float(A)
B = float(B)
C = float(C)
Disc = B**2 - 4 * A * C
X1 = (-B - (Disc**0.5))/(2*A)
X2 = (-B + (Disc**0.5))/(2*A)
print('{:.2f}'.format(X1), '{:.2f}' .format(X2))
