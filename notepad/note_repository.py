from datetime import datetime, date, time

import read_note
import write_note


def save_note(title, note):
    id = len(get_notes()) + 1
    write_note.write_notepad(id, title, note, create_date())


def save_notes(notes):
    write_note.write_notes_in_notepad(notes)


def get_notes():
    return read_note.read_notepad()


def get_note(id):
    for note in get_notes():
        if note[0] == id:
            print(note)


def update_note(id, title, body):
    notes = get_notes()
    for note in notes:
        if note[0] == id:
            notes.remove(note)
            update_note = (f"{id};{title};{body};{create_date()}")
            notes.append(update_note)
    save_notes(sorted(notes))


def delete_note(id):
    notes = get_notes()
    for note in notes:
        if note[0] == id:
            notes.remove(note)
    save_notes(sorted(notes))


def print_notes():
    print(get_notes())


def create_date():
    date_now = datetime.now()
    return date_now.strftime("%d.%m.%Y %H:%M")
