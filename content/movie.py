from typing import Optional, List


class Rating:
    def __init__(self, rate: int, comment: Optional[str] = None):
        self.rate = rate
        self.comment = comment

    def __str__(self) -> str:
        if self.comment is None:
            return f"({self.rate}.0) '{self.comment}'"

        return f"({self.rate}.0)"


class Movie:
    def __init__(self, identifier: int, name: str, filename: str, description: str, start_time: int, duration: int,
                 thumbnail: str = None, director: str = None, age_restricted: bool = False):
        self.identifier = identifier
        self.name = name
        self.filename = filename
        self.description = description
        self.start_time = start_time
        self.duration = duration
        self.thumbnail = thumbnail
        self.director = director
        self.age_restricted = age_restricted
        self.rating = 0.0
        self.__ratings = []

    def add_rating(self, rate: int, comment: Optional[str] = None):
        if rate < 0 or rate > 5:
            raise ValueError("Rate should be in range [0, 5].")

        self.__ratings.append(Rating(rate, comment))
        rates = [o.nome for o in self.__ratings]

        self.rating = sum(rates) / len(rates)

    def get_rating(self) -> List[Rating]:
        return self.__ratings
