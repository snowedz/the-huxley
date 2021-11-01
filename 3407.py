n1 = float(input())
if n1 == 1:
    n2 = input()
    a, b = n2.split()
    a = float(a)
    b = float(b)
    print('{:.2f}'.format(a+b))
elif n1 == 2:
    n2 = input()
    n2 = float(n2)
    print('{:.2f}'.format(n2**0.5))
else:
    print('Opção inválida!')
