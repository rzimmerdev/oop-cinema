#
# @Author: rzimmerdev
# @About: Implements call functions for creating and managing the cinema interface.
# Should only be called by parent methods, as no functionality is managed herein.
#
import tkinter as tk
from tkinter import ttk
import cv2


class ViewFactory:
    def __init__(self, franchise: str = None):
        self.franchise = franchise
        self.video = None
        self.root = tk.Tk()
        content = tk.Label(text="Hello World!")
        content.pack()

    def show(self):
        self.root.mainloop()

    def play_video(self, url):
        self.video = cv2.VideoCapture(url)
        pass


def main():
    cinema1 = ViewFactory(franchise="CinePlex")
    cinema1.show()


if __name__ == "__main__":
    main()
