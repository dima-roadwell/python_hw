# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def sorting_custom(sp1, sp2):
    sp3 = []

    if len(sp1) <= len(sp2):
        for i in range(len(sp1)):
            for j in range(len(sp2)):
                if sp1[i] == sp2[j]:
                    sp3.append(sp1[i])
    else:
        for i in range(len(sp2)):
            for j in range(len(sp1)):
                if sp2[i] == sp1[j]:
                    sp3.append(sp2[i])

    sp3 = set(sp3)

    order_by_asc(sp3)

    return sp3

def order_by_asc(sp):
    sp = list(sp)

    for i in range(len(sp)):
        for j in range(len(sp)):
            if sp[i] > sp[j]:
                tmp = sp[i]
                sp[i] = sp[j]
                sp[j] = tmp

n = int(input("Input n: "))
m = int(input("Input m: "))

sp1 = []
sp2 = []

for i in range(n):
    sp1.append(int(input("Input el for sp1: ")))

for i in range(m):
    sp2.append(int(input("Input el for sp2: ")))


print(sorting_custom(sp1, sp2))