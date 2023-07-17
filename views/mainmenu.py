class MainMenu:
    def __init__(self):
        self.count = 7

    def get(self) -> str:
        menu = ''
        menu += "1. Показать все заметки\n"
        menu += "2. Поиск заметки по содержимому\n"
        menu += "3. Добавить новую заметку\n"
        menu += "4. Получить заметку\n"
        menu += "5. Редактировать заметку\n"
        menu += "6. Удалить заметку\n"
        menu += "7. Выход"
        return menu
