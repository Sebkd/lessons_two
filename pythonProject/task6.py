# Реализовать структуру данных « Товары ». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
my_structure = []
counter = 1
while True:
    print('Для окончания формирования списка введите "нет" ')
    in_data = list(input('Введите через пробел название товара, его цену, количество и единицу измерения\n').split())
    if ('нет' in in_data):
        break
    in_data_tuple = (counter, {'название': str(in_data[0]),
                               'цена': float(in_data[1]),
                               'количество': int(in_data[2]),
                               'eд' : str(in_data[3])})
    my_structure.append(in_data_tuple)
    print('[\n {0} \n ]'.format(*my_structure), sep="\n")
print('[\n {0} \n ]'.format(*my_structure), sep="\n")