n = int(input())

li = []

store_li = []

names = []

store = []

for i in range(n):
    name = input()
    marks = float(input())
    li.append(marks)
    store_li.append([name, marks])

li.sort()

for i in range(1, len(li)):
    if li[i] != li[i-1]:
        scnd_min = li[i]
        break

for i in range(len(store_li)):

    store = store_li[i]

    if store[1] == scnd_min:
        names.append(store[0])


names.sort()

for name in names:
    print(name)