class Movie:
    def __init__(self, name: str, filename:str, duration: int, director: str, age_restricted: bool, start_time: int):
        self.name = name
        self.filename = filename
        self.duration = duration
        self.director = director
        self.age_restricted = age_restricted
        self.start_time = start_time


class ScheduledMovie(Movie):
    def __init__(self, name: str, filename:str, duration: int, director: str, age_restricted: bool, start_time: int):
        super().__init__(name, filename, duration, director, age_restricted, start_time)

class CurrentMovie(Movie):
    pass
