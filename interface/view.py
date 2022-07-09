#
# @Author: rzimmerdev
# @About: Implements call functions for creating and managing the cinema interface.
# Should only be called by parent methods, as no functionality is managed herein.
#
import tkinter as tk

from player import VideoPlayer, Position


class ViewFactory:
    def __init__(self, franchise: str = None):
        self.franchise = franchise
        self.root = tk.Tk()

    def show(self, canvas):
        canvas.pack()
        self.root.title(self.franchise)
        self.root.mainloop()

    def play_video(self, file, src_path):
        canvas = tk.Canvas(self.root, width=1920, height=1080)
        canvas.pack()

        movie_player = VideoPlayer(self.root, canvas, src_path, fps=15)
        movie_player.open(file)

        movie_player.play()
        return canvas


def main():
    cinema1 = ViewFactory(franchise="CinePlex")
    video = cinema1.play_video("water.mp4", "../films/")
    cinema1.show(video)


if __name__ == "__main__":
    main()
