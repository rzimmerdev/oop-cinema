# Gerencia a compra e venda de ingressos dentro das diversas franquias
from content.movie import Movie


class Ticket:
    def __init__(self, movie: Movie):
        self.movie = movie

    def get_movie_from_ticket(self) -> Movie:
        return self.movie


class Cashier:
    price_tags = [24.00, 35.99]

    def __init__(self):
        self.money_amount = 0.0
        self.sold_tickets = list()

    def get_price(self, movie: Movie) -> float:
        return self.price_tags[movie.age_restricted] * (movie.duration / 100) / 2

    def sell(self, movie: Movie) -> Ticket:
        ticket = Ticket(movie)

        self.money_amount += self.get_price(movie)
        self.sold_tickets.append(ticket)

        return ticket

    def validate(self, ticket) -> bool:
        if ticket in self.sold_tickets:
            self.sold_tickets.remove(ticket)
            return True
        return False
