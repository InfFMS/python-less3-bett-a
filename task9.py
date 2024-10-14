# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".

n = int(input())
minn = int(input())
maxx = minn
for _ in range(n - 1):
    a = int(input())
    if 9 < a < 100 and a % 3 == 0:
        if a < minn:
            minn = a
        elif a > maxx:
            maxx = a


if not(9 < minn < 100 or minn % 3 == 0) and not(9 < maxx < 100 or maxx % 3 == 0):
    print('нет')

elif minn % 3 != 0 and maxx % 3 == 0:
    minn = maxx
    print(f'Минимальное: {minn}')
    print(f'Максимальное: {maxx}')
else:
    print(f'Минимальное: {minn}')
    print(f'Максимальное: {maxx}')

