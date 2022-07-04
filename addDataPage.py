import tkinter as tk
from tkinter import ttk


# Page that allows user to add data without trying to work out which door to pick
class AddDataPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.__init__(self, parent)
        lb_data = ttk.Label(self, text="Add Data")

        btn_back_menu = ttk.Button(self, text="Back to Menu",
                                   command=lambda: controller.show_frame(False))

        lb_data.pack(pady=10, padx=10)
        btn_back_menu.pack(pady=10, padx=10)
