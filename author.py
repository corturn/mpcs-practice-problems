from book import Book

class Author:
    """
    A class for representing authors that includes:

      - name - a public attribute the name of the author

    See below for public methods.
    """

    def __init__(self, name: str):
        """
        Create an instance of Author

        Input:
            name: the name of the author
        """
        self.name = name
        self.__books = []


    def add_book(self, book_id: str, title: str, keywords: list[str]) -> bool:
        """
        If the author does not already have a book by that title,
        it adds a Book to the list and returns true.  If the author
        already has a book by that title, it simply returns False.

        Inputs:
            book_id: a unique identifier for the book
            title: the book's title
            keywords: a list of keywords that describe the book.

        Returns: return True if the book was added to the list
          and False otherwise.

        """
        for book in self.__books:
            if title == book.title:
                return False
        new_book = Book(book_id, self.name, title, keywords)
        self.__books.append(new_book)
        return True


    def find_matches(self, keywords: list[str]) -> list[Book]:
        """
        Find the books that match all words in the keywords list.
        
        Input:
            keywords: the keywords to match

        Returns: a list of the books that match
            all the keywords.
        """
        matches = []
        for book in self.__books:
            if all(book.matches_keyword(keyword) for keyword in keywords):
                matches.append(book)
        return matches
