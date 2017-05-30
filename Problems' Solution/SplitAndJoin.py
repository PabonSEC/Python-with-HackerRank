def split_and_join(line):

    return '-'.join(line.split(' '))

if __name__ == '__main__':

    line = str(input())

    result = split_and_join(line)

    print(result)