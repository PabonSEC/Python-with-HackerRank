num = int(input())

st = set(map(int, input().split()))

n = int(input())

for i in range(n):

    s = input().split()

    st1 = set(map(int, input().split()))

    if s[0] == "update":
        st.update(st1)

    elif s[0] == "difference_update":
        st.difference_update(st1)

    elif s[0] == "symmetric_difference_update":
        st.symmetric_difference_update(st1)

    elif s[0] == "intersection_update":
        st.intersection_update(st1)

print(sum(st))
