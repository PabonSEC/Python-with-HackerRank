N, M = map(int, input().split())

for i in range(1, N, 2):
    print((".|." * i).center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N - 2, 0, -2):
    print((".|." * i).center(M, "-"))

'''
N, M = map(int, input().split())

s = '.|.'

wlcm = 'WELCOME'

upper = int(N / 2)

lower = upper

koyta = 1

koyta_hypen = int(M / 2)-1

koyta_str = 1

for i in range(upper):
    for j in range(koyta_hypen):
        print('-', end='')

    for j in range(koyta_str):
        print(s, end='')

    for j in range(koyta_hypen):
        print('-', end='')

    koyta_str += 2

    koyta_hypen = M - (koyta_str * 3)

    koyta_hypen = int(koyta_hypen / 2)

    print()

print(wlcm.center(M, '-'))

for i in range(lower):

    koyta_str -= 2

    koyta_hypen = M - (koyta_str * 3)

    koyta_hypen = int(koyta_hypen / 2)

    for j in range(koyta_hypen):
        print('-', end='')

    for j in range(koyta_str):
        print(s, end='')

    for j in range(koyta_hypen):
        print('-', end='')

    print()
'''
