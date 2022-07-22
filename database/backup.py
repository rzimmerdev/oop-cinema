import csv
from abc import abstractmethod


class Manager:
    def __init__(self):
        self.keys = None

    @abstractmethod
    def get(self):
        pass

    @staticmethod
    def get_params(val):
        return val

    def load_values(self, values):
        return None


class Backup:
    def __init__(self, backup_path="files/backup"):
        self.backup_path = backup_path

    def create(self, manager: Manager, filename):

        values = [manager.get_params(movie) for movie in manager.get()]
        keys = manager.keys

        with open(f'{self.backup_path}/{filename}', 'w', newline='') as output_file:
            output = csv.DictWriter(output_file, keys)
            output.writeheader()
            output.writerows(values)

    def load(self, manager: Manager, filename):
        with open(f'{self.backup_path}/{filename}', 'r', newline='') as input_file:
            values = list(csv.DictReader(input_file))

            manager.load_values(values)
