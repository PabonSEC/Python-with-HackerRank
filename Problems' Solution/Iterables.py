from itertools import combinations

num = int(input())

l = input().split()

n = int(input())

li = list(combinations(l, n))

cnt = 0

for i in li:
    if 'a' in i:
        cnt += 1

print(cnt / len(li))
