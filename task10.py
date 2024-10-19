# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".


def check_prostoe(x):
    q = x // 2
    d = [1, x]
    for i in range(2, q + 1):
        if x % i == 0:
            d.append(i)
    if len(d) == 2 and x != 1:
        return True

n = int(input())
maxx = 0
minn = 0
for _ in range(n):
    x = int(input())
    if check_prostoe(x):
        if minn == 0:
            minn = x
        if maxx < x:
            maxx = x
        if minn > x:
            minn = x

if maxx == 0:
    print("нет")
else:
    print(f'Минимальное: {minn}')
    print(f'Максимальное: {maxx}')
