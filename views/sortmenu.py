class SortMenu:
    def __init__(self):
        self.count = 3

    def get(self) -> str:
        menu = "Выберите необходимую сортировку заметок\n"
        menu += "1. По содержимому заголовка\n"
        menu += "2. По дате создания\n"
        menu += "3. По дате изменения"
        return menu