# task1
# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = ['Зима', 'Лето', 12, True, 12.3]
print(my_list)
for index in my_list:
     print(f'у элемента {index} тип данных равен {type(index)}')
print('end program')