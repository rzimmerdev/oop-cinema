# Gera conteudo para os diferentes filmes a serem colocados em cartaz,
# como arquivo de video MP4, descricao, etc.
# Sera usado como conexao com o módulo do :lib:‘franchise’.
from typing import List, Optional, Union, Dict
from content.movie import Movie


class MovieScheduler:
    def __init__(self):
        self.scheduled_movies: List[Movie] = list()

    def add(self, movie: Movie):
        self.scheduled_movies.append(movie)

    def new_movie(self, identifier, name, filename, description, start_time, duration,
                  thumbnail, director=None, age_restricted=None):

        new_movie = Movie(identifier, name, filename, description, start_time, duration,
                          thumbnail, director, age_restricted)
        self.scheduled_movies.append(new_movie)

    def remove(self, name: str):
        self.scheduled_movies = [movie for movie in self.scheduled_movies if movie.name != name]

    def get(self, identifier: int = None, name: str = None):
        for movie in self.scheduled_movies:
            if movie.identifier == identifier:
                return movie
        for movie in self.scheduled_movies:
            if movie.name == name:
                return movie
        return self.scheduled_movies


class MovieManager(MovieScheduler):
    def __init__(self):
        super().__init__()

        self.keys = ['identifier', 'name', 'filename', 'description', 'start_time', 'duration',
                     'thumbnail', 'director', 'age_restricted']

    def add_movie(self, movie: Movie):
        self.scheduled_movies.append(movie)

    @staticmethod
    def get_params(movie: Movie):
        return {'identifier': movie.identifier, 'name': movie.name, 'filename': movie.filename,
                'description': movie.description, 'start_time': movie.start_time, 'duration': movie.duration,
                'thumbnail': movie.thumbnail, 'director': movie.director, 'age_restricted': movie.age_restricted}

    def load_values(self, movies: List):
        for params in movies:
            movie = Movie(0, "", "", "", 0, 0)

            for key in params:
                if key in ['identifier', 'start_time', 'duration']:
                    setattr(movie, key, int(params[key]))
                else:
                    setattr(movie, key, params[key])

            self.add_movie(movie)
