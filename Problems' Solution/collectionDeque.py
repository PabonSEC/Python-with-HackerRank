from collections import deque as DQ

N, d = int(input()), DQ()

for i in range(N):
    name = input().split()

    if name[0] == 'append':
        d.append(name[1])

    elif name[0] == 'appendleft':
        d.appendleft(name[1])

    elif name[0] == 'pop':
        d.pop()

    elif name[0] == 'popleft':
        d.popleft()

[print(i, end=' ') for i in d]
