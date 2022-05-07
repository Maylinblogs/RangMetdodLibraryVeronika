import os
import socket
import time
users=[]

import stdiomask
from prettytable import PrettyTable
ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
class Person():

    # initialization or constructor method of
    def __init__(self):
        # class Student
        self.name = input('enter student name:')
        self.surname = input('enter student surname:')
        self.patronymic = input('enter patr:')

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic
class Dogovor():
    def __init__(self):
        self.format=format()
        self.copy=int(input("input amiubt of copy"))
class BookSeria():
    def __init__(self):
        self.bookname=input("enter bookname")
class Book(BookSeria):
    def __init__(self):
        self.cycle=input('input cycle')
        self.janr=janr()
class Metod():
    def rang(self):
        while True:
            Z = []
            n = 3
            m = 3
            for i in range(n):
                b = []
                for i in range(m):
                    b.append(int(input('enter ints')))
                    Z.append((b))

            # посчитаем матрицу нормированных оценок
            z = [[i / 3 for i in row] for row in Z]
            print(z)
            # Находим веса целей
            w_1 = (z[0][0] + z[1][0] + z[2][0]) / 3
            print('reshenie 1')
            print(w_1)
            w_2 = (z[0][1] + z[1][1] + z[2][1]) / 3
            print('reshenie 2')
            print(w_2)
            w_3 = (z[0][2] + z[1][2] + z[2][2]) / 3
            print('reshenie 3')
            print(w_3)
            lis = [w_1, w_2, w_3]
            print("Самое выгодное решение ")
            print(max(lis))
            time.sleep(2)
            global kolvo
            kolvo=max(lis)
            return (max(lis))
def format():
    while True:
        print("Выберите формат 1.Сверхкурпные 2.Крупные 3.Среднние 4.Малые 5.Сверхмалые")
        answer=input()
        if answer=='1':
            return "Сверхкурпные"
        elif answer=='2':
            return "Крупные"
        elif answer=='3':
            return "Средние"
        elif answer=='4':
            return "Малые"
        elif answer=='5':
            return "Сверхмалые"
        else:
            print("Попробуйте еще раз")
def janr():
    while True:
        print("Выберите жанр 1.Детектив 2.Фантастика 3.Роман 4.Детская 5.Научная")
        answer=input()
        if answer=='1':
            return "Детектив"
        elif answer=='2':
            return "Фантастика"
        elif answer=='3':
            return "Роман"
        elif answer=='4':
            return "Детская"
        elif answer=='5':
            return "Научная "
        else:
            print("Попробуйте еще раз")
def clear(): os.system('cls')
def client_mode():
    clear()
    person=Person()
    print("hello "+person.name)
    while True:
        print('1.Добавление книги')
        print('2.Просмотр книг')
        print('3.Редактирование записи')
        print('4.Удаление записи')
        print('5.Сортировка записей')
        print('6.Поиск записей')
        print('7.тотал')
        choice=input('enter what you want:')
        if choice=='1':
            add_client(person)
        elif choice=='2':
            watch_client(person)
        elif choice=='3':
            change_client(person)
        elif choice=='4':
            delete_client(person)
        elif choice=='5':
            sort_client(person)
        elif choice=='6':
            find_client(person)
        elif choice=='7':
            total(person)
        elif choice=='8':
            break
        else:
            print("try again")
def total(person):
    watch_client(person)
    k=[]
    sum=0
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
            if person.name == name and person.surname == surname and person.patronymic == patronymic:
                k.append(money)
    array = [int(numeric_string) for numeric_string in k]
    for elem in array:
        sum+=elem

    print("|Итого:")
    print(sum)
def add_client(person):
    while True:
        clear()
        seria = BookSeria()
        book=Book()
        dog=Dogovor()
        money=dog.copy*kolvo
        file = open('tabl.txt', 'a')
        file.write('%s %s %s %s %s %s %s %d %d\n' % (
            person.name, person.surname, person.patronymic, seria.bookname, book.cycle, book.janr, dog.format, dog.copy,
            money))
        file.close()
        clear()
        break
def watch_client(person):
    clear()
    mytable = PrettyTable()
    mytable.field_names = ["name", "surname", "patronymic", "bookname", "cycle", "janr", "format", "amount", "money"]
    mytable.clear_rows()
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
            if person.name == name and person.surname == surname and person.patronymic == patronymic:
                mytable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

    file.close()
    print(mytable)
    time.sleep(3)
    clear()
    mytable.clear_rows()
def delete_client(person):
    while True:
        clear()
        watch_client(person)
        choice=input('enter 1del all 2del 1')
        if choice=='1':
            l = []
            d=[]
            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
                    if person.name != name and person.surname != surname and person.patronymic != patronymic:
                        myline = line.split(' ')
                        d.append(myline)

            with open('tabl.txt', 'w') as x:
                for sub_list in d:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')
            l.clear()
            d.clear()
            break
        elif choice=="2":

            l = []
            l.clear()
            d = []
            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
                    if person.name != name and person.surname != surname and person.patronymic != patronymic:
                        myline = line.split(' ')
                        d.append(myline)
            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
                    if person.name == name and person.surname == surname and person.patronymic == patronymic:
                        myline = line.split(' ')
                        l.append(myline)
            index = int(input('enter what column to delete: '))
            del l[index - 1]
            f = open('tabl.txt', 'w')
            f.close()
            with open('tabl.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')
            with open('tabl.txt', 'a') as x:
                for sub_list in d:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')
            l.clear()
            d.clear()
            watch_client(person)
            clear()
            break
