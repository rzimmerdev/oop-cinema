# Cria backups em arquivos CSV das instancias do tipo :class:`movie` e :class:`franchise`.


#from typing import Union


import csv
from content.movie import Movie, ScheduledMovie, CurrentMovie
from manager.franchise import FranchiseFactory, PrivateFranchise, PublicFranchise


class Backup:
    def __init__(self, movies: Movie = None, franchises: FranchiseFactory = None):
        self.movies = movies
        self.franchises = franchises

        self.create_franchise_file()
        self.create_movie_file()

    def create_movie_file(self):
        path = "data/"
        filename = "movie_backup.csv"
        
        fields = ["Name", "Filename", "Description", "Start Time", "Duration",
            "Thumbnail", "Director", "Age Restricted"]

        movie_list = []
        for each in self.movies:
            movie_list.append(each.export_movie())

        # Write to a file
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csv_writer = csv.writer(csvfile, delimiter=";") 
                
            # writing the fields 
            csv_writer.writerow(fields) 
                
            # writing the data rows 
            csv_writer.writerows(movie_list)

    def create_franchise_file(self):
        path = "data/"
        filename = "franchise_backup.csv"
        
        fields = ["Name", "Opening Year"]
        franchise_list = []
        for each in self.franchises:
            franchise_list.append(each.export_franchise())

        # Write to a file
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csv_writer = csv.writer(csvfile, delimiter=";") 
                
            # writing the fields 
            csv_writer.writerow(fields) 
                
            # writing the data rows 
            csv_writer.writerows(franchise_list)


