# Gerencia a compra e venda de ingressos dentro das diversas franquias
from content.movie import Movie


class Ticket:
    def __init__(self, identifier: int, movie: Movie):
        self.movie = movie
        self.identifier = identifier

    def get_movie_from_ticket(self) -> Movie:
        return self.movie


class FranchiseManager:

    price_tags = [24.00, 35.99]

    def __init__(self):
        self.money_amount = 0.0
        self.sold_tickets = list()

    def get_price(self, movie: Movie) -> float:
        return self.price_tags[movie.age_restricted] * (movie.duration // 3)

    def sell(self, identifier: int, price: float, movie: Movie) -> Ticket:
        ticket = Ticket(identifier, movie)
        
        self.money_amount += price
        self.sold_tickets.append(ticket)

        return ticket

    def validate(self, ticket) -> bool:
        if ticket in self.sold_tickets :
            self.sold_tickets.remove(ticket)
            return True
        return False
