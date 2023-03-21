import random

count = int(input('Введите количество монеток: '))
side_of_coin = [random.randint(0, 1) for i in range(count)]
print(side_of_coin)
count_0 = 0
count_1 = 0
for i in range(count):
    if side_of_coin[i] == 0:
        count_0 += 1
    else:
        count_1 += 1
if count_0 < count_1:
    print(f'Нужно перевернуть минимум {count_0} монет')
elif count_1 < count_0:
    print(f'Нужно перевернуть минимум {count_1} монет')
else:  # если равны
    print(f'Нужно перевернуть минимум {count_1} монет')
