1. Создать объект Парсера, передав ему путь до файла:
parser = Parser(path)
2. Запустить обработку файла через метод handle_file у созданного объекта Парсера: 
parser.handle_file()
3. Результат можно просмотреть, напечатав результат методов get_general_information и get_detailed_information у созданного объекта: print(parser.get_general_information)
