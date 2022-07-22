from typing import Optional, List


class Rating:
    def __init__(self, rate: float, comment: Optional[str] = None):
        """This class is used to store a rating and everything it might
        contain with it. 
        
        Notes: 
            At the given time, ratings only support a value and an optional comment, 
            but this has potential for expansion with images, for example.

        Args:
            rate: a value in range [0, 5], where 0 is the worse (disliked movie).
            comment: an optional comment to accompany/complement the numerical rating.
        """
        self.rate = rate
        self.comment = comment

    def __str__(self) -> str:
        if self.comment is None:
            return f"({self.rate:.1f}) '{self.comment}'"

        return f"({self.rate:.1f})"


class Movie:
    def __init__(self, identifier: int, name: str, filename: str, description: str, start_time: int, duration: int,
                 thumbnail: str = None, director: str = None, age_restricted: bool = False):
        """This class hosts a movie.

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

    def add_rating(self, rate: float, comment: Optional[str] = None) -> None:
        """Adds a new rating to the movie.

        Args:
            rate: a value in range [0, 5], where 0 is the worse (disliked movie).
            comment: an optional comment to accompany/complement the numerical rating.
        """

        if rate < 0 or rate > 5:
            raise ValueError("Rate should be in range [0, 5].")

        self.__ratings.append(Rating(rate, comment))
        rates = [o.rate for o in self.__ratings]

        self.rating = sum(rates) / len(rates)

    def get_rating(self) -> List[Rating]:
        """Get a list of all the ratings

        Returns:
            A list with every rate given to this movie.
        """
        return self.__ratings
