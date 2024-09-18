from data_controller import DataAnalyzer, DataWriter
import random

from random_helper import RandomHelper


def main():
    data_writer = DataWriter()
    data_writer.clear_data()


    author_ids = []
    for _ in range(500):
        author = RandomHelper.get_random_author()
        data_writer.insert_author(author)
        author_id = data_writer.get_random_author_id()
        if author_id:
            author_ids.append(author_id)

    for _ in range(1000):
        author_id = random.choice(author_ids)
        book = RandomHelper.get_random_book(author_id)
        data_writer.insert_book(book)

    data_writer.close()

    data_analyzer = DataAnalyzer()
    data_analyzer.print_book_with_most_pages()
    data_analyzer.print_average_number_of_pages()
    data_analyzer.print_youngest_author()
    data_analyzer.print_authors_without_books()
    data_analyzer.print_authors_with_more_than_3_books()

    data_analyzer.close()


if __name__ == "__main__":
    main()
