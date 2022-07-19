# Classe para instanciar diversos tipos de franquias
# franquia guarda os filmes, o filme atual e os ingressos

#from content.movie import Movie
from content.generator import MovieScheduler
from interface.view import ViewFactory
from manager.manager import Cashier, Ticket

class FranchiseFactory:
    def __init__(self, name: str, opening_year: int):
        self.name = name
        self.opening_year = opening_year

        self.facade = ViewFactory(self, name)
        
        self.movie_scheduler = MovieScheduler()
        self.cashier = Cashier()
        self.current_movie = None

    def export_franchise(self):
        return [self.name, self.opening_year]

    def sell_ticket(self, identifier: int, price: float, movie_name: str,) -> Ticket:
        '''recebe info e vende um ticket'''
        return self.cashier.sell(identifier, price, self.movie_scheduler.get(movie_name))

    def play_movie(self, ticket: Ticket):
        if self.cashier.validate(ticket):
            self.current_movie = ticket.movie
            self.facade.play_src(ticket.movie.filename, "films/")
        else:
            raise Exception("Invalid Ticket")

    def add_movie(self, name, filename, description, start_time, duration, thumbnail, age_restricted) -> None:
        '''adiciona um filme e atualiza a interface grafica'''
        self.movie_scheduler.add(name, filename, description, start_time, duration, thumbnail, age_restricted)
        self.facade.show_movies(self.movie_scheduler.scheduled_movies)
        
    def remove_movie(self, name: str) -> None:
        '''remove um filme e atualiza a interface grafica'''
        self.movie_scheduler.remove(name)
        self.facade.show_movies()

    def show(self):
        self.facade.show()

class PrivateFranchise(FranchiseFactory): 
    def __init__(self, name: str, opening_year: int):
        super().__init__(name, opening_year)


class PublicFranchise(FranchiseFactory):
    def __init__(self, name: str, opening_year: int):
        super().__init__(name, opening_year)
