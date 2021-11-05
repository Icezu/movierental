import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from price_strategy import PriceStrategy


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("No Time To Die", "2021", ["Adventure"])
        self.regular_movie = Movie("CitizenFour", "1996", ["Action", "Sci-Fi", "Thriller"])
        self.childrens_movie = Movie("The Legend of Sarila", "2013", ["Adventure", "Animation", "Children"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        # New Movie
        self.assertEqual("No Time To Die", self.new_movie.get_title())
        self.assertEqual("2021", self.new_movie.get_year())
        self.assertEqual(PriceStrategy.NewReleasePrice, PriceStrategy.for_movie(self.new_movie))
        self.assertEqual(True, self.new_movie.is_genre("Adventure"))
        # Regular Movie
        self.assertEqual("CitizenFour", self.regular_movie.get_title())
        self.assertEqual("1996", self.regular_movie.get_year())
        self.assertEqual(PriceStrategy.RegularPrice, PriceStrategy.for_movie(self.regular_movie))
        self.assertEqual(True, self.regular_movie.is_genre("Sci-Fi"))
        # Children Movie
        self.assertEqual("The Legend of Sarila", self.childrens_movie.get_title())
        self.assertEqual("2013", self.childrens_movie.get_year())
        self.assertEqual(PriceStrategy.ChildrensPrice, PriceStrategy.for_movie(self.childrens_movie))
        self.assertEqual(True, self.childrens_movie.is_genre("Children"))

    def test_rental_price(self):
        """Tests of rental price."""
        # for new movie
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)
        # For regular
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2)
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)
        # for children
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 5)
        self.assertEqual(rental.get_price(), 4.5)

    def test_rental_points(self):
        """Tests rent points."""
        # For new movie
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_rental_point(), 1)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_rental_point(), 5)
        # for regular
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_rental_point(), 1)
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_rental_point(), 1)
        # for children
        rental = Rental(self.childrens_movie, 2)
        self.assertEqual(rental.get_rental_point(), 1)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_rental_point(), 1)
