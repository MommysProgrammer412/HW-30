from abc import ABC, abstractmethod

class AbstractFile(ABC):
    def read():
        '''Абстрактный метод для чтения данных из файла.'''
        pass
    def write(data):
        '''Абстрактный метод для записи данных в файл'''
        pass
    def append(data):
        '''Абстрактный метод для добавления данных в файл'''
        pass

class JsonFile(AbstractFile):
    file_path = 'data.json'#хз
    def read():
        '''Абстрактный метод для чтения данных из файла.'''
        pass
    def write(data):
        '''Абстрактный метод для записи данных в файл'''
        pass
    def append(data):
        '''Абстрактный метод для добавления данных в файл'''
        pass

class TxtFile(AbstractFile):
    file_path = 'data.txt'
    def read():
        '''Абстрактный метод для чтения данных из файла.'''
        pass
    def write(data):
        '''Абстрактный метод для записи данных в файл'''
        pass
    def append(data):
        '''Абстрактный метод для добавления данных в файл'''
        pass

class CsvFile(AbstractFile):
    file_path = 'data.csv'
    def read():
        '''Абстрактный метод для чтения данных из файла.'''
        pass
    def write(data):
        '''Абстрактный метод для записи данных в файл'''
        pass
    def append(data):
        '''Абстрактный метод для добавления данных в файл'''
        pass
