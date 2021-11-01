num_quest = int(input())
gabarito_prov = input()
gabarito_prov = list(gabarito_prov)
gabarito_alun = input()
gabarito_alun = list(gabarito_alun)
x = 0
for n in range(num_quest):
    if gabarito_prov[n] == gabarito_alun[n]:
        x += 1
print(x)
