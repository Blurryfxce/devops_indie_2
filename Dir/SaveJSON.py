import json
from DataSaver import DataSaver


class SaveJSON(DataSaver):
    @staticmethod
    def save(data: dict, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
