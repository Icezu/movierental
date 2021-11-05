import csv
from movie import Movie


class MovieCatalog:
    """Factory for Movie."""

    def __init__(self):
        self.movies = []
        with open("movies.csv", "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            list_of_rows = list(csv_reader)
            for row in range(1, len(list_of_rows)):
                collect_title = list_of_rows[row][1]
                collect_year = list_of_rows[row][2]
                collect_genre = list_of_rows[row][3].split("|")
                self.movies.append(Movie(collect_title, collect_year, collect_genre))

    def get_movie(self, title: str):
        """Returns a movie with matching title."""
        for movie in self.movies:
            if title == movie.get_title():
                return movie
