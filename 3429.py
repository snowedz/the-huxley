qt = int(input())
nomes = []
ab1 = []
ab2 = []
media = []
situa = []
for qt in range(0, qt):
    nome = input()
    nomes = nomes + [nome]
    n1 = float(input())
    ab1 = ab1 + [n1]
    n2 = float(input())
    ab2 = ab2 + [n2]
    media = media + [((n1+n2)/2)]
for qt in range(0, qt+1):
    if media[qt] >= 7:
        sit = 'AP'
    else:
        sit = 'RP'
    situa = situa + [sit]
for qt in range(qt+1):
    print('Nome: ', nomes[qt])
    print('AB1:', '{:.2f}'.format(ab1[qt]))
    print('AB2:', '{:.2f}'.format(ab2[qt]))
    print('Media:', '{:.2f}'.format(media[qt]))
    print('Situacao: ', situa[qt])
