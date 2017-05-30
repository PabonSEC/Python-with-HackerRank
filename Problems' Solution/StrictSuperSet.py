A = set(map(int, input().split()))

check = True

for i in range(int(input())):

    B = set(map(int, input().split()))

    if not A.issuperset(B):
        check = False

print(check)
