# Import tkinter and GUI override
import tkinter as tk
from tkinter.ttk import *

# Import modules
# from modules.main_page import main_menu

### TODO
# Add ability to pick room and automatically increments with next button if different room number not selected
# save info to SQL database - find way to use joins?
# Door picker window whould have option to correct door to update data

FONT = ("Arial", 12)

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
        frame.grid(row=0, column=0, sticky=tk.W) # nswe stretches to all sides of window

        self.show_frame(MainMenu)


    # Brings new frame to top of window
    def show_frame(self, container):
        frame = self.frames[container] # gets new frame to display
        frame.tkraise() # brings new frame to top of window
        #^^ better way of doing this?


# Main page class -> move to own file
class MainMenu(tk.Frame):
    def __init__(self, parent, controllers):
        tk.Frame.__init__(self, parent)
        btn_AddData = tk.Button(self, text="Add Data", command=None, font=FONT)
        btn_NewPicker = tk.Button(self, text="Door Picker", command=None, font=FONT) # TODO: grey out if no data

        btn_AddData.pack(pady=10, padx=10)
        btn_NewPicker.pack(pady=10, padx=10)
        
        

if __name__=='__main__':
    app = App()
    app.mainloop()
