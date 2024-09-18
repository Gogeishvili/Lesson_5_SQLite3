# Author and Book Management System

## Overview

This project provides a basic implementation of a database management system for authors and books using SQLite. It includes functionalities for adding authors and books, clearing data, and performing various analyses.

## Project Structure

- **main.py**: The entry point for the application. It demonstrates how to use `DataWriter` and `DataAnalyzer` classes.
- **models.py**: Contains the `Author` and `Book` classes.
  - `Author`: Represents an author with fields for first name, last name, birth date, and birth place.
  - `Book`: Represents a book with fields for name, category, number of pages, date of issue, and associated author ID.
- **data_controller.py**: Contains the database management classes.
  - `DataController`: Manages the database connection and table creation.
  - `DataWriter`: Inherits from `DataController` and handles data insertion and clearing.
  - `DataAnalyzer`: Inherits from `DataController` and performs data analysis and reporting.

## Features

- **DataWriter**:
  - `insert_author(author)`: Inserts a new author into the database.
  - `insert_book(book)`: Inserts a new book into the database.
  - `clear_data()`: Clears all data from the database.

- **DataAnalyzer**:
  - `print_book_with_most_pages()`: Prints details of the book with the most pages, including all column names and their values.
  - `print_average_number_of_pages()`: Prints the average number of pages across all books.
  - `print_youngest_author()`: Prints the first and last name of the youngest author.
  - `print_authors_without_books()`: Prints the ID, first name, and last name of authors who do not have any books.
  - `print_authors_with_more_than_3_books()`: Prints the ID, first name, last name, and book count of up to 5 authors who have more than 3 books.



## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Functionality**:
    - **Clearing existing data**: Use `DataWriter.clear_data()` to delete all data from the database.
    - **Inserting random authors and books**: Use `DataWriter.insert_author(author)` and `DataWriter.insert_book(book)` to add new records.
    - **Performing data analysis**: Use `DataAnalyzer` methods to generate reports and insights from the database.

## Requirements

- Python 3.x
- sqlite3 (included with Python)
- Faker (install using `pip install faker`)


