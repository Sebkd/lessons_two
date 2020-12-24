# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
# слово с новой строки. Строки необходимо пронумеровать. Если в слово длинное, выводить
# только первые 10 букв в слове.
my_list = list((input('Введите несколько слов разделенных пробелом\n')).split())
for my_index, my_element in enumerate(my_list, 1):
    print(my_index, my_element if len(my_element)<10 else my_element[:10])
print('end program')