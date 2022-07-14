import tkinter as tk
from tkinter import CENTER, ttk
from turtle import bgcolor
import interface_parameters
from PIL import ImageTk, Image

class Window:
    def __init__(self, title, type):
        """
        title: string
        type: a string. Can be "main_menu", "table", "group"
        """
        self._title = title
        self._type = type
        self._window_height = 800
        self._window_width = 800
        if type == "main_menu":
            self.window_height = interface_parameters.main_window_height

        self._window = self.initialize_window()
        self._window.mainloop()

    def initialize_window(self):
        window = tk.Tk(className = self._title)
        window.geometry("{X}x{Y}".format(X = self._window_height, Y = self._window_width))
        window.configure(bg = "black")S

        def add_center_image():
            """need to make more centered, later do"""
            global img
            img = (Image.open("main_logo.png"))
            size_x,size_y = img.size
            img = img.resize((size_x//2,size_y//2), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            canvas = tk.Canvas(window, width = size_x,height = 1000)
            canvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            canvas.configure(background = "black")
            canvas.create_image(size_x/2, 1000-size_y/3, image=img)
            print(size_y)
            welcome = tk.Label(window, text = "Welcome to Groupfinder!", bg = "black", fg = "white")
            welcome.config(font = ('Helvatical bold',20))
            welcome.place(relx = 0.5, rely = 0.1, anchor = CENTER)

        add_center_image()


        return window


        

def main():
    Window(" Main Menu", "main_menu")

if __name__ == "__main__":
    main()