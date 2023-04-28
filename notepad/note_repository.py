import read_note
import write_note


def save_notes(id, title, note):
    write_note.write_notepad(id, title, note)


def get_notes():
    notes = read_note.read_notepad()
    print(notes)
