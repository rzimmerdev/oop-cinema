import tkinter as tk
from tkinter import ttk
from enum import Enum

import cv2 as cv2
from PIL import Image, ImageTk


class Position(Enum):
    START = (0.0, 0.0)
    TOP = (0.0, 0.5)
    CENTER = (0.5, 0.5)
    BOTTOM = (1, 0.5)
    LEFT = (0.5, 1)
    RIGHT = (0.5, 0)


class VideoPlayer:
    def __init__(self, screen, path, fps: int = 15, size: tuple = (640, 360), pos: Position = Position.CENTER):
        self.path = path
        self.canvas = tk.Canvas(screen, width=size[0], height=size[1])
        self.canvas.pack()

        self.fps = fps
        self.pos = pos
        self.size = size

        self._videobuffer = None
        self._frame = None
        self._is_paused = False

    def is_valid(self):
        return self._videobuffer.isOpened()

    def __get_shape(self):
        return self._videobuffer.get(cv2.CAP_PROP_FRAME_WIDTH), self._videobuffer.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def open(self, file):
        url = self.path + file
        self._videobuffer = cv2.VideoCapture(url)

        if not self.is_valid():
            raise ValueError("Invalid URL for video file.", url)

        return self.__get_shape()

    def get_frame(self):
        if self.is_valid():
            is_loaded, frame = self._videobuffer.read()
            if is_loaded:
                frame = cv2.resize(frame, self.size)
                return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return None

    def show_frame(self):
        # Read next frame from video source buffer
        frame = self.get_frame()
        # Test if next frame could be read, else quit video player

        if frame is not None:
            self._frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self._frame, anchor=tk.NW)
            return True
        return False

    def play(self):
        """Recursive method for loading sequence of frames from Video buffer, displaying them to the
        root window, within the canvas element. Calls end when buffer is empty.

        Examples:
            >>> movie = VideoPlayer("../movies/")
            >>> movie.open("Planet_of_the_Apes.mp4")
            >>> movie.play()
        """
        if self._is_paused or not self.show_frame():
            return
        self.canvas.after(self.fps, self.play)

    def toggle(self):
        self._is_paused = not self._is_paused

        if not self._is_paused:
            self.play()

    def show_tools(self, screen, file, root: tk.Tk):
        tool_frame = tk.Frame(screen)
        tool_frame.pack(fill=tk.X, side=tk.TOP)

        pause_btn = ttk.Button(tool_frame, text="Play/Pause", command=self.toggle)
        restart_btn = ttk.Button(tool_frame, text="Reiniciar", command=lambda: self.open(file))
        exit_btn = ttk.Button(tool_frame, text="Exit", command=root.destroy)

        tool_frame.columnconfigure(0, weight=1)
        tool_frame.columnconfigure(1, weight=1)
        tool_frame.columnconfigure(2, weight=1)

        pause_btn.grid(row=0, column=0)
        restart_btn.grid(row=0, column=1)
        exit_btn.grid(row=0, column=2)

    def __del__(self):
        self._videobuffer.release() if self.is_valid() else None
