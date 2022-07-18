#
# @Author: rzimmerdev
# @About: Implements call functions for creating and managing the cinema interface.
# Should only be called by parent methods, as no functionality is managed herein.
#
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from content.movie import Movie, Rating
from interface.player import VideoPlayer


class ViewFactory:
    def __init__(self, manager, franchise: str = None, background_path="files/background.jpeg"):
        self.manager = manager
        self.franchise = franchise
        self.root = tk.Tk()
        self.set_background(background_path)
        self.config_view()
        self.root.resizable(False, False)
        self.canvas = None

    def config_view(self):
        self.root.geometry("1920x1080")
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(3, weight=1)
        self.root.title(self.franchise)
        style = ttk.Style(self.root)
        style.theme_use("clam")

    def show(self):
        self.root.mainloop()

    def play_src(self, file: str, src_path: str):
        screen = MovieView(self.root)
        screen.play_src(file, src_path)

    def set_background(self, background_path):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        background_image = ImageTk.PhotoImage(Image.open(background_path).resize((width, height)))
        background_label = ttk.Label(self.root, image=background_image)
        background_label.image = background_image
        background_label.lower()
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def show_review(self, movie):
        reviews = ReviewView(self.root)
        reviews.show_rating(movie)

    def show_movies(self, movies: list[Movie] = None):
        pv = PosterView(self.root, self.manager)
        pv.movies_to_poster(movies)


class MovieView(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid(row=0, column=1, sticky=tk.W)

    def play_src(self, file, src_path):
        movie_player = VideoPlayer(self, src_path, fps=30)
        movie_player.show_tools(self, file)
        movie_player.open(file)
        movie_player.play()


class PosterView(ttk.Frame):
    def __init__(self, root, manager):
        super().__init__(root)
        self.manager = manager
        self.grid(row=0, column=0, sticky=tk.W)

        posters_canvas = tk.Canvas(self, height=880)
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
            thumbnail = ImageTk.PhotoImage(Image.open("files/films/" + movie.thumbnail).resize((280, 280)))
            image_label = ttk.Label(movie_frame, image=thumbnail)
            image_label.image = thumbnail
            image_label.grid(row=0, column=0)

            name = ttk.Label(movie_frame, text=movie.name)
            description = ttk.Label(movie_frame, text=movie.description, wraplength=280)
            rating = ttk.Label(movie_frame, text=str(movie.rating) + "⋆")
            time = ttk.Label(movie_frame, text=str(movie.duration // 60) + ":" + "{:02d}".format(movie.duration % 60))
            buy = ttk.Button(movie_frame,
                             text="Buy Ticket!", command=lambda i=movie.identifier: self.manager.sell_ticket(i, 34))
            name.grid(row=1, column=0)
            description.grid(row=2, column=0)
            rating.grid(row=3, column=0)
            time.grid(row=4, column=0)
            buy.grid(row=5, column=0, pady=20)

            movie_frame.grid(row=row, column=0, pady=(0, 40))

    def add_movie(self, identifier, name, filename, description, start_time, duration, thumbnail):
        new_movie = Movie(identifier=7, )

        return self.manager.add_movie(new_movie)


class ReviewView(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid(row=0, column=2, sticky=tk.W)
        self.size()

    def show_rating(self, movie):

        title = ttk.Label(self, text=movie.name)
        title.grid()

        rating = ttk.Label(self, text=str(movie.rating) + "⋆")
        rating.grid()

        rating_frame = ttk.Frame(self)

        for rating in movie.get_rating():
            score = ttk.Label(rating_frame, text=str(rating.rate) + "⋆")
            comment = ttk.Label(rating_frame, text=rating.comment)

            score.grid()
            comment.grid()
