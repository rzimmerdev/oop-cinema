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
        """Video player object, implementing streaming of a given video file to a tkinter canvas object.

        Given a screen object and a movie file directory path, call the open method to load and show a stream,
        and use the derived toggle, restart and destroy methods to traverse through the stream.

        Examples:
            >>> screen = tk.Frame()
            >>> path = "files/movies"
            >>> player = VideoPlayer(screen, path)
            >>> player.open("agent_386.mkv")

        Args:
            screen: Tkinter frame object into which to attach the video player canvas
            path: Movie directory path from which to load streams from
            size: Desired video player canvas size to project movie onto
            pos: Which position of the screen should the video be projected into should the canvas size be smaller
            than the desired screen size
        """
        self.path = path
        self.canvas = tk.Canvas(screen, width=size[0], height=size[1])
        self.canvas.pack()

        self.fps = 36
        self.pos = pos
        self.size = size

        # Declare empty stream buffers as to avoid verification errors if streams weren't yet opened.
        self._videobuffer = None
        self._audiobuffer = None
        self._frame = None
        self._is_paused = False

    def __get_shape(self):
        if not self.is_valid():
            return 0, 0
        return self._videobuffer.get(cv2.CAP_PROP_FRAME_WIDTH), self._videobuffer.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def __del__(self):
        self.destroy()

    def is_valid(self):
        if not self._videobuffer:
            return False
        return self._videobuffer.isOpened()

    def open(self, file: str):
        """Opens both frame and audio streams from given input file stream (desirably with the MKV format)."""
        url = self.path + file
        self._videobuffer = cv2.VideoCapture(url)
        self._audiobuffer = MediaPlayer(url)

        # If stream couldn't be opened, show error to the franchise object
        if not self.is_valid():
            raise ValueError("Invalid URL for video file.", url)

        return self.__get_shape()

    def get_frame(self):
        """Get a single frame from the stream and delay video stream to match the audio stream refresh rate."""
        if self.is_valid():

            # Delay used below is the difference between the sampling rates of the opencv and the ffmpeg libraries
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
        """Pauses or unpauses the movie stream based on its previous status."""
        self._is_paused = not self._is_paused
        self._audiobuffer.toggle_pause()

        if not self._is_paused:
            self.play()

    def restart(self, file: str):
        """Destroy and reopen the video and audio stream, restarting the stream sequence."""
        self.destroy()
        self.open(file)
        self._is_paused = False
        self.play()

    def destroy(self, screen: tk.Frame = None):
        if self.is_valid():
            self._videobuffer.release()
            self._audiobuffer.close_player()
        screen.destroy() if screen else None

    def show_tools(self, screen: tk.Frame, file: str):
        toolbar = VideoToolbar(screen, self)
        toolbar.show(file)


class VideoToolbar(ttk.Frame):
    def __init__(self, screen: tk.Frame, player: VideoPlayer):
        """Show a toolbar relative to a given video player, showing effective interaction buttons for playing/pausing,
        restarting or exiting the player stream.

        Projects the toolbar below the video player into the given screen frame.

        Args:
            screen: Tkinter screen frame that contains the VideoPlayer object,
            and should also contain the toolbar instance
            player: VideoPlayer instance to attribute toolbar button functionalities to
        """
        super().__init__(screen)
        self.screen = screen
        self.player = player

    def show(self, file: str):
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
