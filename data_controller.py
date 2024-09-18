import sqlite3
import random


class DataController:
    def __init__(self):
        self.__conn = sqlite3.connect('author_books.sqlite3')  # Changed to _conn
        self.__cursor = self.__conn.cursor()  # Changed to _cursor
        self.create_tables()

    @property
    def cursor(self):
        return self.__cursor

    @property
    def conn(self):
        return self.__conn

    def create_tables(self):
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

    def close(self):
        self.__conn.close()

    def get_random_author_id(self):
        try:
            self.cursor.execute('SELECT id FROM author')
            author_ids = self.cursor.fetchall()
            if author_ids:
                return random.choice(author_ids)[0]
            else:
                return None
        except sqlite3.Error as e:
            print(f"Error fetching random author ID: {e}")
            return None


class DataWriter(DataController):
    def __init__(self):
        super().__init__()

    def insert_author(self, author):
        first_name, last_name, birth_date, birth_place = author.get_author_data()
        self.cursor.execute('''
               INSERT INTO author (first_name, last_name, birth_date, birth_place)
               VALUES (?, ?, ?, ?)
               ''', (first_name, last_name, birth_date, birth_place))
        self.conn.commit()

    def insert_book(self, book):
        name, category_name, number_of_pages, date_of_issue, author_id = book.get_book_data()
        self.cursor.execute('''
                INSERT INTO books (name, category_name, number_of_pages, date_of_issue, author_id)
                VALUES (?, ?, ?, ?, ?)
                ''', (name, category_name, number_of_pages, date_of_issue, author_id))
        self.conn.commit()

    def clear_data(self):
        self.cursor.execute('DELETE FROM books')
        self.cursor.execute('DELETE FROM author')
        self.conn.commit()


class DataAnalyzer(DataController):
    def __init__(self):
        super().__init__()

    def print_book_with_most_pages(self):
        try:
            self.cursor.execute('''
                SELECT * FROM books
                ORDER BY number_of_pages DESC
                LIMIT 1
            ''')
            book = self.cursor.fetchone()
            if book:
                column_names = [description[0] for description in self.cursor.description]
                print("Book with the most pages:")
                for col_name, value in zip(column_names, book):
                    print(f"{col_name}: {value}")
                print("************************************************")
            else:
                print("No books found.")
        except sqlite3.Error as e:
            print(f"Error fetching book with most pages: {e}")

    def print_average_number_of_pages(self):
        try:
            self.cursor.execute('''
                SELECT AVG(number_of_pages) FROM books
            ''')
            avg_pages = self.cursor.fetchone()[0]
            print(f"Average number of pages: {avg_pages:.2f}")
            print("************************************************")
        except sqlite3.Error as e:
            print(f"Error calculating average number of pages: {e}")

    def print_youngest_author(self):
        try:
            self.cursor.execute('''
                SELECT first_name, last_name FROM author
                ORDER BY birth_date DESC
                LIMIT 1
            ''')
            author = self.cursor.fetchone()
            if author:
                first_name, last_name = author
                print(f"Youngest author :{first_name} {last_name}")
                print("************************************************")
            else:
                print("No authors found.")
        except sqlite3.Error as e:
            print(f"Error fetching youngest author: {e}")

    def print_authors_without_books(self):
        try:
            self.cursor.execute('''
                SELECT a.id, a.first_name, a.last_name
                FROM author a
                LEFT JOIN books b ON a.id = b.author_id
                WHERE b.author_id IS NULL
            ''')
            authors = self.cursor.fetchall()
            if authors:
                print("Authors without books:")
                for author in authors:
                    author_id, first_name, last_name = author
                    print(f"ID: {author_id}, Author: {first_name} {last_name}")
                print("************************************************")
            else:
                print("All authors have books.")
        except sqlite3.Error as e:
            print(f"Error fetching authors without books: {e}")

    def print_authors_with_more_than_3_books(self):
        try:
            self.cursor.execute('''
                SELECT a.id, a.first_name, a.last_name, COUNT(b.id) as book_count
                FROM author a
                JOIN books b ON a.id = b.author_id
                GROUP BY a.id
                HAVING COUNT(b.id) > 3
                LIMIT 5
            ''')
            authors = self.cursor.fetchall()

            if authors:
                print("Authors with more than 3 books (limited to 5):")
                for author in authors:
                    author_id, first_name, last_name, book_count = author
                    print(f"Author: {first_name} {last_name}, Number of Books: {book_count}")
                print("************************************************")
            else:
                print("No authors with more than 3 books found.")
        except sqlite3.Error as e:
            print(f"Error fetching authors with more than 3 books: {e}")
