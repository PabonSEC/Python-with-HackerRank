from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'

for i in range(int(input())):
    a = dt.strptime(input(), fmt)
    b = dt.strptime(input(), fmt)
    print(int(abs(a - b).total_seconds()))
