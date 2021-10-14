# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, PriceStrategy
from rental import Rental
from customer import Customer


def make_movies():
    movies = [
        Movie("The Irishman", PriceStrategy.NewReleasePrice),
        Movie("CitizenFour", PriceStrategy.RegularPrice),
        Movie("Frozen", PriceStrategy.ChildrensPrice),
        Movie("El Camino", PriceStrategy.NewReleasePrice),
        Movie("Particle Fever", PriceStrategy.RegularPrice)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
