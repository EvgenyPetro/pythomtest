def write_notepad(id, title, note, date):
    with open("notepad.csv", "a") as notepad_file:
        note = (f"{id};{title};{note};{date}\n")
        notepad_file.write(note)


def write_notes_in_notepad(notes):
    with open("notepad.csv", "w") as notepad_file:
        for note in notes:
            notepad_file.write(f"{note}\n")

