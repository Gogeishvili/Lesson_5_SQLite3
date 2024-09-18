from faker import Faker
from models import Author, Book

fake = Faker()


class RandomHelper:
    @staticmethod
    def get_random_author():
        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
        birth_place = fake.city()
        return Author(first_name, last_name, birth_date, birth_place)

    @staticmethod
    def get_random_book(author_id):
        name = fake.sentence(nb_words=3)
        category_name = fake.word()
        number_of_pages = fake.random_int(min=50, max=1000)
        date_of_issue = fake.date_this_century()
        return Book(name, category_name, number_of_pages, date_of_issue, author_id)



