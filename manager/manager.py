# Gerencia a compra e venda de ingressos dentro das diversas franquias

from xmlrpc.client import Boolean
from content.movie import Movie

class Ticket:
    def __init__(self, identifier: int, movie: Movie):
        self.movie = movie
        self.identifier = identifier

    def get_movie(self) -> Movie:
        return self.movie


class Cashier:
    def __init__(self):
        self.i = 0
        self.money_amount = 0.0
        self.sold_tickets = list()

    def sell(self, price: float, movie: Movie) -> Ticket:
        ticket = Ticket(self.i, movie)

        self.money_amount += price
        self.sold_tickets.append(ticket)
        self.i += 1

        return ticket

    def validate(self, ticket) -> Boolean:
        '''valida um ticket e remove ele da lista de tickets'''
        if ticket in self.sold_tickets :
            self.sold_tickets.remove(ticket)
            return True
        return False