class Author:
    def __init__(self, first_name, last_name, birth_date, birth_place):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__birth_place = birth_place

    def get_author_data(self):
        return (self.__first_name, self.__last_name, self.__birth_date, self.__birth_place)


class Book:
    def __init__(self, name, category_name, number_of_pages, date_of_issue, author_id):
        self.__name = name
        self.__category_name = category_name
        self.__number_of_pages = number_of_pages
        self.__date_of_issue = date_of_issue
        self.__author_id = author_id

    def get_book_data(self):
        return (self.__name, self.__category_name, self.__number_of_pages, self.__date_of_issue, self.__author_id)