#
# @Author: rzimmerdev
# @About: Implements call functions for creating and managing the cinema interface.
# Should only be called by parent methods, as no functionality is managed herein.
#
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from content.movie import Movie
from player import VideoPlayer


class ViewFactory:
    def __init__(self, franchise: str = None):
        self.franchise = franchise
        self.root = tk.Tk()
        style = ttk.Style(self.root)
        style.theme_use('alt')
        self.root.geometry("1840x1080")
        self.root.resizable(False, False)
        self.canvas = None

    def show(self):
        self.root.columnconfigure(0, weight=1)
        self.root.title(self.franchise)
        self.root.mainloop()

    def play_src(self, file, src_path):
        screen = tk.Frame(self.root)
        movie_player = VideoPlayer(screen, src_path, fps=15)
        movie_player.show_tools(screen, file, self.root)
        movie_player.open(file)
        movie_player.play()
        screen.grid(row=0, column=1, sticky=tk.W)

    def movies_to_poster(self, movies: list[Movie]) -> tk.Frame:
        posters = tk.Frame(self.root, height=300, width=100)
        posters_canvas = tk.Canvas(posters)
        posters_canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        scroll = tk.Scrollbar(posters, orient="vertical", command=posters_canvas.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)

        posters_canvas.configure(yscrollcommand=scroll.set)
        posters_canvas.bind('<Configure>', lambda e: posters_canvas.configure(scrollregion=posters_canvas.bbox("all")))

        scroll_frame = tk.Frame(posters_canvas)
        posters_canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        for row, movie in enumerate(movies):
            movie_frame = tk.Frame(scroll_frame)
            thumbnail = ImageTk.PhotoImage(Image.open("posters/" + movie.thumbnail).resize((256, 256)))
            image_label = tk.Label(movie_frame, image=thumbnail)
            image_label.image = thumbnail
            image_label.grid(row=0, column=0)
            name = tk.Label(movie_frame, text=movie.name)
            name.grid(row=1, column=0)

            # description = tk.Label(movie_frame, text=movie.description, wraplength=256)
            # time = tk.Label(movie_frame, text=str(movie.duration // 60) + ":" + "{:02d}".format(movie.duration % 60))
            # thumbnail = ImageTk.PhotoImage(Image.open("posters/" + movie.thumbnail).resize((256, 256)))
            #
            # image_label = tk.Label(movie_frame, image=thumbnail)
            # image_label.image = thumbnail
            #
            # name.grid()
            # description.grid()
            # time.grid()
            # image_label.grid()
            #
            movie_frame.grid(row=row, column=0, pady=(0, 40))
        return posters

    def show_movies(self, movies: list[Movie] = None):
        if not movies:
            movies = list()
        posters = self.movies_to_poster(movies)
        posters.grid(row=0, column=0, sticky=tk.W)


def main():
    cinema1 = ViewFactory(franchise="CinePlex")
    movies = [Movie("Minions: Rise of Gru", "water.mkv",
                    "In the 1970s, young Gru tries to join a group of supervillains, "
                    "called the Vicious 6 after they oust their leader",
                    1071, 141, thumbnail="minions.jpg", age_restricted=False),
              Movie("Despicable Me 3", "water.mkv",
                    "Gru meets his long-lost twin brother Dru, after getting fired from the Anti-Villain League.",
                    842, 155, thumbnail="gru.jpg", age_restricted=False),
              Movie("Minions: Rise of Gru", "water.mkv",
                    "In the 1970s, young Gru tries to join a group of supervillains, "
                    "called the Vicious 6 after they oust their leader",
                    1071, 141, thumbnail="minions.jpg", age_restricted=False),
              Movie("Minions: Rise of Gru", "water.mkv",
                    "In the 1970s, young Gru tries to join a group of supervillains, "
                    "called the Vicious 6 after they oust their leader",
                    1071, 141, thumbnail="minions.jpg", age_restricted=False)
              ]
    cinema1.play_src(movies[0].filename, "films/")
    cinema1.show_movies(movies)
    cinema1.show()


if __name__ == "__main__":
    main()
