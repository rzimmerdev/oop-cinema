from database.backup import Backup
from franchise.factory import FranchiseFactory
from franchise.generator import FranchiseManager


def main():
    backup = Backup()

    cinemark = FranchiseManager()

    backup.load(cinemark, "franchise.csv")
    backup.load(cinemark.get(0).movie_manager, "movies.csv")

    cinemark.get(0).show()

    profit = cinemark.get(0).cashier.money_amount

    print(f"Total profit for this session: R$ {profit:.2f}")

    for franchise in cinemark.get():
        backup.create(franchise.movie_manager, "movies.csv")
    backup.create(cinemark, "franchise.csv")


def generate_mockup_movies(franchise: FranchiseFactory):
    franchise.add_movie(0, "Agent 386", "agent_386.mkv",
                        "Agent 386 is investigating a clue that leads him to a shady barbershop in Amsterdam. "
                        "Little does he know that he is being tailed by mercenary Boris Kloris.",
                        1071, 232, thumbnail="agent_386.jpg")

    franchise.add_movie(1, "Box Assassin", "box_assassin.mkv",
                        "A pizza delivery boy finds himself in the middle of a clash between a gangster boss "
                        "and a legendary assassin who the boy has unknowingly delivered.",
                        842, 162, thumbnail="box_assassin.jpg", age_restricted=True)

    franchise.add_movie(2, "Object at Rest", "object_rest.mkv",
                        "The life of a stone as it travels over the course of millennia, "
                        "facing nature's greatest obstacle: human civilization.",
                        1071, 354, thumbnail="object_rest.jpg")

    franchise.add_movie(3, "Turning Point", "turning_point.mkv",
                        "Animals and humans switched places. "
                        "Now, animals are ruling the earth and humans are at the verge of extinction.",
                        1071, 208, thumbnail="turning_point.jpg")

    franchise.add_review(0, 5, "Perfect!")
    franchise.add_review(1, 4, "Very good.")
    franchise.add_review(1, 5, "Best action movie in 2022!")
    franchise.add_review(1, 3, "Somewhat funny, not adequate for kids!")
    franchise.add_review(2, 3, "Too boring, wouldn't watch again...")
    franchise.add_review(3, 5, "Very wild and bold movie.")
    franchise.add_review(3, 2, "I didn't understand nothing!")


if __name__ == "__main__":
    main()
