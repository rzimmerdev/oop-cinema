from enum import Enum


from content.movie import Movie, ScheduledMovie, CurrentMovie
from manager.franchise import FranchiseFactory, PrivateFranchise, PublicFranchise


class Data(Enum):
    SCHEDULED_MOVIE = 1
    CURRENT_MOVIE = 2
    PRIVATE_FRANCHISE = 3
    PUBLIC_FRANCHISE = 4


class Loader:
    def __init__(self, filename, filetype: Data = None):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
