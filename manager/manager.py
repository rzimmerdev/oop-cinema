# Gerencia a compra e venda de ingressos dentro das diversas franquias

class Ticket:
    def __init__(self, identifier, barcode=None):
        self.identifier = identifier
        self.barcode = barcode


class Cashier:
    def __init__(self):
        self.sold_tickets = list()

    def sell(self):
        pass

    def validate(self, ticket):
        pass