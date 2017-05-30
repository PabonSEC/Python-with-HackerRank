num = int(input())

st = set(map(int, input().split()))

num = int(input())

st1 = set(map(int, input().split()))

ans_set = st.difference(st1).union(st1.difference(st))

li = list(ans_set)

li.sort()

for i in li:
    print(i)
