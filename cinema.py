from manager.franchise import PrivateFranchise


def main():
    cinemark = PrivateFranchise("CineMark", 1999)

    cinemark.add_movie("Minions: Rise of Gru", "water.mkv",
                       "In the 1970s, young Gru tries to join a group of supervillains, "
                       "called the Vicious 6 after they oust their leader",
                       1071, 141, thumbnail="minions.jpg", age_restricted=False)

    cinemark.add_movie("Despicable Me 3", "water.mkv",
                       "Gru meets his long-lost twin brother Dru, after getting fired from the Anti-Villain League.",
                       842, 155, thumbnail="gru.jpg", age_restricted=False)

    cinemark.add_movie("Minions: Rise of Gru", "water.mkv",
                       "In the 1970s, young Gru tries to join a group of supervillains, "
                       "called the Vicious 6 after they oust their leader",
                       1071, 141, thumbnail="minions.jpg", age_restricted=False)

    cinemark.add_movie("Minions: Rise of Gru", "water.mkv",
                       "In the 1970s, young Gru tries to join a group of supervillains, "
                       "called the Vicious 6 after they oust their leader",
                       1071, 141, thumbnail="minions.jpg", age_restricted=False)

    ticket = cinemark.sell_ticket(32.85, "Despicable Me 3")
    cinemark.play_movie(ticket)
    cinemark.facade.show()


if __name__ == "__main__":
    main()
