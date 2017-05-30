def countSubstr(string, substr):
    res = 0

    lnstr = len(string)

    ln = len(substr)

    for i in range(lnstr):

        count = 0

        k = i

        for j in range(ln):

            if string[k] == substr[j]:
                count += 1

                if k + 1 < lnstr:
                    k += 1

            else:
                break

        if count == ln:
            res += 1

    return res


if __name__ == '__main__':
    string = str(input())
    substr = str(input())

    cnt = countSubstr(string, substr)

    print(cnt)
