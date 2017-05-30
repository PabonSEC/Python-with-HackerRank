import math

AB = int(input())

BC = int(input())

angle = int(round(math.degrees(math.atan(float(AB) / float(BC))), 0))

print('%d' % angle + '\xb0')
