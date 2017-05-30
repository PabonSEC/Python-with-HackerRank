import itertools as it

s, num = input().split()

num = int(num)

s = sorted(s)

li = list(it.combinations_with_replacement(s, num))

for i in li:
    print("".join(i))