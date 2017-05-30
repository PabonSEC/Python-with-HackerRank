from collections import namedtuple as NT

N = int(input())

details = NT('Student', input())

marks = []

for i in range(N):
    data = details(*input().split())
    marks.append(int(data.MARKS))

print('%.2f' % (sum(marks) / N))
