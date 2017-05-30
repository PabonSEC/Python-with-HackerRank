def capitalize(string):
    ln = len(string)

    ans = string[0].upper()

    for i in range(1, ln):
        if string[i - 1] == ' ':
            ans += string[i].upper()
        else:
            ans += string[i]

    return ans


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)