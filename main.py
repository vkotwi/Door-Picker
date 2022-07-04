# Import tkinter and GUI override
import tkinter as tk
from tkinter.ttk import *

# Import modules
# from modules.main_page import main_menu

### TODO
# Add ability to pick room and automatically increments with next button if different room number not selected
# save info to SQL database - find way to use joins?

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # Creates tk.TK() instance
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1) # min size, priority
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # stores different "pages"

        frame = MainMenu(container, self)

        self.frames[MainMenu] = frame

        # Assigns frame to specirfic position in grid
        frame.grid(row=0, column=0, stinky="nswe") # nswe stretches to all sides of window

        self.show_frame(MainMenu)


if __name__=='__main__':
    app = App()
    app.mainloop()
