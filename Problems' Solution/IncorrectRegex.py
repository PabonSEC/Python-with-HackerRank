import re

for _ in range(int(input())):

    check = input()

    try:
        re.compile(check)

    except re.error:
        print(False)
    else:
        print(True)
