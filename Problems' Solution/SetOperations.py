num = int(input())

st = set(map(int, input().split()))

n = int(input())

for i in range(n):

    s = input().split()

    if s[0] == "pop":
        st.pop()

    elif s[0] == "remove":
        st.remove(int(s[1]))

    elif s[0] == "discard":
        st.discard(int(s[1]))

print(sum(st))
