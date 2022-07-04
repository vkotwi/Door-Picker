# Import tkinter and GUI override
import tkinter as tk
from tkinter import ttk

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
        tk.Tk.wm_title(self, "Door Picker 6000")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1) # min size, priority
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # stores different "pages"

        for f in (MainMenu, AddDataPage, DoorPickerMenu):

            frame = f(container, self)

            self.frames[f] = frame

            # Assigns frame to specirfic position in grid
            frame.grid(row=0, column=0, sticky="nsew") # nswe stretches to all sides of window

        self.show_frame(MainMenu)


    # Brings new frame to top of window
    def show_frame(self, container):
        frame = self.frames[container] # gets new frame to display
        frame.tkraise() # brings new frame to top of window
        #^^ better way of doing this?


# Main page class -> move to own file
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        btn_AddData = tk.Button(self, text="Add Data",
                                command=lambda: App.show_frame(self, controller.show_frame(AddDataPage)),
                                font=FONT)
        
        btn_NewPicker = tk.Button(self, text="Door Picker",
                                  command=lambda: App.show_frame(self, controller.show_frame(DoorPickerMenu)),
                                  font=FONT) 

        btn_AddData.pack(pady=10, padx=10)
        btn_NewPicker.pack(pady=10, padx=10)


# Page that allows user to add data without trying to work out which door to pick
class AddDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        lb_Data = tk.Label(self, text="Add Data", font=FONT)

        btn_BackMenu = tk.Button(self, text="Back to Menu",
                                  command=lambda: App.show_frame(self, controller.show_frame(MainMenu)),
                                  font=FONT)

        lb_Data.pack(pady=10, padx=10)
        btn_BackMenu.pack(pady=10, padx=10)        
        

# Page that takes in user input to figure out which door to pick
# Allows correction of door if wrong door is picked
class DoorPickerMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lb_Picker = tk.Label(self, text="Door Picker", font=FONT)

        btn_BackMenu = tk.Button(self, text="Back to Menu",
                                  command=lambda: App.show_frame(self, controller.show_frame(MainMenu)),
                                  font=FONT)

        lb_Picker.pack(pady=10, padx=10)
        btn_BackMenu.pack(pady=10, padx=10)

if __name__=='__main__':
    app = App()
    app.mainloop()
