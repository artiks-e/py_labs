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
        return 0

def find30():
    table = open_table()
    count = 0
    if table:
        for book in table:
            if len(book[1]) > 30:
                count += 1
    print(count)

def author(name):
    table = open_table()
    if table:
        flag = 0
        for book in table:
            if name.lower() in book[2].lower():
                if 1997 <= int(book[3]) <= 2000:
                    flag = 1
                    print(book)
        if not flag:
            print("There's no books by this author")

def generator():
    table = open_table()
    if table:
        books = sample(table, 20)

        with open('result.txt', 'w', encoding='utf-8') as result:
            for n, book in enumerate(books):
                result.write(f"{n + 1}. {book[2]}. {book[1]} - {book[3]}\n")

def xml():
    with open('currency.xml', 'r') as xml_file:
        xml_data = xml_file.read()

    dom = minidom.parseString(xml_data)

    elements = dom.getElementsByTagName("Valute")
    currency_dict = {}

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
    for key in currency_dict.keys():
        print(key, currency_dict[key])

def unic_tags():
    table = open_table()
    if table:
        tags = set(book[4] for book in table)
        for tag in tags:
            print(tag)

def popular():
    table = open_table()
    if table:
        most_popular = sorted(table, key=lambda book: int(book[5]), reverse=True)[:20]
        for book in most_popular:
            print(book)


find30()
author("bar")
generator()
xml()
unic_tags()
popular()
