# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

def check_rhyme(poem_list):
    first_phrase_syll_count = 0
    for i in range(len(poem_list[0])):
        if poem_list[0][i] == "а":
            first_phrase_syll_count += 1

    def check_syll(phrase):
        syll_phrase_count = 0
        for i in range(len(phrase)):
            if phrase[i] == "а":
                syll_phrase_count += 1

        if syll_phrase_count != first_phrase_syll_count:
            return False
            
        return True
    return check_syll

        

poem = input("Input poem: ")

poem_li = poem.split()

check_phrase = check_rhyme(poem_li)

for i in range(1, len(poem_li)):
    if not check_phrase(poem_li[i]):
        print("Пам-парам")
        break
    if i == len(poem_li) - 1:
        print("Парам пам-пам")

