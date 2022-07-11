#
# @Author: rzimmerdev
# @About: Implements call functions for creating and managing the cinema interface.
# Should only be called by parent methods, as no functionality is managed herein.
#
import tkinter as tk
from tkinter import ttk

from content.movie import Movie
from player import VideoPlayer


class ViewFactory:
    def __init__(self, franchise: str = None):
        self.franchise = franchise
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=1920, height=1080)

    def show(self):
        self.canvas.pack(anchor=tk.NW)
        self.root.title(self.franchise)
        self.root.mainloop()

    def play_src(self, file, src_path):
        movie_player = VideoPlayer(self.root, self.canvas, src_path, fps=15)
        movie_player.open(file)

        pause_btn = ttk.Button(self.root, text="Play/Pause", command=movie_player.toggle)
        restart_btn = ttk.Button(self.root, text="Reiniciar", command=lambda: movie_player.open(file))
        exit_btn = ttk.Button(self.root, text="Exit", command=self.root.destroy)

        pause_btn.pack(side=tk.TOP, pady=5)
        restart_btn.pack(side=tk.TOP, pady=2)
        exit_btn.pack(pady=5)

        movie_player.play()

    def movies_to_poster(self, movies: list[Movie]) -> tk.Frame:

        print(Movie.__dict__.keys())
        posters = tk.Frame(self.root)

        for movie in movies:

            movie_frame = tk.Frame(posters)
            name = tk.Label(movie_frame, text="Macaco")
            name.pack()
            movie_frame.pack()

        return posters

    def show_movies(self, movies: list[Movie] = None):
        if not movies:
            movies = list()
        poster_list = self.movies_to_poster(movies)
        poster_list.pack()


def main():
    cinema1 = ViewFactory(franchise="CinePlex")
    cinema1.play_src("water.mkv", "films/")
    cinema1.show_movies()
    cinema1.show()


if __name__ == "__main__":
    main()
