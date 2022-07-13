#
# @Author: rzimmerdev
# @About: Implements call functions for creating and managing the cinema interface.
# Should only be called by parent methods, as no functionality is managed herein.
#
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from content.movie import Movie
from interface.player import VideoPlayer


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
        posters = tk.Frame(self.root, width=300)
        posters_canvas = tk.Canvas(posters, height=800)
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
            description = tk.Label(movie_frame, text=movie.description, wraplength=256)
            time = tk.Label(movie_frame, text=str(movie.duration // 60) + ":" + "{:02d}".format(movie.duration % 60))
            name.grid(row=1, column=0)
            description.grid(row=2, column=0)
            time.grid(row=3, column=0)

            movie_frame.grid(row=row, column=0, pady=(0, 40))
        return posters

    def show_movies(self, movies: list[Movie] = None):
        if not movies:
            return
        posters = self.movies_to_poster(movies)
        posters.grid(row=0, column=0, sticky=tk.W)

