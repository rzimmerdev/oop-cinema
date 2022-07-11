from typing import Optional


class Movie:
    def __init__(self, name: str, filename: str, description: str, start_time: int, duration: int,
                 thumbnail: str = None, director: str = None, age_restricted: bool = None):
        self.name = name
        self.filename = filename
        self.description = description
        self.start_time = start_time
        self.duration = duration
        self.thumbnail = thumbnail
        self.director = director
        self.age_restricted = age_restricted
        self.rating = None
        self.__ratings = []

    def add_rating(self, rate: int, comment: Optional[str] = None) -> Optional[float]:
        if rate < 0 or rate > 5:
            raise ValueError("Rate should be in range [0, 5].")

        # Create a new rating
        self.__ratings.append(Rating(rate, comment))
        rates = [o.nome for o in self.__ratings]

        # Compute new rates' mean
        self.rating = sum(rates) / len(rates)
        return None


class Rating:
    def __init__(self, rate: int, comment: Optional[str] = None):
        self.rate = rate
        self.comment = comment

    def __str__(self) -> str:
        if self.comment is None:
            return f"({self.rate}.0) '{self.comment}'"

        return f"({self.rate}.0)"


class ScheduledMovie(Movie):
    def __init__(self, name: str, filename: str, description: str, start_time: int, duration: int,
                 thumbnail: str = None, director: str = None, age_restricted: bool = None):
        super().__init__(name, filename, description, start_time, duration,
                         thumbnail, director, age_restricted)


class CurrentMovie(Movie):
    pass
