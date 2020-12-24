# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input() .
user_list = []
while True:
    print('Для окончания формирования списка введите "Нет" ')
    user_list.append(input('Введите очередной элемент списка \n'))
    if ('нет' in user_list):
        user_list.pop()
        if (len(user_list) < 2):
            print('Нужно больше элементов')
            continue
        else:
            break
    else:
        print(user_list)
        continue
print(user_list)
for count_list in range(0, len(user_list) if (len(user_list) % 2 == 0) else len(user_list)-1, 2):
    user_list[count_list], user_list [count_list+1] = user_list [count_list+1], user_list [count_list]
print(user_list)
print('end program')