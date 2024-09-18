import sqlite3
import random


class DataController:
    def __init__(self):
        self.__conn = sqlite3.connect('author_books.sqlite3')
        self.__cursor = self.__conn.cursor()

        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS author (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            birth_date DATE NOT NULL,
                            birth_place TEXT NOT NULL)''')

        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            category_name TEXT NOT NULL,
                            number_of_pages INTEGER NOT NULL,
                            date_of_issue DATE NOT NULL,
                            author_id INTEGER NOT NULL,
                            FOREIGN KEY(author_id) REFERENCES author(id))''')

    def insert_author(self, first_name, last_name, birth_date, birth_place):
        self.__cursor.execute('''
        INSERT INTO author (first_name, last_name, birth_date, birth_place)
        VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, birth_date, birth_place))
        self.__conn.commit()

    def insert_book(self, name, category_name, number_of_pages, date_of_issue):
        author_id = self.__get_random_author_id()
        if author_id is None:
            print("No authors available to assign to the book.")
            return
        self.__cursor.execute('''
        INSERT INTO books (name, category_name, number_of_pages, date_of_issue, author_id)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, category_name, number_of_pages, date_of_issue, author_id))
        self.__conn.commit()

    def clear_data(self):
        self.__cursor.execute('DELETE FROM books')
        self.__cursor.execute('DELETE FROM author')
        self.__conn.commit()
        print("All data from author and books tables has been cleared.")

    def close(self):
        self.__conn.close()

    def __get_random_author_id(self):
        self.__cursor.execute('SELECT id FROM author')
        author_ids = self.__cursor.fetchall()
        if author_ids:
            return random.choice(author_ids)[0]
        else:
            return None
