def print_formatted(number):
    wid = len(str(bin(number))) - 2

    for num in range(1, number + 1):
        decimal = int(num)

        octal = oct(num)

        hexadecimal = hex(num)

        binary = bin(num)

        print(str(decimal).rjust(wid), octal[2:].rjust(wid), hexadecimal[2:].swapcase().rjust(wid),
              binary[2:].rjust(wid))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
