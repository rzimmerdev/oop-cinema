# Gera conteudo para os diferentes filmes a serem colocados em cartaz,
# como arquivo de video MP4, descricao, etc.
# Sera usado como conexao com o módulo do :lib:‘manager’.
from typing import List, Optional, Union
from interface.view import ViewFactory
from content.movie import Movie


class MovieScheduler:
    def __init__(self):
        self.scheduled_movies: List[Movie] = list()

    def add(self, identifier, name, filename, description, start_time, duration,
            thumbnail, director=None, age_restricted=None):

        new_movie = Movie(identifier, name, filename, description, start_time, duration,
                          thumbnail, director, age_restricted)
        self.scheduled_movies.append(new_movie)

    def remove(self, name: str):
        self.scheduled_movies = [movie for movie in self.scheduled_movies if movie.name != name]

    def get(self, identifier: int = None, name: str = None) -> Union[List[Movie], Movie, None]:
        for movie in self.scheduled_movies:
            if movie.identifier == identifier:
                return movie
        for movie in self.scheduled_movies:
            if movie.name == name:
                return movie
        return self.scheduled_movies


class MovieManager:
    def __init__(self, movie: Movie, cinema: ViewFactory):
        self.movie = movie
        self.cinema = cinema

    def update(self, movie: Movie):
        self.movie = movie

    def play(self):
        self.cinema.show_src(self.movie.filename, "files/films/")

