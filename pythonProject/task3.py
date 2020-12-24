# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
while True:
    try:
        user_answer = int(input('Введите месяц в числовом выражении от 1 до 12\n'))
    except ValueError:
        print('Вы ввели не то что просили, попробуйте еще')
        continue
    if (user_answer > 12 or user_answer <= 0):
        print('Вы ввели не то что просили, попробуйте еще')
        continue
    else:
        break
user_answer -= 1
print('Решение через списки')
my_list_month = ['январь',
                 'февраль',
                 'март',
                 'апрель',
                 'май',
                 'июнь',
                 'июль',
                 'август',
                 'сентябрь',
                 'октябрь',
                 'ноябрь',
                 'декабрь'
                 ]
my_list_weather = ['Зима', 'Весна', 'Лето', 'Осень']
print(f'Выбранный месяц {my_list_month[user_answer]}')
if (user_answer >= 2 and user_answer <= 4):
    print(f'Время года {my_list_weather[1]}')
elif (user_answer >= 5 and user_answer <= 7):
    print(f'Время года {my_list_weather[2]}')
elif (user_answer >= 8 and user_answer <= 10):
    print(f'Время года {my_list_weather[3]}')
else:
    print(f'Время года {my_list_weather[0]}')
print('\nРешение через словарь')
user_answer += 1
my_dict_months = { 1:['зима', 'январь'],
                  2:['зима','февраль'],
                  3:['весна','март'],
                  4:['весна', 'апрель'],
                  5:['весна', 'май'],
                  6:['лето','июнь'],
                  7:['лето','июль'],
                  8:['лето','август'],
                  9:['осень','сентябрь'],
                  10:['осень','октябрь'],
                  11:['осень','ноябрь'],
                  12:['зима','декабрь'],
                  }
print(f'Выбранное время года {my_dict_months[user_answer][0]}, а месяц {my_dict_months[user_answer][1]}')
print('\nend program')