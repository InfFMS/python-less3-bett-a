# с клавиатуры вводится число N, а затем – N натуральных чисел.
# Определить минимальное и максимальное среди простых чисел
# (которые делятся на сами не себя и на 1).
# Если таких чисел не было, вывести "нет".


# когда_нибудь
'''
def check_prostoe(x):
    q = x // 2
    d = [1, x]
    for i in range(2, q + 1):
        if x % i == 0:
            d.append(i)
    if len(d) == 2:
        return x


n = int(input())
minn = int(input())
maxx = minn
a = 0
while check_prostoe(minn) is None and a < n:
    minn = int(input())
    a += 1
for _ in range(n - a):
    j = check_prostoe(int(input()))
    if j is None:
        continue
    else:
        if j <= minn:
            minn = j
        elif j >= maxx:
            maxx = j


print(f'Наибольшее: {maxx}, наименьшее: {minn}')
'''

# нужно сделать проверку на отсутствие подходящих чисел,
# а то оно вообще не реагирует на составные
