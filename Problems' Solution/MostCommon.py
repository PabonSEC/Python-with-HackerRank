s = sorted(input())

cnt = sorted(sorted(set(s)), key=s.count, reverse=True)

for i in range(3):
    print(cnt[i], s.count(cnt[i]))
