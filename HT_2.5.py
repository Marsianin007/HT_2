# 5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
#   роботи захардкодити свій.
#                Приклад словника (не використовувати):
#                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
#                Очікуваний результат:
#                {'a': 1, 'b': 3, 'd': 5}

example_dict = {'Vlad' : 12, 'Artem' : 26, "Andrey" : 45, "Misha" : 12, 'Kostya' : 44, 'Lesha' : 68, 'Anna' : 44}

result_dict = {}
for key, value in example_dict.items():
    if value not in result_dict.values():
        result_dict[key] = value
print (result_dict)





