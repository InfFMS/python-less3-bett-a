#с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено положительных
# и сколько отрицательных чисел.

positive = 0
negative = 0
a = int(input())
while a:
    if a > 0:
        positive += 1
    elif a < 0:
        negative += 1
    a = int(input())

print(f'Положительных чисел: {positive}')
print(f'Отрицательных чисел: {negative}')
