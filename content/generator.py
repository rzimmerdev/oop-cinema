# Gera conteudo para os diferentes filmes a serem colocados em cartaz,
# como arquivo de video MP4, descricao, etc.
# Sera usado como conexao com o módulo do :lib:‘franchise’.
from typing import List, Union
from content.movie import Movie


class MovieScheduler:
    def __init__(self):
        """Allows for managing a movie scheduler, where movie can be scheduled,
        de-scheduled and programmed.
        """
        self.scheduled_movies: List[Movie] = list()

    def add(self, movie: Movie) -> None:
        """Add an existing Movie object to the schedule.

        Args:
            movie: Movie object containing movie that will be added to schedule.
        """
        self.scheduled_movies.append(movie)

    def new_movie(self, identifier: int, name: str, filename: str, description: str, start_time: int, duration: int,
                  thumbnail: str, director: str = None, age_restricted: bool = False) -> None:
        """Create a new Movie object and add it to schedule.

        Args:
            identifier: Movie object's unique ID
            name: movie's title
            filename: name of file containing movie's .mkv: files/films/<filename>
            description: movie's description
            start_time: time when movie will start playing in schedule (Unix).
            duration: movie's duration in seconds.
            thumbnail: name of file containing movie's thumbnail: files/films/<thumbnail>
            director: movie director's name
            age_restricted: true or false, indicating if movie has age restriction
        """

        new_movie = Movie(identifier, name, filename, description, start_time, duration,
                          thumbnail, director, age_restricted)
        self.scheduled_movies.append(new_movie)

    def remove(self, name: str) -> None:
        """Remove a movie from scheduled movies.

        Args:
            name: movie's name.
        """
        self.scheduled_movies = [movie for movie in self.scheduled_movies if movie.name != name]

    def get(self, identifier: int = None, name: str = None) -> Union[List[Movie], Movie, None]:
        """Get a movie whose field matches given parameters. 

        Notes:
            Only one of the args should be passed: identifier or name.

        Args:
            identifier: movie's unique identifier.
            name: movie's name

        Returns:
            A movie, if any is found based on given parameters. Otherwise, returns
            a list of every movie in scheduler.
        """

        if identifier is not None:
            for movie in self.scheduled_movies:
                if movie.identifier == identifier:
                    return movie

        elif name is not None:
            for movie in self.scheduled_movies:
                if movie.name == name:
                    return movie
        else:
            return self.scheduled_movies


class MovieManager(MovieScheduler):
    def __init__(self):
        super().__init__()

        self.keys = ['identifier', 'name', 'filename', 'description', 'start_time', 'duration',
                     'thumbnail', 'director', 'age_restricted']

    def add_movie(self, movie: Movie) -> None:
        """Add a Movie to the manager.
        """
        self.scheduled_movies.append(movie)

    @staticmethod
    def get_params(movie: Movie) -> dict:
        """Get all movie's parameters.

        Returns:
            A dictionary with every parameter labeled (JSON-like).
        """
        return {'identifier': movie.identifier, 'name': movie.name, 'filename': movie.filename,
                'description': movie.description, 'start_time': movie.start_time, 'duration': movie.duration,
                'thumbnail': movie.thumbnail, 'director': movie.director, 'age_restricted': movie.age_restricted}

    def load_values(self, movies: List) -> None:
        for params in movies:
            movie = Movie(0, "", "", "", 0, 0)

            for key in params:
                if key in ['identifier', 'start_time', 'duration']:
                    setattr(movie, key, int(params[key]))
                elif key == 'age_restricted':
                    setattr(movie, key, bool(params[key]))
                else:
                    setattr(movie, key, params[key])

            self.add_movie(movie)