def change_client(person):
    clear()
    l = []
    d=[]
    l.clear()
    d.clear()
    print(l)

    watch_client(person)
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
            if person.name!=name and person.surname!=surname and person.patronymic!=patronymic:
                myline = line.split(' ')
                d.append(myline)
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
            if person.name==name and person.surname==surname and person.patronymic==patronymic:
                myline = line.split(' ')
                l.append(myline)
    index = int(input('enter what column to change: '))
    del l[index - 1]
    f = open('tabl.txt', 'w')
    f.close()
    with open('tabl.txt', 'w') as x:
        for sub_list in l:
            for item in sub_list:

                x.write(item + ' ')
            x.write('\n')
    with open('tabl.txt', 'a') as x:
        for sub_list in d:
            for item in sub_list:

                x.write(item + ' ')
            x.write('\n')
    l.clear()
    d.clear()
    add_client(person)
def sort_client(person):
    clear()
    myytable = PrettyTable()
    myytable.field_names = ["name", "surname", "patronymic", "bookname", "cycle", "janr", "format", "amount", "money"]
    myytable.clear_rows()
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
            if person.name == name and person.surname == surname and person.patronymic == patronymic:
                myytable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

    file.close()
    choice = input('sor by 1amount 2money')
    while True:
        if choice == '1':
            print(myytable.get_string(sortby='amount', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            clear()
            break
        elif choice == '2':
            print(myytable.get_string(sortby='money', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            clear()
            break
        else:
            clear()
            break
def find_client(person):
    while True:
        clear()
        newtable = PrettyTable()
        newtable.field_names = ["name", "surname", "patronymic", "bookname", "cycle", "janr", "format", "amount",
                                "money"]
        choice = input('find by 1bookname 2janr 3.format')
        if choice == '1':
            newbookname = input('enter bookname:')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
                    if newbookname == bookname and person.name == name and person.surname == surname and person.patronymic == patronymic:
                        newtable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

            file.close()
            print(newtable)
            time.sleep(3)
            clear()
            break
        elif choice == '2':
            newmodel = input('enter janr:')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
                    if newmodel == janr and person.name == name and person.surname == surname and person.patronymic == patronymic:
                        newtable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

            file.close()
            print(newtable)
            time.sleep(3)
            clear()
            break
        elif choice == '3':
            newsize = input('enter format:')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
                    if newsize == format and person.name == name and person.surname == surname and person.patronymic == patronymic:
                        newtable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

            file.close()
            print(newtable)
            time.sleep(3)
            clear()
            break
        else:
            print('try again')
def admin_mode():
    clear()
    while True:
        print("1.Добавление записи\n")
        print("2.Просмотр записи\n")
        print("3.Редактирование записи\n")
        print("4.Удаление записи\n")
        print("5.Работа с пользователями\n")
        print("6.Поиск записи\n")
        print("7.Сортировка записи\n")
        print("8.Выход\n")
        choice_3=input("Выберите действие: ")
        if choice_3=='1':
            clear()
            add()
        elif choice_3=='2':
            clear()
            watch()
        elif choice_3=='3':
            clear()
            change()
        elif choice_3=='4':
            clear()
            delete()
        elif choice_3=='5':
            clear()
            work()
        elif choice_3=='6':
            clear()
            find()
        elif choice_3=='7':
            clear()
            sort()
        elif choice_3=='8':
            clear()
            break
        else:
            print('try again')
            time.sleep(1)
            clear()
def add():
    clear()
    while True:
        person=Person()
        seria=BookSeria()
        book=Book()
        dog=Dogovor()
        money=dog.copy*kolvo
        file = open('tabl.txt', 'a')
        file.write('%s %s %s %s %s %s %s %d %d\n' % (
            person.name, person.surname, person.patronymic, seria.bookname, book.cycle, book.janr, dog.format, dog.copy,
            money))
        file.close()
        clear()
        break
def watch():
    clear()
    mytable = PrettyTable()
    mytable.field_names = ["name", "surname", "patronymic", "bookname", "cycle", "janr", "format", "amount", "money"]
    mytable.clear_rows()
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, bookname , cycle, janr, format, amount, money) = line.split(' ')
            mytable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

    file.close()
    print(mytable)
    time.sleep(2)
    mytable.clear_rows()
    clear()
def delete():
    clear()
    while True:
        choice = input('1.delete all 2 one')
        if choice == '1':
            grid = 9
            l = []
            watch()
            with open("tabl.txt", 'r') as f:
                for line in (line.rstrip() for line in f.readlines()):
                    myline = line.split(' ')
                    l.append(myline)
            l.clear()
            with open('tabl.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')

            break
        elif choice == '2':
            grid = 9
            l = []
            watch()
            with open("tabl.txt", 'r') as f:
                for line in (line.rstrip() for line in f.readlines()):
                    myline = line.split(' ')
                    l.append(myline)

            index = int(input('enter what column to delete: '))
            l.pop(index - 1)
            with open('tabl.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item + ' ')
                    x.write('\n')

            l.clear()
            watch()
            clear()
            break
        else:
            print('try again')
def change():
    clear()
    while True:
        grid = 9
        l = []
        watch()
        with open("tabl.txt", 'r') as f:
            for line in (line.rstrip() for line in f.readlines()):
                myline = line.split(' ')
                l.append(myline)

        index = int(input('enter what column to change: '))
        l.pop(index - 1)
        with open('tabl.txt', 'w') as x:
            for sub_list in l:
                for item in sub_list:
                    x.write(item + ' ')
                x.write('\n')

        l.clear()
        add()
        watch()
        clear()
        break
def work():
    clear()
    users={}
    with open("users.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (key, value) = line.split(' ')

            users[key] = value
    while True:
        l=[]
        choice=input('1.Удаление 2.Добавление 3.Выход')
        if choice=='1':

            index=int(input('what user to delete:'))
            grid = 9


            with open("users.txt", 'r') as f:
                for line in (line.rstrip() for line in f.readlines()):
                    myline = line.split(' ')
                    l.append(myline)
            print(l)
            index = int(input('what user to delete:'))
            del l[index-1]
            file=open('users.txt', 'w')
            file.close()
            with open('users.txt', 'w') as x:
                for sub_list in l:
                    for item in sub_list:
                        x.write(item)
                        x.write(" ")
                    x.write('\n')

            l.clear()
            clear()
            break
        elif choice=='2':
            clear()
            registration()
            clear()
            break
        elif choice=='3':
            clear()
            break
        else:
            print('try again')
def sort():
    clear()
    myytable = PrettyTable()
    myytable.field_names = ["name", "surname", "patronymic", "bookname", "cycle", "janr", "format", "amount", "money"]
    myytable.clear_rows()
    with open("tabl.txt", 'r') as file:
        for line in (line.rstrip() for line in file.readlines()):
            (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
            myytable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

    file.close()
    choice = input('sor by 1money 2 amount ')
    while True:
        if choice == '1':
            print(myytable.get_string(sortby='money', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            clear()
            break
        elif choice == '2':
            print(myytable.get_string(sortby='amount', sort_key=lambda row: int(row[0])))
            time.sleep(3)
            clear()
            break
        else:
            clear()
            break
def find():
    while True:
        newtable = PrettyTable()
        newtable.field_names = ["name", "surname", "patronymic", "bookname", "cycle", "janr", "format", "amount",
                                "money"]
        choice = input('find by 1surname 2janr 3.format')
        if choice == '1':
            nsurname = input('enter surname:')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
                    if nsurname == surname:
                        newtable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

            file.close()
            print(newtable)
            time.sleep(3)
            clear()
            break
        elif choice == '2':
            newmodel = input('enter janr:')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
                    if newmodel == janr:
                        newtable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

            file.close()
            print(newtable)
            time.sleep(3)
            clear()
            break
        elif choice == '3':
            newsize = input('enter format:')

            with open("tabl.txt", 'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (name, surname, patronymic, bookname, cycle, janr, format, amount, money) = line.split(' ')
                    if newsize == format:
                        newtable.add_row([name, surname, patronymic, bookname, cycle, janr, format, amount, money])

            file.close()
            print(newtable)
            time.sleep(3)
            clear()
            break
        else:
            break
def authorization():
    while True:
        clear()
        login=input('Введите логин:')

        pas=stdiomask.getpass("Введите пароль: ")
        if login=='admin' and pas=="admin":
            admin_mode()
            break
        else:
            #users = {}
            with open("users.txt",'r') as file:
                for line in (line.rstrip() for line in file.readlines()):
                    (key, value) = line.split(' ')
                    if login==key and pas==value:
                        clear()
                        client_mode()
                        clear()
                        break



            if EOFError:
                break
def registration():
    clear()
    key = input('Введите логин ')
    value = stdiomask.getpass("Введите пароль")
    while True:
        if len(key) > 5 and len(value) > 5:
            file = open("users.txt", "a")
            file.write('%s %s\n' % (key, value))
            file.close()
            clear()
            break
        else:
            print("Логин и пароль не менее 6 символов,попрбуйте еще раз")
            break
def enter():
    while True:
        clear()
        answer = input('1.Регистрация\n2.Вход\n3.Выход\n')
        if answer == '1':
            registration()
        elif answer == '2':
            authorization()
        elif answer == '3':
            break
        else:
            print("Неверно.Попробуйте еще раз: ")
def Main():
    while True:
        Input = input('Do you want to enter?yes or no ')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        Response=Response.decode('utf-8')
        if Response=='im ready':
            rang=Metod()
            kolv0=rang.rang()
            enter()
            break
        else:
            print('bye')
            break


    ClientSocket.close()
if __name__ == '__main__':
    Main()


