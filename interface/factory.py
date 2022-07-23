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

from content.generator import MovieManager
from franchise.store import Cashier


class ViewFactory:
    def __init__(self, manager, movie_manager: MovieManager = None, cashier: Cashier = None,
                 franchise: str = "", background_path="files/background.jpg"):
        """Shows a single franchise movie screen, given a desired movie manager to load posters and available
        movies to be played.

        Requires a cashier and a manager object to take care of the movies purchases, reviews and total profit count.

        Args:
            manager: FranchiseFactory object that manages the interface reference
            movie_manager: Holds the movies that are currently in schedule to be played
            cashier: Sells movie tickets and accounts for total profit during session
            franchise: Franchise title to be displayed on the window bar
            background_path: Path to the cinema background, can be changed between franchise instances

        Example:
            >>> # Inside a FranchiseFactory object, call
            >>> self.movie_manager = MovieManager()
            >>> self.cashier = Cashier()
            >>> name = "CineMark - SP Morumbi"
            >>> facade = ViewFactory(self, self.movie_manager, self.cashier, name)
            <class 'interface.factory.ViewFactory'>

        Notes:
            This class should not be instantiated on its own, as it requires a manager object
            to account for new movies added, reviews and tickets sales
        """
        self.manager = manager
        self.movie_manager = movie_manager
        self.cashier = cashier

        self.root = tk.Tk()
        self.root.resizable(False, False)

        self.title = franchise
        self.background_path = background_path
        self.set_background()
        self.config_view()

        self.canvas = None
        self.posters = None
        self.screen = None
        self.reviews = None

    def config_view(self, size="1920x1080", stylesheet="clam"):
        """Configures interface window size, title and column order, as well as OS-independent window style"""
        window = self.root
        window.title(self.title)
        window.geometry(size)
        window.columnconfigure(0, weight=1)
        window.columnconfigure(1, weight=2)
        window.columnconfigure(3, weight=1)
        window.columnconfigure(4, weight=0)

        leave = ttk.Button(text="Exit", command=self.root.destroy)
        leave.grid(row=0, column=4, sticky=tk.NE)

        # Set window style to tkinter available styles
        style = ttk.Style(self.root)
        style.theme_use(stylesheet)

    def show(self):
        """Main loop function, displays Interface window, as well as begins tkinter root.mainloop() function,
        freezing program until further exit conditions are called.

        Use the implemented tkinter :func:`root.after()` to execute parallel processing tasks, such as showing
        any desired video players.
        """
        self.root.mainloop()

    def set_background(self, background_path: str = ""):
        """Defines and places the default background image relative to the current interface instance.
        Background location can be changed by either setting the initial background variable or inserting a new path.

        Args:
            background_path: New path variable to switch with the current interface background
        """
        if background_path != "":
            self.background_path = background_path

        width = self.root.winfo_screenwidth() // 2
        height = self.root.winfo_screenheight()

        background_image = ImageTk.PhotoImage(Image.open(self.background_path).resize((width, height)))
        background_label = ttk.Label(self.root, image=background_image)
        background_label.image = background_image
        background_label.lower()
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def show_src(self, file: str, src_path: str):
        """Shows a video source to the cinema screen, given an input stream file, as well as its directory path.

        Args:
            file: Filename from which to read stream
            src_path: Directory path to the desired file stream

        Examples:
            >>> file = "agent_386.mkv"
            >>> src_path = "files/films"
            >>> self.show_src(file, src_path)
        """
        if self.screen:
            self.screen.destroy()

        self.screen = MovieFrame(self.root)
        self.screen.show(file, src_path)

    def show_movies(self, movies: list[Movie] = None):
        """Shows a list of movies as a poster window, sticked to the left of the cinema screen. For each movie,
        show an individual poster containing basic movie information and ticket selling button.

        Args:
            movies: List of movies to transform into a PosterFrame object
        """
        if self.posters:
            self.posters.destroy()
        self.posters = PosterFrame(self.root, self.manager, self.cashier)
        self.posters.show(movies)

    def show_review(self, movie):
        """Shows a single movie list of reviews as a review window, sticked to the right of the cinema screen.
        Display total review score, and for each individual review display related comment.

        Also shows a "Leave your review" form for users interested in leaving a review.

        Args:
            movie: Movie from which to take reviews to be shown to ReviewFrame object
        """
        if self.reviews:
            self.reviews.destroy()
        self.reviews = ReviewFrame(self.root, self.manager)
        self.reviews.show(movie)
        self.reviews.show_feedback(movie)


class MovieFrame(ttk.Frame):
    def __init__(self, root):
        """Project a movie player to the desired root position, with assigned video player toolbar.

        Instance can be killed by calling the destroy method.

        Args:
            root: Where to fix the frame object to.
        """
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
    def __init__(self, root, manager, cashier):
        """Project a list of movie posters to the desired root position,
        as well as buttons to buy individual movie tickets.

        Instance can be killed by calling the destroy method.

        Args:
            root: Where to fix the frame object to.
        """
        super().__init__(root)
        self.manager = manager
        self.cashier = cashier
        self.grid(row=0, column=0, sticky=tk.W)
        self.scroll_frame = None

    def show(self, movies: list[Movie]):
        title = tk.Label(self, text="Scheduled Movies", font=('Arial Black', 16, "bold"))
        title.pack(pady=(20, 10))

        posters_canvas = tk.Canvas(self, width=300, height=880)
        posters_canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1, padx=10)

        scroll = ttk.Scrollbar(self, orient="vertical", command=posters_canvas.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)

        posters_canvas.configure(yscrollcommand=scroll.set)
        posters_canvas.bind('<Configure>', lambda e: posters_canvas.configure(scrollregion=posters_canvas.bbox("all")))
        self.scroll_frame = ttk.Frame(posters_canvas)

        posters_canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        for row, movie in enumerate(movies):
            self.show_poster(row, movie)

    def show_poster(self, row, movie):
        movie_frame = ttk.Frame(self.scroll_frame)
        thumbnail = ImageTk.PhotoImage(Image.open("files/films/" + movie.thumbnail).resize((280, 280)))
        image_label = ttk.Label(movie_frame, image=thumbnail)
        image_label.image = thumbnail
        image_label.grid(row=0, column=0)

        name = ttk.Label(movie_frame, text=movie.name, font=('Arial Black', 14, "bold"))
        description = ttk.Label(movie_frame, text=movie.description, wraplength=280, font=('Arial Black', 11))
        price = ttk.Label(movie_frame, text="Ticket price: R$ {:.2f}".format(self.cashier.get_price(movie)))
        rating = ttk.Label(movie_frame, text="Rating: {:.2f}⋆".format(movie.rating))
        time = ttk.Label(movie_frame, text="Duration: {}:{:02d}".format(movie.duration // 60, movie.duration % 60))
        buy = ttk.Button(movie_frame,
                         text="Buy Ticket!", command=lambda i=movie.identifier: self.manager.sell_ticket(i))
        name.grid(row=1, column=0)
        description.grid(row=2, column=0)
        rating.grid(row=3, column=0, pady=(10, 0))
        time.grid(row=4, column=0)
        buy.grid(row=5, column=0, pady=(20, 0))
        price.grid(row=6, column=0)

        movie_frame.grid(row=row, column=0, pady=(0, 40))


class ReviewFrame(ttk.Frame):
    def __init__(self, root, manager):
        """Project a list of movie reviews to the desired root position, and a review form for the user.

        Instance can be killed by calling the destroy method.

        Args:
            root: Where to fix the frame object to.
        """
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
        vcmd = (self.register(self.callback))

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

    @staticmethod
    def callback(P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
