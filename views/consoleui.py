from re import match

class ConsoleUI:
    def checked_input(self, start_msg: str, regex: str, mismatch_msg: str):
        while True:
            input_data = input(start_msg)
            if input_data == "":
                self.show("Ввод не должен быть пустым. Пожалуйста, повторите ввод: ")
            elif not match(regex, input_data):
                self.show(mismatch_msg)
                self.show("Пожалуйста, повторите ввод")
            else:
                return input_data

    def goodbye(self):
        self.show('Приятного дня!')

    def show(self, data: str):
        print(data)

    def welcome(self):
        self.show('Программа "Заметки"')