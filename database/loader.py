
import csv
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

    def read_movie_file(self):
        path = "data/"
        filename = "movie_backup.csv"
        
        fields = ["Name", "Filename", "Description", "Start Time", "Duration",
            "Thumbnail", "Director", "Age Restricted"]

        movie_list = []
        for each in self.movies:
            movie_list.append(each.export_movie())

        # Write to a file
        with open(filename) as csvfile: 
            # creating a csv writer object 
            csv_reader = csv.reader(csvfile, delimiter=";") 
            movie_list = []
            for row in csv_reader:
                movie_list.append(row)

        return movie_list


                

        def read_franchise_file(self):
        path = "data/"
        filename = "franchise_backup.csv"
        
        fields = ["Name", "Opening Year"]
        franchise_list = []
        for each in self.franchises:
            franchise_list.append(each.export_franchise())

        # Write to a file
        with open(filename) as csvfile: 
            # creating a csv writer object 
            csv_reader = csv.reader(csvfile, delimiter=";") 
            franchise_list = []
            for row in csv_reader:
                franchise_list.append(row)

        return franchise_list




def main():
    pass


if __name__ == "__main__":
    main()
