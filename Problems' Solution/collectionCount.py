from collections import Counter

_ = int(input())

coll = Counter(map(int, input().split()))

tot = 0

for _ in range(int(input())):

    size, price = map(int, input().split())

    if coll[size]:
        coll[size] -= 1
        tot += price

print(tot)
