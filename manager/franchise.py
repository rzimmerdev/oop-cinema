# Classe para instanciar diversos tipos de franquias
# franquia guarda os filmes, o filme atual e os ingressos

from content.generator import MovieScheduler
from interface.view import ViewFactory
from manager.manager import Cashier, Ticket


class FranchiseFactory:
    def __init__(self, name: str, opening_year: int):
        self.name = name
        self.opening_year = opening_year

        self.cinema = ViewFactory(name)
        self.cinema.show()
        self.movie_scheduler = MovieScheduler()
        self.cashier = Cashier()
        self.current_movie = None

    def sell_ticket(self, price: float, movie_name: str) -> Ticket:
        """recebe info e vende um ticket"""
        return self.cashier.sell(price, self.movie_scheduler.get(movie_name))

    def play_movie(self, ticket: Ticket):
        if self.cashier.validate(ticket):
            self.cinema.play_src(ticket.movie.filename, "films/")
        else:
            raise Exception("Invalid Ticket")

    def add_movie(self, name, filename, description, start_time, duration, thumbnail, director=None, age_restricted=None) -> None:
        """adiciona um filme e atualiza a interface grafica"""
        self.movie_scheduler.add(name, filename, description, start_time, duration, thumbnail, director, age_restricted)
        self.cinema.show_movies(self.movie_scheduler.scheduled_movies)

    def remove_movie(self, name: str) -> None:
        """adiciona um filme e atualiza a interface grafica"""
        self.movie_scheduler.remove(name)
        self.cinema.show_movies(self.movie_scheduler.scheduled_movies)


class PrivateFranchise(FranchiseFactory):
    pass


class PublicFranchise(FranchiseFactory):
    pass
