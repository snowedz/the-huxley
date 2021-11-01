A = 12
B = 9
C = 8
dados = input()
x1, x2 = dados.split()
x1 = float(x1)
if x2 == ('A'):
    print('{:.2f}'.format(x1/A))
elif x2 == ('B'):
    print('{:.2f}'.format(x1/B))
elif x2 == ('C'):
    print('{:.2f}'.format(x1/C))
else:
    print('Tipo inválido!')
