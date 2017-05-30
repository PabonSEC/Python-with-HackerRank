from itertools import product

li = list(map(int, input().split()))

li1 = list(map(int, input().split()))

print(*product(li, li1))