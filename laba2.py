from csv import reader
import xml.dom.minidom as minidom
from random import sample


def open_table():
    try:
        with open('books-en.csv', 'r', encoding="utf-8") as csvfile:
            table = list(reader(csvfile, delimiter=';'))
            table = table[1:]
            return table

    except FileNotFoundError:
        print('Файл не найден!')
        return ""

def open_xml():
    try:
        with open('currency.xml', 'r') as xml_file:
            xml_data = xml_file.read()
        dom = minidom.parseString(xml_data)
        elements = dom.getElementsByTagName("Valute")
        return elements

    except FileNotFoundError:
        print('Файл не найден!')
        return ""

def find30():
    table = open_table()
    count = 0
    if table:
        for book in table:
            if len(book[1]) > 30:
                count += 1
        print(f"Книг с названием длиннее 30 символов: {count}")

def author():
    table = open_table()
    if table:
        while True:
            name = input("Введите имя автора или 0 для завершения: ")
            if name == "0": break
            flag = 0
            for book in table:
                if name.lower() in book[2].lower():
                    if 1997 <= int(book[3]) <= 2000:
                        flag = 1
                        print(book)
            if not flag:
                print("Нет книг этого автора")
            input("Нажмите Enter")

def generator():
    table = open_table()
    if table:
        books = sample(table, 20)

        with open('result.txt', 'w', encoding='utf-8') as result:
            for n, book in enumerate(books):
                result.write(f"{n + 1}. {book[2]}. {book[1]} - {book[3]}\n")

def xml():
    elements = open_xml()
    currency_dict = {}
    if elements:
        for node in elements:
            for child in node.childNodes:
                if child.nodeType == 1:
                    if child.tagName == "CharCode":
                        if child.firstChild.nodeType == 3:
                            title = child.firstChild.data
                    elif child.tagName == "Nominal":
                        if child.firstChild.nodeType == 3:
                            price = int(child.firstChild.data)
            currency_dict[title] = price

    print(currency_dict)
    # for key in currency_dict.keys():
        # print(key, currency_dict[key])

def unic_tags():
    table = open_table()
    if table:
        tags = set(book[4] for book in table)
        print("Перечень издательств без повторений:")
        # for tag in tags:
        #     print(tag)
        print(tags)

def popular():
    table = open_table()
    if table:
        print("20 самых популярных книг по скачиваниям:")
        most_popular = sorted(table, key=lambda book: int(book[5]), reverse=True)[:20]
        print(most_popular)
        # for book in most_popular:
        #     print(book)


find30()
generator()
xml()
unic_tags()
popular()
author()
