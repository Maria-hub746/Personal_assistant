from AddressBook import *
from abc import ABC, abstractmethod


class Singleton:
    __instance = None

    def __init__(self):
        self.book = AddressBook()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(Singleton)
        return cls.__instance



class Add:
    def __init__(self):
        self.book = AddressBook()
    def func(self, action):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        return self.book.add(record)


class Search:
    def __init__(self):
        self.book = AddressBook()
    def func(self, action):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = (self.book.search(pattern, category))
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)


class Edit:
    def __init__(self):
        self.book = AddressBook()
    def func(self, action):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        return self.book.edit(contact_name, parameter, new_value)


class Remove:
    def __init__(self):
        self.book = AddressBook()
    def func(self, action):
        pattern = input("Remove (contact name or phone): ")
        return self.book.remove(pattern)


class Save:
    def __init__(self):
        self.book = AddressBook()
    def func(self, action):
        file_name = input("File name: ")
        return self.book.save(file_name)


class Load:
    def __init__(self):
        self.book = AddressBook()
    def func(self, action):
        file_name = input("File name: ")
        return self.book.load(file_name)


class Congratulate:
    def __init__(self):
        self.book = AddressBook()
    def func(self, action):
        print(self.book.congratulate())


class View:
    def __init__(self):
        self.book = AddressBook()
    def func(self, action):
        print(self.book)


class Exit:
    def func(self, action):
        pass


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == 'add':
            add = Add()
            add.func(action)
        elif action == 'search':
            search = Search()
            search.func(action)
        elif action == 'edit':
            edit = Edit()
            edit.func(action)
        elif action == 'remove':
            remove = Remove()
            remove.func(action)
        elif action == 'save':
            save = Save()
            save.func(action)
        elif action == 'load':
            load = Load()
            load.func(action)
        elif action == 'congratulate':
            congratulate = Congratulate()
            congratulate.func(action)
        elif action == 'view':
            view = View()
            view.func(action)
        elif action == 'exit':
            exit = Exit()
            exit.func(action)
        else:
            print("There is no such command!")
