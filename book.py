class Book:
    """
    A class for representing books that includes

      - book_id: a public attribute for the book's a unique identifier
      - title - a public attribute for the book's title
      - author_name - a public attribute for the book's author

    See below for public methods.
    """

    def __init__(self, book_id: str, author_name: str, 
                 title: str, keywords: list[str]) -> None:
        """
        Create an instance of the Book class.

        Inputs:
          book_id: a unique identifier for the book
          author_name: the author's name
          title: the book's title
          keywords: a list of keywords that
              describe the book.
        """
        self.book_id = book_id
        self.author_name = author_name
        self.title = title
        self.__keywords = set(keywords)


    def matches_keyword(self, keyword: str) -> bool:
        """
        Is the specified keyword associated with this book?

        Input:

            keyword: the keyword to check

        Returns:

            Returns True, if the keyword in the set of keywords
            associated with the book and False, otherwise.

        """
        return keyword in self.__keywords

    def __str__(self) -> str:
        s = (f"{self.book_id}: {self.title} by {self.author_name}"
             f"{', '.join(self.__keywords)}")
        return s

    def __repr__(self) -> str:
        return str(self)