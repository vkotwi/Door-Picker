import tkinter as tk

# automatically overrides all the widgets in tkinter
# GUI is OS specific
from tkinter.ttk import *

# Import modules
# from modules.main_page import main_menu

### TODO
# Add ability to pick room and automatically increments with next button if different room number not selected
# save info to SQL database - find way to use joins?


# Creates button with all parameters returns ready button obj to be packed
def createButtons(inst, msg, cmd):
    btn = Button(inst, text=msg, bd='2', command=cmd)
    return btn

# creates new layout
def menu(root):
    data={}


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Creates main window
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Door picker")
        #self.geometry('400x620')

        # Creates frame and assign it to a container (template for later)
        container = tk.Frame(self, height=600, width=400)
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create dictionary of frames
        self.frames = {}
        # Add the components to the dictionary (not frames yet)
        for frame in (MainMenu, ExcitePage):
            new_frame = frame(container, self)
 
            # windows class acts as the root window for the frames
            self.frames[frame] = new_frame
            frame.grid(row=0, column=0, sticky="nsew") #?
 
        # Using a method to switch frames
        #self.show_frame(MainPage)

    def show_frame(self, container):
        frame = self.frames[container]
        # raises the current frame to the top
        frame.tkraise()

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)
 
        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

App()
