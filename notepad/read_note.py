def read_notepad():
    with open("notepad.csv", "r") as notepad_file:
        notes = []
        for i in notepad_file.read().splitlines():
            notes.append(i)
    return notes
