# Import tkinter and GUI override
import tkinter as tk
from tkinter import ttk

# Import modules
# from modules.main_page import main_menu

# Import pages
from addDataPage import AddDataPage

# TODO
# Add ability to pick room and automatically increments with next button if different room number not selected
# save info to SQL database - find way to use joins?
# Door picker window would have option to correct door to update data

FONT = ("Arial", 12)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)  # Creates tk.TK() instance
        tk.Tk.iconbitmap(self, default="lop.ico")
        tk.Tk.wm_title(self, "Door Picker 6000")
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)  # min size, priority
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}  # stores different "pages"

        for f in (MainMenu, AddDataPage, DoorPickerMenu):
            frame = f(container, self)

            self.frames[f] = frame

            # Assigns frame to specific position in grid
            frame.grid(row=0, column=0, sticky="nsew")  # nsew stretches to all sides of window

        self.show_frame(MainMenu)

    # Brings new frame to top of window
    def show_frame(self, container):
        if container:
            frame = self.frames[MainMenu]
        else:
            frame = self.frames[container]  # gets new frame to display
        frame.tkraise()  # brings new frame to top of window
        # ^^ better way of doing this?


# Main page class -> move to own file
class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        btn_add_data = ttk.Button(self, text="Add Data",
                                  command=lambda: controller.show_frame(AddDataPage))

        btn_new_picker = ttk.Button(self, text="Door Picker",
                                    command=lambda: controller.show_frame(DoorPickerMenu))

        btn_add_data.pack(pady=10, padx=10)
        btn_new_picker.pack(pady=10, padx=10)


# Allows correction of door if wrong door is picked
class DoorPickerMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lb_picker = ttk.Label(self, text="Door Picker", font=FONT)

        btn_back_menu = ttk.Button(self, text="Back to Menu",
                                   command=lambda: controller.show_frame(MainMenu))

        lb_picker.pack(pady=10, padx=10)
        btn_back_menu.pack(pady=10, padx=10)


if __name__ == '__main__':
    app = App()
    app.mainloop()
