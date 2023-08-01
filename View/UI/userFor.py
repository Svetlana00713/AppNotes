import View.UI.printMenu as m

def user_for():
    m.printMenuTitle("Главное меню\n           СПИСОК ЗАМЕТОК")
    print("1 - вывод списка \n2 - вывод заметки по id \n3 - выбор заметки по дате\n4 - редактирование заметки"
          " \n5 - добавление заметки\n6 - удаление заметки\n7 - выход")
    m.printMenuLine()
    print("\n Введите пункт из меню: ")
