def print_rangoli(size):
    ln = (size * 2 - 1) * 2 - 1

    import string

    letter = string.ascii_lowercase[0:size]

    for i in range(1, size + 1):
        cs = letter[-1:size - i:-1] + letter[size - i:]

        cs = "-".join(cs)

        print(cs.center(ln, '-'))

    for i in range(1, size):
        cs = letter[size - 1:i:-1] + letter[i:size]

        cs = "-".join(cs)

        print(cs.center(ln, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
