import tkinter as tk
from tkinter import ttk

import csv

import pandas as pd

buttons = {}

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

        btn_back_menu.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        lb_data.grid(row=0, column=2, pady=10, padx=10)

        self.add_buttons("Events", "radiobutton", 0)
        self.row_counter = self.row_counter - len(events["Events"]) - 1
        self.add_buttons("Door Events", "radiobutton", 1)
        self.add_buttons("Notable Rewards", "checkbutton")
        self.add_buttons("Normal loot", "checkbutton")

    def add_buttons(self, key, btn_type, col=0):
        ttk.Label(self, text=key).grid(row=self.row_counter, column=col, pady=10, padx=10, sticky='w')
        self.row_counter += 1
        if btn_type == "radiobutton":
            for ele in events[key]:
                btn_name = str("button_" + key + "_" + str(self.row_counter))
                buttons[btn_name] = ttk.Radiobutton(self, text=ele, value=ele)
                buttons[btn_name].grid(row=self.row_counter, column=col, pady=5, padx=20, sticky='w')
                self.row_counter += 1
        elif btn_type == "checkbutton":
            for ele in events[key]:
                btn_name = str("button_" + key + "_" + str(self.row_counter))
                buttons[btn_name] = ttk.Checkbutton(self, text=ele, variable="")
                buttons[btn_name].grid(row=self.row_counter, column=col, pady=5, padx=20, sticky='w')
                self.row_counter += 1


    def gamblers_lure_rewards(self):
        pass
