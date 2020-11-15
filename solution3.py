import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = (b * b) - (4 * a * c)

if d > 0:
    x = (-b + (d ** 0.5)) / (2 * a)
    print(int(x))
    x = (-b - (d ** 0.5)) / (2 * a)
    print(int(x))
elif d == 0:
    x = -b / (a * 2)
    print(int(x))
elif d < 0:
    print('Решения нет')
