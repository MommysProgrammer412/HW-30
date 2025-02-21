from file_classes import JsonFile, TxtFile, CsvFile

def test_json_file():
    json_file = JsonFile('test.json')
    json_file.write({'ключ': 'значение'})
    print("Чтение JSON:", json_file.read())
    json_file.append({'новый_ключ': 'новое_значение'})
    print("Чтение JSON после добавления:", json_file.read())

def test_txt_file():
    txt_file = TxtFile('test.txt')
    txt_file.write('Привет, мир!')
    print("Чтение TXT:", txt_file.read())
    txt_file.append('\nНовая строка')
    print("Чтение TXT после добавления:", txt_file.read())

def test_csv_file():
    csv_file = CsvFile('test.csv')
    csv_file.write([['Имя', 'Возраст'], ['Алиса', '30'], ['Борис', '25']])
    print("Чтение CSV:", csv_file.read())
    csv_file.append([['Виктор', '35']])
    print("Чтение CSV после добавления:", csv_file.read())

if __name__ == "__main__":
    test_json_file()
    test_txt_file()
    test_csv_file()