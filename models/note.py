from time import time, localtime, strftime


class Note:
    def __init__(self, note_id: int, head: str, text: str, created: float, changed: float = None):
        self.note_id = note_id
        self.head = head
        self.text = text
        self.created = created
        if changed is None:
            self.changed = self.created
        else:
            self.changed = changed

    @staticmethod
    def from_dict(dct: dict):
        return Note(note_id=dct["id"],
                    head=dct["head"],
                    text=dct["text"],
                    created=dct["created"],
                    changed=dct["changed"])

    def to_dict(self):
        return {"id": self.note_id,
                "head": self.head,
                "text": self.text,
                "created": self.created,
                "changed": self.changed}

    def set_head(self, new_head: str):
        self.head = new_head

    def set_text(self, new_text: str):
        self.text = new_text

    def set_changed(self, new_timestamp: float):
        self.changed = new_timestamp

    def to_str(self) -> str:
        date_format = "%d.%m.%Y %H:%M"
        output = f'ID: {self.note_id}\n' + \
                 f'Заголовок: {self.head}\n' + \
                 f'Дата создания: {strftime(date_format, localtime(self.created))}\n'
        if self.changed is not None:
            output += f'Дата изменения: {strftime(date_format, localtime(self.changed))}'
        return output