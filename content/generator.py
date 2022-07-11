# Gera conteudo para os diferentes filmes a serem colocados em cartaz,
# como arquivo de video MP4, descricao, etc.
# Sera usado como conexao com o módulo do :lib:‘manager’.
from typing import List
from interface.view import ViewFactory
from movie import Movie, ScheduledMovie, CurrentMovie


class MovieScheduler:
    def __init__(self):
        self.scheduled_movies: List[Movie] = list()

    def add(self, name: str, filename:str, duration: int, director: str, age_restricted: bool, start_time: int):
        new_movie = ScheduledMovie(name, filename, duration, director, age_restricted, start_time)
        self.scheduled_movies.append(new_movie)

    def remove(self, name: str):
        self.scheduled_movies = [movie for movie in self.scheduled_movies if movie.name != name]


class MoviePlayer:
    def __init__(self, movie: Movie, cinema: ViewFactory):
        self.movie = movie
        self.cinema = cinema

    def play(self):
        video = self.cinema.play_video(self.movie.filename, "../films/")
        self.cinema.show(video)
