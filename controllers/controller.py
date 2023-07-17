from models.notes import Notes
from views.consoleui import ConsoleUI
from views.mainmenu import MainMenu
from views.sortmenu import SortMenu
from views.editnotemenu import EditNoteMenu


class Controller:
    def __init__(self, model: Notes, view: ConsoleUI):
        self.model = model
        self.view = view

    def run(self):
        self.view.welcome()
        while True:
            self.view.show(MainMenu().get())
            choice = self.view.checked_input(start_msg="Введите команду: ",
                                             regex=f"^[1-{MainMenu().count}]",
                                             mismatch_msg="Выберите пункт меню")
            if choice == "1":
                if self.model.count() == 0:
                    self.view.show("Заметок не найдено")
                else:
                    self.view.show(SortMenu().get())
                    sort_choice = self.view.checked_input(start_msg="Ввод: ",
                                                          regex=f"^[1-{SortMenu().count}]",
                                                          mismatch_msg="Выберите пункт меню")
                    if sort_choice == "1":
                        self.view.show(self.model.sort_by_head())
                    elif sort_choice == "2":
                        self.view.show(self.model.sort_by_created())
                    else:
                        self.view.show(self.model.sort_by_changed())

            elif choice == "2":
                if self.model.count() == 0:
                    self.view.show("Заметок не найдено")
                else:
                    sought = self.view.checked_input(start_msg="Введите шаблон для поиска: ",
                                                     regex=".*",
                                                     mismatch_msg="Ошибка при вводе")
                    self.view.show(self.model.find_note(sought))

            elif choice == "3":
                head = self.view.checked_input(start_msg="Введите заголовок заметки: ",
                                               regex=".*",
                                               mismatch_msg="Ошибка при вводе")
                text = self.view.checked_input(start_msg="Введите содержимое заметки: ",
                                               regex=".*",
                                               mismatch_msg="Ошибка при вводе")
                self.view.show(self.model.add_note(head, text))

            elif choice == "4":
                if self.model.count() == 0:
                    self.view.show("Заметок не найдено")
                else:
                    note_id = int(self.view.checked_input(start_msg="Введите ID заметки, которую хотите получить: ",
                                                      regex=f"^[1-{self.model.count()}]",
                                                      mismatch_msg="Некорректный ID"))
                    self.view.show(self.model.get_note(note_id))

            elif choice == "5":
                if self.model.count() == 0:
                    self.view.show("Заметок не найдено")
                else:
                    note_id = int(self.view.checked_input(start_msg="Введите ID заметки, которую хотите изменить: ",
                                                      regex=f"^[1-{self.model.count()}]",
                                                      mismatch_msg="Некорректный ID"))
                    self.view.show(EditNoteMenu().get())
                    edit_choice = self.view.checked_input(start_msg="Ввод: ",
                                                          regex=f"^[1-{EditNoteMenu().count}]",
                                                          mismatch_msg="Выберите пункт меню")
                    if edit_choice == "1":
                        new_head = self.view.checked_input(start_msg="Введите новый заголовок заметки: ",
                                                           regex=".*",
                                                           mismatch_msg="Ошибка при вводе")
                        self.view.show(self.model.edit_note_head(note_id, new_head))
                    elif edit_choice == "2":
                        new_text = self.view.checked_input(start_msg="Введите новый текст заметки: ",
                                                           regex=".*",
                                                           mismatch_msg="Ошибка при вводе")
                        self.view.show(self.model.edit_note_text(note_id, new_text))
                    else:
                        new_head = self.view.checked_input(start_msg="Введите новый заголовок заметки: ",
                                                           regex=".*",
                                                           mismatch_msg="Ошибка при вводе")
                        self.view.show(self.model.edit_note_head(note_id, new_head))
                        new_text = self.view.checked_input(start_msg="Введите новый текст заметки: ",
                                                           regex=".*",
                                                           mismatch_msg="Ошибка при вводе")
                        self.view.show(self.model.edit_note_text(note_id, new_text))

            elif choice == "6":
                if self.model.count() == 0:
                    self.view.show("Заметок не найдено")
                else:
                    note_id = int(self.view.checked_input(start_msg="Введите ID заметки, которую хотите удалить: ",
                                                      regex=f"^[1-{self.model.count()}]",
                                                      mismatch_msg="Некорректный ID"))
                    self.view.show(self.model.remove_note(note_id))
            else:
                self.view.goodbye()
                self.model.save_cfg()
                self.model.save_notes()
                break
