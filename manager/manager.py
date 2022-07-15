# Gerencia a compra e venda de ingressos dentro das diversas franquias

from content.movie import Movie

class Ticket:
    def __init__(self, identifier: int, movie: Movie):
        self.movie = movie
        self.identifier = identifier

    def get_movie_from_ticket(self) -> Movie:
        '''recupera o filme do ticket'''
        return self.movie


class Cashier:
    def __init__(self):
        self.money_amount = 0.0
        self.sold_tickets = list()

    def sell(self, identifier: int, price: float, movie: Movie) -> Ticket:
        '''vende um ticket e adiciona aos tickets vendidos'''
        ticket = Ticket(identifier, movie)
        
        self.money_amount += price
        self.sold_tickets.append(ticket)

        return ticket

    def validate(self, ticket) -> bool:
        '''valida um ticket e remove ele dos tickets vendidos'''
        if ticket in self.sold_tickets :
            self.sold_tickets.remove(ticket)
            return True
        return False