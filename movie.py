from enum import Enum


class PriceStrategy(Enum):
    """An enumeration for different kinds of movies and their behavior."""
    RegularPrice = {"price": lambda days: 2 if days <= 2 else 2 + (1.5 * (days - 2)),
                    "frp": lambda days: 1}
    NewReleasePrice = {"price": lambda days: 3.0 * days,
                       "frp": lambda days: days}
    ChildrensPrice = {"price": lambda days: 1.5 if days <= 3 else 1.5 + (1.5 * (days - 3)),
                      "frp": lambda days: 1}

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days."""
        pricing = self.value["price"]   # the enum member's price formula
        return pricing(days)

    def points(self, days: int):
        """Return the rental points for a given number of days."""
        point = self.value["frp"]   # the enum member's point formula
        return point(days)


class Movie:
    """
    A movie available for rent.
    """
    def __init__(self, title, price_code):
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        """Get the price code."""
        return self.price_code

    def get_title(self):
        """Get movie title."""
        return self.title

    def __str__(self):
        return self.title

