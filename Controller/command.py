import Presenter.loadFromFile as lF
import Presenter.writeToFile as wF
import Model.Note

def add_note():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    note = Model.Note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Model.Note.Note.get_id(note) == Model.Note.Note.get_id(i):
            Model.Note.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Заметка добавлена в список")

def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("СПИСОК ЗАМЕТОК:")
            for i in array_notes:
                print(Model.Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Model.Note.Note.get_id(i))
            id = input("\nВведите ID заметки: ")
            flag = True
            for i in array_notes:
                if id == Model.Note.Note.get_id(i):
                    print(Model.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif txt == "date":
            date = input("Введите дату в формате: DD.MM.YYYY: ")
            flag = True
            for i in array_notes:
                date_note = str(Model.Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Model.Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Список заметок пуст")

def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == Model.Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'a')
        print("Заметка с ID: ", id, " успешно удалена")
    else:
        print("Нет такого ID")

def change_note():
    id = input("Введите ID редактируемой заметки: ")
    array_notes = lF.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Model.Note.Note.get_id(i):
            i.title = input("Измените  заголовок:\n")
            i.body = input("Измените  описание:\n")
            Model.Note.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wF.write_file(array_notes_new, 'a')
        print("Заметка с ID: ", id, " успешно изменена")
    else:
        print("Нет такого ID")




