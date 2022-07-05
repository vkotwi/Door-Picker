import tkinter as tk
from tkinter import ttk

import csv

import pandas as pd

events = {}
# Gets names for buttons
with open(r"events_and_rewards.txt") as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for r in reader:
        events[r[0]] = []
        for e in r[1:]:
            events[r[0]].append(e.replace('\n', ''))

print(events)


# Page that allows user to add data without trying to work out which door to pick
class AddDataPage(tk.Frame):
    row_counter = 1
    buttons= {}
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        lb_data = ttk.Label(self, text="Add Data")

        btn_back_menu = ttk.Button(self, text="Back to Menu",
                                   command=lambda: controller.show_frame(False))

        btn_back_menu.grid(row=0, column=0, pady=10, padx=10)

        lb_data.grid(row=0, column=2, pady=10, padx=10)

        self.setup_radio_buttons("Events")
        #self.setup_checkboxes()

    def setup_radio_buttons(self, key):
        ttk.Label(self, text=key).grid(row=self.row_counter, column=0, pady=10, padx=10, sticky='w')
        self.row_counter += 1
        for ele in events[key]:
            ttk.Radiobutton(self, text=ele, value=False).grid(row=self.row_counter, column=0, pady=5, padx=20, sticky='w')
            self.row_counter += 1
        # c1 = tk.Checkbutton(self, text='Python', variable=None, onvalue=1, offvalue=0, command=None)

    def setup_checkboxes(self):
        counter = 1
        for key in events:
            ttk.Label(self, text=key).grid(row=counter, column=0, pady=10, padx=10, sticky='w')
            counter += 1
            for ele in events[key]:
                tk.Radiobutton(self, text=ele).grid(row=counter, column=0, pady=5, padx=20, sticky='w')
                counter += 1
            # c1 = tk.Checkbutton(self, text='Python', variable=None, onvalue=1, offvalue=0, command=None)

    def gamblers_lure_rewards(self):
        pass
