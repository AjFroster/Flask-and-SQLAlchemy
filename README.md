Flask and SQLite Book Collection App
Description

This project serves as an introduction to using Flask with SQLite. It's a simple web application for managing a collection of books. Users can add new books to the collection and view the existing ones. The application utilizes Flask for the backend and SQLite as the database.

Features

    Add New Books: Users can input book details like title, author, and rating.
    View Book Collection: A list of all books in the database is displayed.

Installation

    Clone the Repository:

    bash

    git clone [repository-url]

Install Dependencies:

    pip install -r requirements.txt

    Set Up the Database:
        The application uses SQLite, which is integrated with Flask-SQLAlchemy.

Usage

To run the application:

python main.py

The application will be accessible through your web browser at localhost:5000.

How it Works

    Backend Framework: Flask.
    Database: SQLite, integrated through SQLAlchemy.