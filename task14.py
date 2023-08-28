# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

def display_pow(n):
    for i in range(n + 1):
        print(pow(2, i))

num = int(input("Input N: "))

display_pow(num)