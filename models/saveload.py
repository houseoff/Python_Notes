from os import path
import json


class SaveLoadHandler:
    def __init__(self, filename: str):
        self._filename = filename

    def load(self):
        if path.exists(self._filename):
            try:
                with open(self._filename, 'r', encoding='utf-8') as file:
                    return json.loads(file.read())
            except Exception:
                open(self._filename, 'r', encoding='utf-8').close()

    def save(self, data):
        with open(self._filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)
