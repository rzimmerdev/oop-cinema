from typing import List, Dict

from franchise.factory import FranchiseFactory
from database.backup import Manager


class FranchiseManager(Manager):
    def __init__(self):
        super().__init__()
        self.keys = ['name', 'opening_year']
        self.franchises = list()

    def add(self, franchise: FranchiseFactory):
        """Add a franchise to the franchise list"""
        self.franchises.append(franchise)

    def get(self, identifier: int = None, name: str = None):
        """Get a franchise whose field matches given parameters
        
        Args:
            identifier (int, optional): franchises identifier
            name (str, optional): franchises name

        Returns:
            If both parameters are None returns a FranchiseFactory list, 
            otherwise returns the FranchiseFactory that matches given parameters
        """
        if identifier is not None and (0 <= identifier < len(self.franchises)):
            return self.franchises[identifier]
        if name:
            return next(franchise for franchise in self.franchises if franchise.name == name)
        return self.franchises

    @staticmethod
    def get_params(franchise: FranchiseFactory):
        """Get the attributes from a FranchiseFactory object"""
        return {'name': franchise.name, 'opening_year': franchise.opening_year}

    def load_values(self, franchises: List):
        """Load a FranchiseFactory list"""
        for params in franchises:
            franchise = FranchiseFactory(params[self.keys[0]], params[self.keys[1]])
            self.add(franchise)
