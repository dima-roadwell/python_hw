# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progrssion(a, d, n):
    sp = []

    for i in range(1, n + 1):
        sp.append(a + (i - 1) * d)

    return sp

a = int(input("Input first el: "))
d = int(input("Input d: "))
num_items = int(input("Input num items: "))

print(arithmetic_progrssion(a, d, num_items))