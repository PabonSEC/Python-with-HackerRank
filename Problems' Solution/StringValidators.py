if __name__ == '__main__':

    s = str(input())

    ln = len(s)

    alpha = False

    for i in range(ln):
        if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
            alpha = True
            break

    digit = False

    for i in range(ln):
        if s[i] >= '0' and s[i] <= '9':
            digit = True
            break

    if alpha == True or digit == True:
        print(True)
    else:
        print(False)


    if alpha == True:
        print(True)
    else:
        print(False)


    if digit == True:
        print(True)
    else:
        print(False)

    lower = False

    for i in range(ln):
        if s[i] >= 'a' and s[i] <= 'z':
            lower = True
            break

    if lower == True:
        print(True)
    else:
        print(False)

    upper = False

    for i in range(ln):
        if s[i] >= 'A' and s[i] <= 'Z':
            upper = True
            break

    if upper == True:
        print(True)
    else:
        print(False)
