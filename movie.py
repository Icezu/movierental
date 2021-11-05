class Movie:
    """
    A movie available for rent.
    """
    def __init__(self, title, year, genre: list):
        self.__title = title
        self.__year = year
        self.__genre = genre

    def is_genre(self, same_genre):
        """Returns True if same_genre matches one of the movie genre"""
        return same_genre in self.__genre

    def get_title(self):
        """Get movie title."""
        return self.__title

    def get_year(self):
        """Get movie year."""
        return self.__year

    def __str__(self):
        return self.__title

