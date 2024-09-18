from data_controller import DataController
import random

from random_helper import RandomHelper


def main():
    data_controller = DataController()
    data_controller.clear_data()

    author_ids = []
    for _ in range(500):
        author = RandomHelper.get_random_author()
        data_controller.insert_author(author)

        author_id = data_controller.get_random_author_id()
        if author_id:
            author_ids.append(author_id)

    for _ in range(1000):
        author_id = random.choice(author_ids)
        book = RandomHelper.get_random_book(author_id)
        data_controller.insert_book(book)

    data_controller.close()


if __name__ == "__main__":
    main()
