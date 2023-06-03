# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1234 5
# 3 -> 1

# import random
# n = int(input("Введите колл-во элементов в массиве: "))
# num_list = [0]*n
# for i in range (1,n):
#     num_list[i] = random.randint(1,10)
# print (num_list)
# x = int(input('Введите искомое число: '))
# count = 0
# for j in num_list:
#     if j == x:
#         count += 1
# print(f"ваше число попалось {count} раз(a)")

# решение 2 
num = int(input('Введите размер списка: '))
listnumber = list(map(int,(input('Введите числа: ').split())))
if len(listnumber) > num:
    print(f'Вы ввели чисел больше чем нужно на {len(listnumber) - num}')
elif len(listnumber) < num:
    print(f'Вы ввели чисел меньше чем нужно на {num - len(listnumber)}')
x = int(input('Введите искомое число: '))
counter = 0
for i in listnumber:
    if i == x:
        counter += 1
if counter == 0:
    print('Число не найдено')
else:
    print(f'Ваше число попалось в списке {counter} раз(a)')