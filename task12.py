# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

def search_nums(s, p):
    num1 = 0
    num2 = 0

    has_find = False

    for i in range(s):
        if not has_find:
            for j in range(p):
                if s == j + i and p == j * i:
                    num1 = i
                    num2 = j

                    has_find = True
                    break
                
    print(num1, num2)

sum = int(input("Input sum: "))
product = int(input("Input product: "))

search_nums(sum, product)
