# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

def init_coins(num):
    coins = []
    obverse = 0
    reverse = 0
    min_flip = 0

    for i in range(num):
        rnd = randint(0, 1)

        if rnd == 0:
            obverse += 1
        else:
            reverse += 1
        coins.append(rnd)

    if obverse >= reverse:
        min_flip = reverse
    else:
        min_flip = obverse

    return coins, min_flip

num_coins = int(input("Input num coins: "))

desk = init_coins(num_coins)
print(f"Монеты:\n {desk[0]}\nМинимальное количество переворотов: {desk[1]}")