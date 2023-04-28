from datetime import datetime, date, time


def write_notepad(id, title, note):
    with open("notepad.csv", "a") as notepad_file:
        date_now = datetime.now()
        date_now = date_now.strftime("%d.%m.%Y %H:%M")
        note = (f"{id};{title};{note};{date_now}\n")
        notepad_file.write(note)
