# Classe para instanciar diversos tipos de franquias
# franquia guarda os filmes, o filme atual e os ingressos
from content.generator import MovieScheduler
from manager.manager import Cashier, Ticket


class FranchiseFactory:
    def __init__(self, name: str, opening_year: int):
        self.name = name
        self.opening_year = opening_year
        
        #instanciando o objeto responsavel pelo filmes
        self.movie_scheduler = MovieScheduler()

        #instanciando a cashier, responsavel pelos tickets
        self.cashier = Cashier()
        self.current_movie = None

    def sell_ticket(self, identifier: int, price: float):
        """
        Vende um ticket
        """
        ticket = self.cashier.sell(identifier, price, self.movie_scheduler.get(identifier))
        self.play_movie(ticket)

    def play_movie(self, ticket: Ticket):
        """
        Recebe um ticket e, se for validado com sucesso, da play no filme
        """
        if self.cashier.validate(ticket):
            self.current_movie = ticket.movie
            #self.facade.play_src(ticket.movie.filename, "files/films/")
            #self.facade.show_review(ticket.movie)
        else:
            raise Exception("Invalid Ticket")

    def add_movie(self, identifier: int, name: str, filename: str, description: str, start_time: int, duration: int,
                 thumbnail: str = None, director: str = None, age_restricted: bool = False) -> None:
        """
        Adiciona um filme e atualiza a interface grafica
        """
        self.movie_scheduler.add(identifier, name, filename, description, start_time, duration, thumbnail, director, age_restricted)
        
    def remove_movie(self, name: str) -> None:
        """
        Remove um filme e atualiza a interface grafica
        """
        self.movie_scheduler.remove(name)

    #def show(self):
    #    """
    #    Abre a interface grafica
    #    """
    #    self.facade.show()


class PrivateFranchise(FranchiseFactory): 
    def __init__(self, name: str, opening_year: int):
        super().__init__(name, opening_year)


class PublicFranchise(FranchiseFactory):
    def __init__(self, name: str, opening_year: int):
        super().__init__(name, opening_year)
