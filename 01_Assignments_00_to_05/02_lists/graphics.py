"""Simple graphics library for CS 106A."""

import tkinter
import time
import math

class Canvas:
    """A simple graphics library for CS 106A."""
    
    def __init__(self, width, height):
        """Create a new canvas with the given width and height."""
        self._window = tkinter.Tk()
        self._window.title("Graphics Window")
        self._canvas = tkinter.Canvas(self._window, width=width, height=height)
        self._canvas.pack()
        self._width = width
        self._height = height
        self._last_click_x = None
        self._last_click_y = None
        self._canvas.bind("<Button-1>", self._on_click)
        
    def _on_click(self, event):
        """Internal method to handle mouse clicks."""
        self._last_click_x = event.x
        self._last_click_y = event.y
        
    def get_last_click(self):
        """Return the coordinates of the last mouse click."""
        return (self._last_click_x, self._last_click_y)
        
    def get_mouse_x(self):
        """Return the current x coordinate of the mouse."""
        return self._canvas.winfo_pointerx() - self._canvas.winfo_rootx()
        
    def get_mouse_y(self):
        """Return the current y coordinate of the mouse."""
        return self._canvas.winfo_pointery() - self._canvas.winfo_rooty()
        
    def create_rectangle(self, x1, y1, x2, y2, color="black"):
        """Create a rectangle with the given coordinates and color."""
        return self._canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        
    def create_oval(self, x1, y1, x2, y2, color="black"):
        """Create an oval with the given coordinates and color."""
        return self._canvas.create_oval(x1, y1, x2, y2, fill=color)
        
    def create_line(self, x1, y1, x2, y2, color="black"):
        """Create a line with the given coordinates and color."""
        return self._canvas.create_line(x1, y1, x2, y2, fill=color)
        
    def create_text(self, x, y, text, color="black"):
        """Create text at the given coordinates with the given color."""
        return self._canvas.create_text(x, y, text=text, fill=color)
        
    def set_color(self, object_id, color):
        """Set the color of the given object."""
        self._canvas.itemconfig(object_id, fill=color)
        
    def moveto(self, object_id, x, y):
        """Move the given object to the new coordinates."""
        self._canvas.coords(object_id, x, y, x + 20, y + 20)
        
    def find_overlapping(self, x1, y1, x2, y2):
        """Find all objects that overlap with the given rectangle."""
        return self._canvas.find_overlapping(x1, y1, x2, y2)
        
    def wait_for_click(self):
        """Wait for a mouse click."""
        self._last_click_x = None
        self._last_click_y = None
        while self._last_click_x is None:
            self._window.update()
            time.sleep(0.1) 