import itertools as it

s, num = input().split()

num = int(num)

s = sorted(s)

for i in range(1, num + 1):
    li = list(it.combinations(s, i))

    for j in li:
        print("".join(j))
