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
    def __init__(self, manager, franchise: str = None, background="files/background.jpeg"):
        self.manager = manager
        self.franchise = franchise
        self.root = tk.Tk()
        self.root.geometry("1920x1080")
        self.background = background
        self.root.resizable(False, False)
        self.canvas = None

    def show(self):
        width = self.root.winfo_screenwidth() // 2
        height = self.root.winfo_screenheight()
        background_image = ImageTk.PhotoImage(Image.open(self.background).resize((width, height)))
        background_label = ttk.Label(self.root, image=background_image)
        background_label.lower()

        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.title(self.franchise)
        style = ttk.Style(self.root)
        style.theme_use("clam")
        self.root.mainloop()

    def play_src(self, file, src_path):
        screen = ttk.Frame(self.root)
        movie_player = VideoPlayer(screen, src_path, fps=15)
        movie_player.show_tools(screen, file, self.root)
        movie_player.open(file)
        movie_player.play()
        screen.grid(row=0, column=1, sticky=tk.W)

    def show_movies(self, movies: list[Movie] = None):
        pv = PosterView(self.root)
        pv.movies_to_poster(movies)


class MovieView(ttk.Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root

    def play_src(self, file, src_path):
        movie_player = VideoPlayer(self, src_path, fps=15)
        movie_player.show_tools(self, file, self.root)
        movie_player.open(file)
        movie_player.play()
        self.grid(row=0, column=1, sticky=tk.W)


class PosterView(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid(row=0, column=0, sticky=tk.W)

        posters_canvas = tk.Canvas(self, height=1080)
        posters_canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1, padx=10)

        scroll = ttk.Scrollbar(self, orient="vertical", command=posters_canvas.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)

        posters_canvas.configure(yscrollcommand=scroll.set)
        posters_canvas.bind('<Configure>', lambda e: posters_canvas.configure(scrollregion=posters_canvas.bbox("all")))

        self.scroll_frame = ttk.Frame(posters_canvas)
        posters_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

    def movies_to_poster(self, movies: list[Movie]):
        for row, movie in enumerate(movies):
            movie_frame = ttk.Frame(self.scroll_frame)
            thumbnail = ImageTk.PhotoImage(Image.open("posters/" + movie.thumbnail).resize((280, 280)))
            image_label = ttk.Label(movie_frame, image=thumbnail)
            image_label.image = thumbnail
            image_label.grid(row=0, column=0)

            name = ttk.Label(movie_frame, text=movie.name)
            description = ttk.Label(movie_frame, text=movie.description, wraplength=280)
            time = ttk.Label(movie_frame, text=str(movie.duration // 60) + ":" + "{:02d}".format(movie.duration % 60))
            buy = ttk.Button(movie_frame, text="Buy Ticket!")
            name.grid(row=1, column=0)
            description.grid(row=2, column=0)
            time.grid(row=3, column=0)
            buy.grid(row=4, column=0, pady=20)

            movie_frame.grid(row=row, column=0, pady=(0, 40))


class TicketView(ttk.Frame):
    pass
