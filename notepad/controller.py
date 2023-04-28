import note_repository as repository
def start():
    repository.get_notes()
    repository.save_notes(3, "title", "note")
