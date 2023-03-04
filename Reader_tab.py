import customtkinter as ct
from tkinter import ttk
import tkinter as tk


class ReaderTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Layout
        
        # Creating and griding
        text_read = TextRead(self)
        text_read.grid(row=0, column=0)

        text_read = TextRead(self)
        text_read.grid(row=0, column=0)


class TextRead(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Definitions(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    window = ct.CTk()

    # window.geometry("1300x550")
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")

    E = ReaderTab(window)
    E.grid(row=0, column=0, sticky='NSEW')

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
