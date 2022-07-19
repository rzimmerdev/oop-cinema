from interface.view import ViewFactory
from manager.franchise import PrivateFranchise


def main():
    
    cinemark = PrivateFranchise("CineMark", 1999)
    facade = ViewFactory(cinemark)
    

    cinemark.add_movie(0, "Agent 386", "agent_386.mkv",
                       "Agent 386 is investigating a clue that leads him to a shady barbershop in Amsterdam. "
                       "Little does he know that he is being tailed by mercenary Boris Kloris.",
                       1071, 4, thumbnail="agent_386.jpg")

    cinemark.add_movie(1, "Box Assassin", "box_assassin.mkv",
                       "A pizza delivery boy finds himself in the middle of a clash between a gangster boss "
                       "and a legendary assassin who the boy has unknowingly delivered.",
                       842, 3, thumbnail="box_assassin.jpg", age_restricted=False)

    cinemark.add_movie(2, "Object at Rest", "object_rest.mkv",
                       "The life of a stone as it travels over the course of millennia, "
                       "facing nature's greatest obstacle: human civilization.",
                       1071, 6, thumbnail="object_rest.jpg", age_restricted=False)

    cinemark.add_movie(3, "Turning Point", "turning_point.mkv",
                       "Animals and humans switched places. "
                       "Now, animals are ruling the earth and humans are at the verge of extinction.",
                       1071, 3, thumbnail="turning_point.jpg", age_restricted=False)

    facade.show_movies(cinemark.movie_scheduler.scheduled_movies)

    facade.show()


if __name__ == "__main__":
    main()
