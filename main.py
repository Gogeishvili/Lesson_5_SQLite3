from data_controller import DataController


def main():
    data_controller = DataController()
    data_controller.clear_data()
    # Insert authors
    data_controller.insert_author("Giorgi", "Gogeishvili", "1989-01-01", "Samtredia")
    data_controller.insert_author("John", "Doe", "1975-03-15", "New York")

    # Insert a book (random author ID is selected)
    data_controller.insert_book("The Mysterious Journey", "Fantasy", 350, "2022-07-20")
    data_controller.insert_book("The Silent Moon", "Thriller", 280, "2021-11-15")

    # Close the connection
    data_controller.close()


if __name__=="__main__":
    main()