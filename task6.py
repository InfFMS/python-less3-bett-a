# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.

minn = int(input())
maxx = minn
b = int(input())
while b:
    if b < minn:
        minn = b
    elif b > maxx:
        maxx = b
    b = int(input())

print(f'Минимальное: {minn}')
print(f'Максимальное: {maxx}')