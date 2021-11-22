# 3. Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
#        Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
#        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

simple_list = [(), (), ('',), ('a', 'g'), {}, ('a', 'o', 'c'), ('d'), '', [], [567], (), ("';",)]
result_list = []
for i in simple_list:
    if (len (i) != 0):
        result_list.append(i)
print(result_list)