num = int(input())

li = list(map(float, input().split()))

st = set(li)

tot = sum(st)  # sum of set

n = len(st)

print(tot / n)
