from abc import ABC, abstractmethod
import json
import csv
from typing import Any, List, Dict

class AbstractFile(ABC):
    @abstractmethod
    def read(self) -> Any:
        '''Абстрактный метод для чтения данных из файла.'''

    @abstractmethod
    def write(self, data: Any) -> None:
        '''Абстрактный метод для записи данных в файл'''

    @abstractmethod
    def append(self, data: Any) -> None:
        '''Абстрактный метод для добавления данных в файл'''

class JsonFile(AbstractFile):
    def __init__(self, file_path: str):
        self.file_path: str = file_path

    def read(self) -> Dict[str, Any]:
        '''метод для чтения данных из json файла.'''
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def write(self, data: Dict[str, Any]) -> None:
        '''метод для записи данных в json файл'''
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    def append(self, data: Dict[str, Any]) -> None:
        '''метод для добавления данных в json файл'''
        with open(self.file_path, 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class TxtFile(AbstractFile):
    def __init__(self, file_path: str):
        self.file_path: str = file_path

    def read(self) -> str:
        '''метод для чтения данных из txt файла.'''
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write(self, data: str) -> None:
        '''метод для записи данных в txt файл'''
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(str(data) + '\n')

    def append(self, data: str) -> None:
        '''метод для добавления данных в txt файл'''
        with open(self.file_path, 'a', encoding="utf-8") as file:
            file.write(str(data) + '\n')

class CsvFile(AbstractFile):
    def __init__(self, file_path: str):
        self.file_path: str = file_path

    def read(self) -> List[List[str]]:
        '''метод для чтения данных из csv файла.'''
        with open(self.file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return list(reader)

    def write(self, data: List[List[str]]) -> None:
        '''метод для записи данных в csv файл'''
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def append(self, data: List[str]) -> None:
        '''метод для добавления данных в csv файл'''
        with open(self.file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)
