import time
import tkinter as tk
from tkinter import ttk
from enum import Enum

import cv2 as cv2
from ffpyplayer.player import MediaPlayer
from PIL import Image, ImageTk


class Position(Enum):
    START = (0.0, 0.0)
    TOP = (0.0, 0.5)
    CENTER = (0.5, 0.5)
    BOTTOM = (1, 0.5)
    LEFT = (0.5, 1)
    RIGHT = (0.5, 0)


class VideoPlayer:
    def __init__(self, screen, path, size: tuple = (640, 360), pos: Position = Position.CENTER):
        self.path = path
        self.canvas = tk.Canvas(screen, width=size[0], height=size[1])
        self.canvas.pack()

        self.fps = 36
        self.pos = pos
        self.size = size

        self._videobuffer = None
        self._audiobuffer = None
        self._frame = None
        self._is_paused = False

    def __get_shape(self):
        if not self.is_valid():
            return 0, 0
        return self._videobuffer.get(cv2.CAP_PROP_FRAME_WIDTH), self._videobuffer.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        self.destroy(self)

    def is_valid(self):
        if not self._videobuffer:
            return False
        return self._videobuffer.isOpened()

    def open(self, file):
        url = self.path + file
        self._videobuffer = cv2.VideoCapture(url)
        self._audiobuffer = MediaPlayer(url)

        if not self.is_valid():
            raise ValueError("Invalid URL for video file.", url)

        return self.__get_shape()

    def get_frame(self):
        if self.is_valid():
            time.sleep(0.00008)
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
        self._audiobuffer.toggle_pause()

        if not self._is_paused:
            self.play()

    def restart(self, file):
        self.destroy()
        self.open(file)
        self._is_paused = False
        self.play()

    def destroy(self, screen=None):
        if self.is_valid():
            self._videobuffer.release()
            self._audiobuffer.close_player()
        screen.destroy() if screen else None

    def show_tools(self, screen, file):
        toolbar = VideoToolbar(screen, self)
        toolbar.show(file)


class VideoToolbar(ttk.Frame):
    def __init__(self, screen, player: VideoPlayer):
        super().__init__(screen)
        self.screen = screen
        self.player = player

    def show(self, file):
        pause_btn = ttk.Button(self, text="Play/Pause", command=self.player.toggle)
        restart_btn = ttk.Button(self, text="Reiniciar", command=lambda: self.player.restart(file))
        exit_btn = ttk.Button(self, text="Exit", command=lambda: self.player.destroy(self.screen))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        pause_btn.grid(row=0, column=0)
        restart_btn.grid(row=0, column=1)
        exit_btn.grid(row=0, column=2)

        self.pack(fill=tk.X, side=tk.TOP)