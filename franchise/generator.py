from typing import List, Dict

from franchise.factory import FranchiseFactory
from database.backup import Manager


class FranchiseManager(Manager):
    def __init__(self):
        super().__init__()
        self.keys = ['name', 'opening_year']
        self.franchises = list()

    def add(self, franchise: FranchiseFactory):
        self.franchises.append(franchise)

    def get(self, identifier: int = None, name: str = None):
        if identifier is not None and (0 <= identifier < len(self.franchises)):
            return self.franchises[identifier]
        if name:
            return next(franchise for franchise in self.franchises if franchise.name == name)
        return self.franchises

    @staticmethod
    def get_params(franchise: FranchiseFactory):
        return {'name': franchise.name, 'opening_year': franchise.opening_year}

    def load_values(self, franchises: List):
        for params in franchises:
            franchise = FranchiseFactory(params[self.keys[0]], params[self.keys[1]])
            self.add(franchise)
