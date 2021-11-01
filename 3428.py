dados = input()
o, x = dados.split()
o = int(o)
x = int(x)
a = []
dia = []
d = 0
for i in range(0, o):
    linha = []
    for i in range(0, o):
        elemento = int(input())
        linha.append(elemento)
    a.extend(linha)
for c in range(0, len(a), 4):
    d = a[c]
    if a[c] % x == 0:
        dia.append(d)
if dia == []:
    print('NMDX')
else:
    print(*dia)
