import sys

class Book:
    def __init__(self, title, page_count, year=None):
        self.title = title
        self.page_count = page_count
        self.year = year if year is not None else "Unknown"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Title must be a non-empty string.")
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __str__(self):
        return f"{self.title}, {self.page_count} pages, published in {self.year}"
