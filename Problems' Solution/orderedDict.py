from collections import OrderedDict as orD

N, od = int(input()), orD()

for i in range(N):
    name, price = input().rsplit(' ', 1)

    if name in od:
        od[name] += int(price)

    else:
        od[name] = int(price)

for i in od:
    print(i, od[i])
