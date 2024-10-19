# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".

'''
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
'''


'''
n = int(input())
l = list()
for _ in range(n):
    x = int(input())
    if 9 < x < 100 and x % 3:
        l.append(x)

if len(l) == 0:
    print("нет")
else:
    print(f'Минимальное: {min(l)}')
    print(f'Максимальное :{max(l)}')
'''

n = int(input())
maxx = 0
minn = 100

for _ in range(n):
    x = int(input())
    if 9 < x < 100 and x % 3 == 0:
        if x > maxx:
            maxx = x
        if x < minn:
            minn = x

if minn == 100:
    print("нет")
else:
    print(f'Минимальное: {minn}')
    print(f'Максимальное: {maxx}')

