import note_repository as repository
import view


def start():
    while True:
        type = view.get_type()
        if type == 1:
            repository.print_notes()
        if type == 2:
            title, body = view.save_new_note()
            repository.save_note(title, body)
        if type == 3:
            id, title, body = view.update_note()
            repository.update_note(id, title, body)
        if type == 4:
            repository.delete_note(view.get_id())
        if type == 5:
            repository.get_note(view.get_id())
        elif type == 6:
            exit(0)

