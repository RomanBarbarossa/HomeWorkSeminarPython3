# ---------Task 1

# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N].
# Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1234 5
# 3 -> 1

#                    решение 1   - пользователь не вводит значения  

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

#                    решение 2   - пользователь сам вводит значения через .split

# num = int(input('Введите размер списка: '))
# listnumber = list(map(int,(input('Введите числа: ').split())))
# if len(listnumber) > num:
#     print(f'Вы ввели чисел больше чем нужно на {len(listnumber) - num}')
# elif len(listnumber) < num:
#     print(f'Вы ввели чисел меньше чем нужно на {num - len(listnumber)}')
# x = int(input('Введите искомое число: '))
# counter = 0
# for i in listnumber:
#     if i == x:
#         counter += 1
# if counter == 0:
#     print('Число не найдено')
# else:
#     print(f'Ваше число попалось в списке {counter} раз(a)')

 
# ----------Task 2

# Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих строках записаны N 
# целых чисел Ai. Последняя строка содержит число X


# n = int(input("введите количество элементов: "))
# massive = list(map(int,(input('Введите числа: ').split())))
# x = int(input('Введите искомое число: '))
# new = [0]*n
# i = 0

# minIndex = 0
# while i < len(massive):
#     new[i] = abs(x - massive[i])
#     minValue = new[0]
#     if new[i] < minValue:
#         minValue = new[i]
#         minIndex = i
#     i += 1
# print(f'Самое ближайшее число {massive[minIndex]}')
 
 #  НЕ ПОНИМАЮ ПОЧЕМУ НЕ РАБОТАЕТ ,ЧИСЛО ВЫДАЕТ ТО ВЕРНОЕ ТО НЕТ


#------------------- Task 3

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# rusdict = {1 : "АВЕИНОРСТ", 2 : "ДКЛМПУ" , 3 : "БГЁЬЯ" , 4: "ЙЫ",5: "ЖЗХЦЧ", 8 : "ШЭЮ",10:"ФЩЪ" }
# engdict = {1 : "A,E,I,O,U,L,N,S,T,R", 2 : "D,G" , 3 : "B,C,M,P" , 4: "F,H,V,W,Y",5: "K", 8 : "J,X",10:"Q,Z" }


rusengdict = {'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1,
          'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1,
          'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3,
          'Э': 8, 'Ю': 8, 'Я': 3,'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
          'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
          'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

word = input("Введите слово: ").upper()
sum = 0

#   РЕШЕНИЕ 1
# for letter in word:
#     for key, value in rusengdict.items():
#         if letter in key:
#             sum += value

#   РЕШЕНИЕ 2
for letter in word:
    if letter in rusengdict.keys():
        sum += rusengdict[letter]
print (sum)
