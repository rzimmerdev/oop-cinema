# Gerencia a compra e venda de ingressos dentro das diversas franquias
from content.movie import Movie


class Ticket:
    def __init__(self, movie: Movie):
        self.movie = movie

    def get_movie_from_ticket(self) -> Movie:
        """Get the movie from a ticket
        
        Returns:
            (obj: Movie): movie
        """
        return self.movie


class Cashier:
    price_tags = [24.00, 35.99]

    def __init__(self):
        self.money_amount = 0.0
        self.sold_tickets = list()

    def get_price(self, movie: Movie) -> float:
        """Get ticket price
        
        Args:
            movie (obj: Movie): movie to get the price

        Return:
            float: ticket price
        """
        return self.price_tags[movie.age_restricted] * (movie.duration / 100) / 2

    def sell(self, movie: Movie) -> Ticket:
        """Sell a ticket to a movie and add it to the sold tickets
        
        Args:
            movie (obj: Movie): movie
        
        Returns:
            (obj: Ticket): sold ticket
        """
        ticket = Ticket(movie)

        self.money_amount += self.get_price(movie)
        self.sold_tickets.append(ticket)

        return ticket

    def validate(self, ticket: Ticket) -> bool:
        """Validate a ticket and remove it from the sold tickets
        
        Args:
            ticket (Ticket): ticket to validate
        Returns:
            bool: True if successful, False otherwise.
        """
        if ticket in self.sold_tickets:
            self.sold_tickets.remove(ticket)
            return True
        return False
