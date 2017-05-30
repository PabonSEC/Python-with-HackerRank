import itertools as it

s = input()

for i, k in it.groupby(s):
    ln = len(list(k))

    print(tuple((ln, int(i))), end=' ')
