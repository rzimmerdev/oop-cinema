# Cria backups em arquivos CSV das instancias do tipo :class:`movie` e :class:`franchise`.
from typing import Union

from content.movie import Movie, ScheduledMovie, CurrentMovie
from manager.franchise import FranchiseFactory, PrivateFranchise, PublicFranchise


class Backup:
    def __init__(self, movies: Movie = None, franchises: FranchiseFactory = None):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
