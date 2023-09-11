# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

def create_list(list_len):
    sp = []

    for i in range(list_len):
        sp.append(random.randint(0, 100))

    return sp

def find_num_in_range(sp, sn, en):
    sp2 = []

    for i in range(len(sp)):
        if sp[i] >= sn and sp[i] <= en:
            sp2.append(sp[i])

    return sp2


li = create_list(5)
print(li)

start_num = int(input("Input start num: "))
end_num = int(input("Input end num: "))

print(find_num_in_range(li, start_num, end_num))