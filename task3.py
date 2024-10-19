# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено простых натуральных чисел
# (которые делятся только сами на себя и на 1), и сколько составных.

def check_prostoe(x):
    q = x // 2
    d = [1, x]
    for i in range(2, q + 1):
        if x % i == 0:
            d.append(i)
    if len(d) == 2:
        return True

count = 0
other = 0
one = 0
a = int(input())
while a:
    if a == 1:
        one += 1
    elif check_prostoe(a):
        count += 1
    else:
        other += 1
    a = int(input())

print(f'Простых: {count}')
print(f'Составных: {other}')
print(f'Единиц:{one}')

