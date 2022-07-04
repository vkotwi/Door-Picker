import tkinter as tk
from tkinter import ttk

import pandas as pd

events = {}
# Gets names for buttons
#data_names = pd.read_csv("events_and_rewards.txt")

#for i in data_names:
#    print(i)


# Page that allows user to add data without trying to work out which door to pick
class AddDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        lb_data = ttk.Label(self, text="Add Data")

        btn_back_menu = ttk.Button(self, text="Back to Menu",
                                   command=lambda: controller.show_frame(False))

        btn_back_menu.grid(row=0, column=0, pady=10, padx=10)

        lb_data.grid(row=0, column=2, pady=10, padx=10)

        #self.setup_checkboxes()

    def setup_checkboxes(self):
        for i in data_names.nrows:
            c1 = tk.Checkbutton(self, text='Python', variable=None, onvalue=1, offvalue=0, command=None)
        c1.pack()

    def gamblers_lure_rewards(self):
        pass
