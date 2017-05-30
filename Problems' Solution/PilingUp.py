from collections import deque

test = int(input())

for i in range(test):
    _ = int(input())

    DQ = deque(map(int, input().split()))

    mx = max(DQ)

    for j in range(len(DQ)):

        if DQ[-1] >= DQ[0] and mx >= DQ[-1]:
            mx = DQ[-1]
            DQ.pop()

        elif DQ[0] >= DQ[-1] and mx >= DQ[0]:
            mx = DQ[0]
            DQ.popleft()
        else:
            break

    if len(DQ) == 0:
        print('Yes')
    else:
        print('No')