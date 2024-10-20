# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, среднее арифметическое тех введённых чисел,
# которые являются степенями числа 2.
# Вывести "нет", если таких чисел нет.

def is_power_two(x):
    while x != 1:
        if x % 2 != 0:
            break
        x //= 2

    if x == 1:
        return True
    else:
        return False

i = 0
count = 0
a = int(input())
while a:
    if is_power_two(a):
        i += a
        count += 1
    a = int(input())

if count == 0:
    print("нет")
else:
    print(i / count)


