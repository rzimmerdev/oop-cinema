# Classe para instanciar diversos tipos de franquias
# franquia guarda os filmes, o filme atual e os ingressos
from content.generator import MovieManager
from interface.factory import ViewFactory
from franchise.store import Cashier, Ticket


class FranchiseFactory:
    def __init__(self, name: str, opening_year: int):
        self.name = name
        self.opening_year = opening_year

        self.movie_manager = MovieManager()
        self.cashier = Cashier()

        self.facade = ViewFactory(self, self.movie_manager, self.cashier, name)

        self.current_movie = None

    def sell_ticket(self, identifier: int, price: float):
        ticket = self.cashier.sell(identifier, price, self.movie_manager.get(identifier))
        self.play_movie(ticket)

    def add_review(self, identifier: int, rate: float, comment: str):
        self.movie_manager.get(identifier).add_rating(rate, comment)
        self.facade.show_movies(self.movie_manager.get())

    def play_movie(self, ticket: Ticket):
        if self.cashier.validate(ticket):
            self.current_movie = ticket.movie
            self.facade.show_src(ticket.movie.filename, "files/films/")
            self.facade.show_review(ticket.movie)
        else:
            raise Exception("Invalid Ticket")

    def add_movie(self, identifier, name, filename, description, start_time, duration,
                  thumbnail, age_restricted=None) -> None:
        self.movie_manager.new_movie(identifier, name, filename, description, start_time, duration,
                                     thumbnail, age_restricted)
        self.facade.show_movies(self.movie_manager.get())

    def remove_movie(self, name: str) -> None:
        self.movie_manager.remove(name)
        self.facade.show_movies()

    def show(self):
        self.facade.show_movies(self.movie_manager.get())
        self.facade.show()


class PrivateFranchise(FranchiseFactory): 
    def __init__(self, name: str, opening_year: int):
        super().__init__(name, opening_year)


class PublicFranchise(FranchiseFactory):
    def __init__(self, name: str, opening_year: int):
        super().__init__(name, opening_year)
