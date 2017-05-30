K = int(input())

li = list(map(int, input().split()))

st = set(li)

for i in st:
    li.remove(i)
    if i not in li:
        print(i)
        break
