import tkinter as tk
from tkinter import ttk

# Allows correction of door if wrong door is picked
class DoorPickerMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lb_picker = ttk.Label(self, text="Door Picker")

        btn_back_menu = ttk.Button(self, text="Back to Menu",
                                   command=lambda: controller.show_frame(False))

        lb_picker.pack(pady=10, padx=10)
        btn_back_menu.pack(pady=10, padx=10)