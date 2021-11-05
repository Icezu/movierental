import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceStrategy


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Mulan")
        self.regular_movie = Movie("CitizenFour")
        self.childrens_movie = Movie("Frozen")

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("CitizenFour")
        self.assertEqual("CitizenFour", m.get_title())

    # def test_rental_price(self):
    #     """Tests of rental price."""
    #     # for new movie
    #     rental = Rental(self.new_movie, 1, )
    #     self.assertEqual(rental.get_price(), 3.0)
    #     rental = Rental(self.new_movie, 5)
    #     self.assertEqual(rental.get_price(), 15.0)
    #     # For regular
    #     rental = Rental(self.regular_movie, 1)
    #     self.assertEqual(rental.get_price(), 2)
    #     rental = Rental(self.regular_movie, 5)
    #     self.assertEqual(rental.get_price(), 6.5)
    #     # for children
    #     rental = Rental(self.childrens_movie, 1)
    #     self.assertEqual(rental.get_price(), 1.5)
    #     rental = Rental(self.childrens_movie, 5)
    #     self.assertEqual(rental.get_price(), 4.5)

    # def test_rental_points(self):
    #     """Tests rent points."""
    #     # For new movie
    #     rental = Rental(self.new_movie, 1)
    #     self.assertEqual(rental.get_rental_point(), 1)
    #     rental = Rental(self.new_movie, 5)
    #     self.assertEqual(rental.get_rental_point(), 5)
    #     # for regular
    #     rental = Rental(self.regular_movie, 1)
    #     self.assertEqual(rental.get_rental_point(), 1)
    #     rental = Rental(self.regular_movie, 3)
    #     self.assertEqual(rental.get_rental_point(), 1)
    #     # for children
    #     rental = Rental(self.childrens_movie, 2)
    #     self.assertEqual(rental.get_rental_point(), 1)
    #     rental = Rental(self.childrens_movie, 4)
    #     self.assertEqual(rental.get_rental_point(), 1)
