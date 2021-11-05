from movie import *


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie, days_rented, price_code):
        """
        Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    def get_price_code(self):
        """Get the price code."""
        return self.price_code

    def get_movie(self):
        """Return movie."""
        return self.movie

    def get_days_rented(self):
        """Return days_rented."""
        return self.days_rented

    def get_price(self):
        """Calculate the price of each rental."""
        amount = self.get_movie().get_price_code().price(self.get_days_rented())
        return amount

    def get_rental_point(self):
        """Calculate movie rental point."""
        points = self.get_movie().get_price_code().points(self.get_days_rented())
        return points
