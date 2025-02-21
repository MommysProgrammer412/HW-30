from abc import ABC, abstractmethod
import json
import csv

class AbstractFile(ABC):
    @abstractmethod
    def read(self):
        '''Абстрактный метод для чтения данных из файла.'''
    @abstractmethod
    def write(self, data):
        '''Абстрактный метод для записи данных в файл'''
    @abstractmethod
    def append(self, data):
        '''Абстрактный метод для добавления данных в файл'''

class JsonFile(AbstractFile):
    def __init__(self, file_path: str):
        self.file_path = file_path
    def read(self):
        '''метод для чтения данных из json файла.'''
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    def write(self, data):
        '''метод для записи данных в json файл'''
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
    def append(self, data):
        '''метод для добавления данных в json файл'''
        with open(self.file_path, 'a', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

class TxtFile(AbstractFile):
    def __init__(self, file_path: str):
        self.file_path = file_path
    def read(self):
        '''метод для чтения данных из txt файла.'''
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()
    def write(self, data):
        '''метод для записи данных в txt файл'''
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write(str(data) + '\n')
    def append(self, data):
        '''метод для добавления данных в txt файл'''
        with open(self.file_path, 'a', encoding="utf-8") as file:
            file.write(str(data) + '\n')

class CsvFile(AbstractFile):
    def __init__(self, file_path: str):
        self.file_path = file_path
    def read(self):
        '''метод для чтения данных из csv файла.'''
        pass
    def write(self, data):
        '''метод для записи данных в csv файл'''
        pass
    def append(self, data):
        '''метод для добавления данных в csv файл'''
        pass
