# Gerencia a compra e venda de ingressos dentro das diversas franquias

from movie import Movie
from random import randint

class Ticket:
    def __init__(self, identifier, barcode):
        self.identifier = identifier
        self.barcode = barcode


class Cashier:
    def __init__(self):
        self.sold_tickets = list()

    def sell(self, card_number: int, cardholder_name: str, cvc: int, buyers_name: str, buyers_id: int):
        self.sold_tickets.append(Ticket(len(self.sold_tickets), randint(0,100000)))

    def validate(self, ticket):
        if ticket in self.sold_tickets :
            return True
        return False