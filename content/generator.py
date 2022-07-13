# Gera conteudo para os diferentes filmes a serem colocados em cartaz,
# como arquivo de video MP4, descricao, etc.
# Sera usado como conexao com o módulo do :lib:‘manager’.
from typing import List, Optional
from interface.view import ViewFactory
from content.movie import Movie, ScheduledMovie


class MovieScheduler:
    def __init__(self):
        self.scheduled_movies: List[Movie] = list()

    def add(self, name, filename, description, start_time, duration,
            thumbnail, director=None, age_restricted=None):

        new_movie = ScheduledMovie(name, filename, description, start_time, duration,
                                   thumbnail, director, age_restricted)
        self.scheduled_movies.append(new_movie)

    def remove(self, name: str):
        self.scheduled_movies = [movie for movie in self.scheduled_movies if movie.name != name]

    def get(self, name: str) -> Optional[Movie]:
        for movie in self.scheduled_movies:
            if movie.name == name:
                return movie
        return None


class MoviePlayer:
    def __init__(self, movie: Movie, cinema: ViewFactory):
        self.movie = movie
        self.cinema = cinema

    def play(self):
        self.cinema.play_src(self.movie.filename, "films/")
