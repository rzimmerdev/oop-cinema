from content.generator import MovieManager
from interface.factory import ViewFactory
from franchise.store import Cashier, Ticket


class FranchiseFactory:
    def __init__(self, name: str, opening_year: int) -> None:
        self.name = name
        self.opening_year = opening_year

        self.movie_manager = MovieManager()
        self.cashier = Cashier()

        self.facade = ViewFactory(self, self.movie_manager, self.cashier, name)
        self.current_movie = None

    def sell_ticket(self, identifier: int) -> None:
        """Sell a ticket to a movie and calls play_movie()

        Args:
            identifier (int): movies identifier
        """
        ticket = self.cashier.sell(self.movie_manager.get(identifier))
        self.play_movie(ticket)

    def add_review(self, identifier: int, rate: float, comment: str) -> None:
        """Add a review to a movie
        
        Args:
            identifier (int): movies identifier
            rate (float) - float in range [0, 5]
            comment (str): comment regarding the rating
        """
        self.movie_manager.get(identifier).add_rating(rate, comment)
        self.facade.show_movies(self.movie_manager.get())

    def play_movie(self, ticket: Ticket):
        """Validate a ticket and play a movie
        
        Args:
            ticket (obj: Ticket): ticket to a movie

        Raises:
            Exception: invalid ticket
        """
        if self.cashier.validate(ticket):
            self.current_movie = ticket.movie
            self.facade.show_src(ticket.movie.filename, "files/films/")
            self.facade.show_review(ticket.movie)
        else:
            raise Exception("Invalid Ticket")

    def add_movie(self, identifier, name, filename, description, start_time, duration,
                  thumbnail, age_restricted=False) -> None:
        """Add a Movie to scheduler"""
        self.movie_manager.new_movie(identifier, name, filename, description, start_time, duration,
                                     thumbnail, age_restricted)
        self.facade.show_movies(self.movie_manager.get())

    def remove_movie(self, name: str) -> None:
        """Remove a movie from scheduled movies
        
        Args:
            name (str): movies name
        """
        self.movie_manager.remove(name)
        self.facade.show_movies()

    def show(self):
        """Displays interface window"""
        self.facade.show_movies(self.movie_manager.get())
        self.facade.show()


class PrivateFranchise(FranchiseFactory): 
    def __init__(self, name: str, opening_year: int):
        super().__init__(name, opening_year)


class PublicFranchise(FranchiseFactory):
    def __init__(self, name: str, opening_year: int):
        super().__init__(name, opening_year)
