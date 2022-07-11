import threading
import tkinter as tk
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
    def __init__(self, window_root, canvas, path,
                 size: tuple = (640, 360), pos: Position = Position.CENTER, fps: int = 15):
        self.root = window_root
        self.path = path
        self.canvas = canvas

        self.pos = pos
        self.size = size
        self.fps = fps

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
        offset_x = (self.canvas.winfo_width() - self.size[0]) * self.pos.value[0]
        offset_y = (self.canvas.winfo_height() - self.size[1]) * self.pos.value[1]

        if frame is not None:
            self._frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(offset_x, offset_y, image=self._frame, anchor=tk.NW)
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
        if self._is_paused:
            return
        playing = self.show_frame()
        self.root.after(self.fps, self.play)

    def toggle(self):
        self._is_paused = not self._is_paused

        if not self._is_paused:
            self.play()

    def __del__(self):
        self._videobuffer.release() if self.is_valid() else None
