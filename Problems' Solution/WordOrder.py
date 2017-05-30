from collections import OrderedDict as orD

N, od = int(input()), orD()

for i in range(N):
    name = input()

    if name in od:
        od[name] += 1
    else:
        od[name] = 1

print(len(od))

[print(od[i], end=' ') for i in od]
