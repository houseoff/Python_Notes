from os import path
from models.saveload import SaveLoadHandler


class IDGenerator:
    __CFG = "cfg.json"

    def __init__(self, start_id: int):
        self.handler = SaveLoadHandler(self.__CFG)
        self._id = max(start_id, 0)
        self.cfg = {"id": self._id}
        if path.exists(self.__CFG):
            self.cfg = self.handler.load()
            self._id = self.cfg["id"]

    def get_id(self) -> int:
        id = self._id
        self._id += 1
        return id

    def set_id(self, new_id: int):
        self._id = new_id

    def show_next_id(self):
        return self._id

    def export_cfg(self):
        self.cfg["id"] = self._id
        self.handler.save(self.cfg)
