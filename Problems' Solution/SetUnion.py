n = int(input())

st = set(map(int, input().split()))

n1 = int(input())

st1 = set(map(int, input().split()))

print(len(st.union(st1)))