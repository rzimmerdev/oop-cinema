from typing import Optional

class Movie:
    def __init__(self, name: str, filename:str, duration: int, director: str, age_restricted: bool, start_time: int):
        self.name = name
        self.filename = filename
        self.duration = duration
        self.director = director
        self.age_restricted = age_restricted
        self.start_time = start_time
        self.rating = None
        self.__ratings = []

    def add_rating(self, rate: int) -> Optional[float]:
        if rate < 0 or rate > 5:
            raise ValueError("Rate should be in range [0, 5].")

        self.__ratings.append(rate)
        self.rating = sum(self.__ratings) / len(self.__ratings)
        

class ScheduledMovie(Movie):
    def __init__(self, name: str, filename:str, duration: int, director: str, age_restricted: bool, start_time: int):
        super().__init__(name, filename, duration, director, age_restricted, start_time)

class CurrentMovie(Movie):
    pass
