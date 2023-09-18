import json

def set_config(option, param, conf):
    stream = open("conf.ini", "w")

    for key, value in conf.items():
        if key == option and value != param:
            conf[key] = param

    for key, value in conf.items():        
        stream.writelines(f"{key}={value}")
    stream.close()

def get_config():
    conf = {}

    try:
        stream = open("conf.ini", "r")
    except:
        stream = open("conf.ini", "w")
    
    for line in stream:
        cur_line = line.split("=")
        conf[cur_line[0]] = cur_line[1]

    stream.close()
    return conf
    
def add_contact(pb, name):
    phone_nums = int(input('Сколько номеров вы хотите ввести: '))
    phone_number = []
    for i in range(phone_nums):
        phone_number.append(input("Введите номер телефона: "))

    contact_city = input("Город: ")
    contact_status = input("Статус: ")

    pb[name] = {"phones": phone_number, "city": contact_city, "status": contact_status}

    return pb

def import_phonebook(pb_name, mode):
    try:
        stream = open(f"{pb_name}.json", "r")
    except:
        print("Такой книги не существует!")
    
    pb = stream.read()
    stream.close()

    if mode != "init":
        set_config(option="DEFAULT_PHONEBOOK", param=pb_name, conf=config)

    return json.loads(pb)

def export_phonebook(pb, pb_name):
    pb = json.dumps(pb)

    stream = open(f"{pb_name}.json", "w", encoding="utf-8")
    stream.write(pb)
    stream.close()
        
    
def del_contact(pb, name):
    del pb[name]

def change_contact(pb, contact_name):
    def change_param(param):
        for k in pb.items():
            if k[0] == contact_name:
                pb[k[0]][param] = input("Введите значение: ")
                return pb
    return change_param


def get_phonebook(conf):
    param = "DEFAULT_PHONEBOOK"
    for item in conf.items():
        if item[0] == param:
            return import_phonebook(item[1], mode="init")

def display_phonebook(pb):
    try:
        for el in pb:
            if isinstance(pb, dict):
                print(f"{el}: ")
                display_phonebook(pb[el])
            elif isinstance(pb, list):
                print(f" {el}")
            else:
                print(f"  {pb}")
                break
    except:
        print("Не удалось прочитать телефонную книгу!")

    
config = get_config()

sp = get_phonebook(config)
sp_name = config["DEFAULT_PHONEBOOK"]

is_exit = False
while not is_exit:
    command = input('Введите команду: ')

    match command:
        case "/all":
            display_phonebook(sp)
        case "/add":
            f = input('Введите имя нового контакта: ')
            if f in sp:
                print('Контакт существует!')
            else:
                sp = add_contact(sp, f)
            print('\nКонтакт был успешно добавлен!')
        case "/del":
            f = input('Введите имя удаляемого контакта: ')
            del_contact(sp, f)
            display_phonebook(sp)
        case "/import":
            phonebook_name = input("Какую телефонную книгу хотите импортировать?: ")
            sp = import_phonebook(phonebook_name)
        case "/change":
            cn = change_contact(sp, input("Введите имя изменяемого контакта: "))
            sp = cn(input("Введите изменяемый параметр: "))
        case "/exit":
            export_phonebook(sp, sp_name)
            is_exit = True