import sqlite3
import random


class DataController:
    def __init__(self):
        try:
            self.__conn = sqlite3.connect('author_books.sqlite3')
            self.__cursor = self.__conn.cursor()
            self.__create_tables()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise

    def __create_tables(self):
        try:
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
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
            raise

    def insert_author(self, author):
        try:
            first_name, last_name, birth_date, birth_place = author.get_author_data()
            self.__cursor.execute('''
                   INSERT INTO author (first_name, last_name, birth_date, birth_place)
                   VALUES (?, ?, ?, ?)
                   ''', (first_name, last_name, birth_date, birth_place))
            self.__conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting author: {e}")
            self.__conn.rollback()

    def insert_book(self, book):
        try:
            name, category_name, number_of_pages, date_of_issue, author_id = book.get_book_data()
            if not self.__author_exists(author_id):
                print(f"Author ID {author_id} does not exist.")
                return
            self.__cursor.execute('''
                    INSERT INTO books (name, category_name, number_of_pages, date_of_issue, author_id)
                    VALUES (?, ?, ?, ?, ?)
                    ''', (name, category_name, number_of_pages, date_of_issue, author_id))
            self.__conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting book: {e}")
            self.__conn.rollback()

    def __author_exists(self, author_id):
        self.__cursor.execute('SELECT 1 FROM author WHERE id = ?', (author_id,))
        return self.__cursor.fetchone() is not None

    def clear_data(self):
        try:
            self.__cursor.execute('DELETE FROM books')
            self.__cursor.execute('DELETE FROM author')
            self.__conn.commit()
        except sqlite3.Error as e:
            print(f"Error clearing data: {e}")
            self.__conn.rollback()

    def get_random_author_id(self):
        try:
            self.__cursor.execute('SELECT id FROM author')
            author_ids = self.__cursor.fetchall()
            if author_ids:
                return random.choice(author_ids)[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error fetching author IDs: {e}")
            return None

    def close(self):
        self.__conn.close()
