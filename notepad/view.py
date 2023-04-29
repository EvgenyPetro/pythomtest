def get_type():
    type = int(input("1 - показать заметки \n"
                     "2 - создать заметку \n"
                     "3 - обновить заметку \n"
                     "4 - удалить заметку \n"
                     "5 - показать заметку \n"
                     "6 - выход: "))
    return type


def save_new_note():
    title = input("Введите заголовок: ")
    note = input("Введите заметку: ")
    return title, note


def get_id():
    id = input("Введите id: ")
    return id


def update_note():
    id = get_id()
    title, body = save_new_note()
    return id, title, body

