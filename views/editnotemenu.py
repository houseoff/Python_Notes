class EditNoteMenu:
    def __init__(self):
        self.count = 3

    def get(self) -> str:
        menu = "Выберите элемент заметки для изменения\n"
        menu += "1. Заголовок\n"
        menu += "2. Текст\n"
        menu += "3. И заголовок, и текст"
        return menu