# Реализовать структуру « Рейтинг », представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
# в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3 , 2.
# Пользователь ввел число 8. Результат: 8 , 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1 .
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3,
# 3, 2].
my_list = [90, 2, 45, 3, 67, 900, 34, 2, 1, 0]
my_list.sort()
my_list.reverse()
while True:

    print('Для окончания формирования списка введите 999 ')
    print(my_list)
    try:
        user_answer = int(input('Введите натуральное число для списка\n'))
        if (user_answer == 999):
            break
    except ValueError:
            print('Вы ввели не то что просили, попробуйте еще')
            continue
    if int(my_list.count(user_answer)) == 0:
        for counter in range(len(my_list)):
            if user_answer > my_list[counter]:
                my_list.insert(counter, user_answer)
                break
    else:
        my_list.insert(my_list.index(user_answer) + int(my_list.count(user_answer)), user_answer)
print('end program')
