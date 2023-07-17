from os import path
from time import time
from re import match
from models.saveload import SaveLoadHandler
from models.idgenerator import IDGenerator
from models.note import Note
from operator import attrgetter


class Notes:
    __NOTES_DB = "notes.db"

    def __init__(self):
        self.__cache = {}
        self.id_generator = IDGenerator(start_id=1)
        self.handler = SaveLoadHandler(self.__NOTES_DB)
        if path.exists(self.__NOTES_DB):
            json_list = self.handler.load()
            if json_list is not None:
                for dct in json_list:
                    note = Note.from_dict(dct)
                    self.__cache[note.note_id] = note

    def __check_id(self, note_id) -> int:
        if len(self.__cache) != 0 or note_id in self.__cache:
            return note_id
        else:
            return -1

    def __get_note(self, note_id) -> Note | None:
        if self.__check_id(note_id) != -1:
            return self.__cache[note_id]
        else:
            return None

    def __get_notes(self, notes) -> str:
        if self.count() == 0:
            return "Заметок нет"
        else:
            result = ''
            for note in notes:
                result += note.to_str()
                result += '\n'
            return result

    def add_note(self, head: str, text: str) -> str:
        note = Note(note_id=self.id_generator.get_id(),
                    created=time(),
                    head=head,
                    text=text)
        self.__cache[note.note_id] = note
        return "Заметка успешно добавлена"

    def count(self):
        return len(self.__cache)

    def edit_note_head(self, note_id: int, new_head: str) -> str:
        if self.__check_id(note_id) != -1:
            self.__cache[note_id].set_head(new_head)
            self.__cache[note_id].set_changed(time())
            return f"Заголовок заметки с ID {note_id} изменен успешно"
        else:
            return f"Не найдено заметки с ID {note_id}"

    def edit_note_text(self, note_id: int, new_text: str) -> str:
        if self.__check_id(note_id) != -1:
            self.__cache[note_id].set_text(new_text)
            self.__cache[note_id].set_changed(time())
            return f"Текст заметки с ID {note_id} изменен успешно"
        else:
            return f"Не найдено заметки с ID {note_id}"

    def find_note(self, sought: str) -> str:
        result = f'По запросу "{sought}" найдены следующие заметки\n'
        find = False
        for key in self.__cache:
            if match(f'.*{sought.lower()}.*', f"{self.__cache[key].head} {self.__cache[key].text}".lower()):
                result += self.get_note(key)
                find = True
        if not find:
            result = f'Заметки с содержимым "{sought}" не найдено'
        return result

    def get_note(self, note_id: int) -> str:
        if self.__check_id(note_id) != -1:
            return self.__cache[note_id].to_str() + f"\nТекст: {self.__cache[note_id].text}\n"
        else:
            return f"Не найдено заметки с ID {note_id}"

    def get_notes(self) -> str:
        return self.__get_notes(self.__cache.values())

    def remove_note(self, note_id: int) -> str:
        if self.__check_id(note_id) != -1:
            self.__cache.pop(note_id)
            if note_id == self.id_generator.show_next_id() - 1:
                self.id_generator.set_id(note_id)
            return f"Удаление заметки с ID {note_id} прошло успешно"
        else:
            return f"Не найдено заметки с ID {note_id}"

    def save_cfg(self):
        self.id_generator.export_cfg()

    def save_notes(self):
        serialization_list = []
        for note in self.__cache.values():
            serialization_list.append(Note.to_dict(note))
        self.handler.save(serialization_list)

    def sort_by_head(self) -> str:
        return self.__get_notes(sorted(self.__cache.values(), key=attrgetter('head')))

    def sort_by_created(self) -> str:
        return self.__get_notes(sorted(self.__cache.values(), key=attrgetter('created'), reverse=True))

    def sort_by_changed(self) -> str:
        return self.__get_notes(sorted(self.__cache.values(), key=attrgetter('changed'), reverse=True))
