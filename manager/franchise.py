# Classe para instanciar diversos tipos de franquias
# franquia guarda os filmes, o filme atual e os ingressos

from content.movie import *
from content.generator import *
from interface.view import ViewFactory
from manager.manager import *

class FranchiseFactory:
    def __init__(self, name: str, opening_year: int):
        self.name = name
        self.opening_year = opening_year

        self.cinema = ViewFactory(name)
        self.movie_scheduler = MovieScheduler()
        self.cashier = Cashier()
        self.current_movie = None

    def sell_ticket(self, price: float, movie_name: str) -> Ticket:
        '''recebe info e vende um ticket'''
        return self.cashier.sell(price, self.movie_scheduler.get(movie_name))

    def validate_ticket_and_play_film(self, ticket: Ticket) -> None:
        '''recebe um ingresso e se for validado com sucesso da play no filme'''
        if self.cashier.validate(ticket):
            movie = ticket.get_movie_from_ticket()
            self.current_movie = movie
            self.cinema.play_src(movie.filename, "films/")

    def add_movie(self, name, filename, description, start_time, duration, thumbnail, age_restricted) -> None:
        '''adiciona um filme e atualiza a interface grafica'''
        self.movie_scheduler.add(name, name, filename, description, start_time, duration, thumbnail, age_restricted)
        self.cinema.show_movies()
        self.cinema.show()
        
    def remove_movie(self, name: str) -> None:
        '''adiciona um filme e atualiza a interface grafica'''
        self.movie_scheduler.remove(name)
        self.cinema.show_movies()
        self.cinema.show()


class PrivateFranchise(FranchiseFactory): 
    pass


class PublicFranchise(FranchiseFactory):
    pass


def main():
    cine = FranchiseFactory("Cineplex", 1999)

    cine.add_movie("Minions: Rise of Gru", "water.mkv",
                    "In the 1970s, young Gru tries to join a group of supervillains, "
                    "called the Vicious 6 after they oust their leader",
                    1071, 141, thumbnail="minions.jpg", age_restricted=False)

    cine.add_movie("Despicable Me 3", "water.mkv",
                    "Gru meets his long-lost twin brother Dru, after getting fired from the Anti-Villain League.",
                    842, 155, thumbnail="gru.jpg", age_restricted=False)

    cine.add_movie("Minions: Rise of Gru", "water.mkv",
                    "In the 1970s, young Gru tries to join a group of supervillains, "
                    "called the Vicious 6 after they oust their leader",
                    1071, 141, thumbnail="minions.jpg", age_restricted=False)

    cine.add_movie("Minions: Rise of Gru", "water.mkv",
                    "In the 1970s, young Gru tries to join a group of supervillains, "
                    "called the Vicious 6 after they oust their leader",
                    1071, 141, thumbnail="minions.jpg", age_restricted=False)

    ticket = cine.sell_ticket(32.85, "Despicable Me 3")

    cine.validate_ticket_and_play_film(ticket)

if __name__ == "__main__":
    main()