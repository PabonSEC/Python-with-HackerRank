from collections import defaultdict

n, m = map(int, input().split())

defDict = defaultdict(list)

for i in range(1, n + 1):
    defDict[input()].append(str(i))

for i in range(1, m + 1):
    check = input()

    print(' '.join(defDict[check]) or -1)
