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


# TODO: Comment and make function documentations
# TODO: Build unittesting file
class ViewFactory:
    def __init__(self, manager, movie_manager=None, franchise_manager=None,
                 franchise: str = "", background_path="files/background.jpg"):
        self.manager = manager
        self.franchise = franchise

        self.movie_manager = movie_manager
        self.franchise_manager = franchise_manager

        self.root = tk.Tk()
        self.root.resizable(False, False)

        self.set_background(background_path)
        self.config_view()

        self.canvas = None
        self.posters = None
        self.screen = None
        self.reviews = None

    def config_view(self):
        self.root.geometry("1920x1080")
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=0)
        leave = ttk.Button(text="Exit", command=self.root.destroy)
        leave.grid(row=0, column=4, sticky=tk.NE)
        self.root.title(self.franchise)
        style = ttk.Style(self.root)
        style.theme_use("clam")

    def show(self):
        self.root.mainloop()

    def set_background(self, background_path):
        width = self.root.winfo_screenwidth() // 2
        height = self.root.winfo_screenheight()

        background_image = ImageTk.PhotoImage(Image.open(background_path).resize((width, height)))
        background_label = ttk.Label(self.root, image=background_image)
        background_label.image = background_image
        background_label.lower()
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def show_src(self, file: str, src_path: str):
        if self.screen:
            self.screen.destroy()
        self.screen = MovieFrame(self.root)
        self.screen.show(file, src_path)

    def show_movies(self, movies: list[Movie] = None):
        if self.posters:
            self.posters.destroy()
        self.posters = PosterFrame(self.root, self.manager)
        self.posters.show(movies)

    def show_review(self, movie):
        if self.reviews:
            self.reviews.destroy()
        self.reviews = ReviewFrame(self.root, self.manager)
        self.reviews.show(movie)
        self.reviews.show_feedback(movie)


class MovieFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid(row=0, column=1, sticky=tk.W)
        self.movie_player = None

    def destroy(self):
        self.movie_player.destroy()
        super().destroy()

    def show(self, file, src_path):
        self.movie_player = VideoPlayer(self, src_path, size=(960, 480))
        self.movie_player.show_tools(self, file)
        self.movie_player.open(file)
        self.movie_player.play()


class PosterFrame(ttk.Frame):
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

    def show(self, movies: list[Movie]):
        for row, movie in enumerate(movies):
            self.show_poster(row, movie)

    def show_poster(self, row, movie):
        movie_frame = ttk.Frame(self.scroll_frame)
        thumbnail = ImageTk.PhotoImage(Image.open("files/films/" + movie.thumbnail).resize((280, 280)))
        image_label = ttk.Label(movie_frame, image=thumbnail)
        image_label.image = thumbnail
        image_label.grid(row=0, column=0)

        name = ttk.Label(movie_frame, text=movie.name)
        description = ttk.Label(movie_frame, text=movie.description, wraplength=280)
        rating = ttk.Label(movie_frame, text=f"{movie.rating:.2f}⋆")
        time = ttk.Label(movie_frame, text=str(movie.duration // 60) + ":" + "{:02d}".format(movie.duration % 60))
        buy = ttk.Button(movie_frame,
                         text="Buy Ticket!", command=lambda i=movie.identifier: self.manager.sell_ticket(i, 34))
        name.grid(row=1, column=0)
        description.grid(row=2, column=0)
        rating.grid(row=3, column=0, pady=(10, 0))
        time.grid(row=4, column=0)
        buy.grid(row=5, column=0, pady=20)

        movie_frame.grid(row=row, column=0, pady=(0, 40))

    def add_movie(self, identifier, name, filename, description, start_time, duration, thumbnail):
        # new_movie = Movie(identifier=7, )

        return self.manager.add_movie()


class ReviewFrame(ttk.Frame):
    def __init__(self, root, manager):
        super().__init__(root)
        self.grid(row=0, column=2, sticky=tk.W, pady=(50, 20), padx=30)
        self.size()
        self.manager = manager

    def show(self, movie):
        title = ttk.Label(self, text=movie.name)
        description = ttk.Label(self, text=movie.description, wraplength=280, justify=tk.CENTER)
        rating = ttk.Label(self, text=f"Total rating: {movie.rating:.2f}⋆")

        separator = ttk.Separator(self, orient='horizontal')

        title.grid(pady=10)
        description.grid()
        rating.grid(pady=(20, 0))

        separator.grid(row=3, column=0, columnspan=2)

        rating_frame = ttk.Frame(self)

        for row, rating in enumerate(movie.get_rating()):
            score = ttk.Label(rating_frame, text=str(rating.rate) + "⋆")
            comment = ttk.Label(rating_frame, text=rating.comment, wraplength=280)

            score.grid(row=row, column=0, padx=(10, 10))
            comment.grid(row=row, column=1)

        rating_frame.grid(pady=(5, 20))

    def show_feedback(self, movie):
        vcmd = (self.register(callback))

        review_frame = ttk.Frame(self)

        comment_label = tk.Label(review_frame, text="Comment")
        score_label = tk.Label(review_frame, text="Score")

        comment = tk.Entry(review_frame)
        score = tk.Entry(review_frame, validate="key", validatecommand=(vcmd, '%P'))

        comment_label.grid(row=0, column=0)
        comment.grid(row=0, column=1)
        score_label.grid(row=1, column=0)
        score.grid(row=1, column=1)

        confirm = tk.Button(review_frame, text="Send review",
                            command=lambda: self.add_review(movie, int(score.get()), comment.get()))
        confirm.grid(row=2, column=1)
        review_frame.grid()

    def add_review(self, movie, score, comment):
        for widget in self.winfo_children():
            widget.destroy()
        self.manager.add_review(movie.identifier, score, comment)
        self.show(movie)


def callback(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False
