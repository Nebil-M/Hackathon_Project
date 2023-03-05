import customtkinter as ct
from tkinter import ttk
import tkinter as tk


# Combining both sides
class ReaderTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Layout

        # Creating and griding
        text_read = TextRead(self)
        text_read.grid(row=0, column=0)

        word = Word(self)
        word.grid(row=0, column=1)


# The left side
class TextRead(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.text = ct.CTkTextbox(self, wrap='word')

        self.text.grid(row=0, column=0)

# The right side
class Word(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.word = tk.StringVar(value='word')
        self.word_label = ct.CTkLabel(self, textvariable=self.word)
        self.definition = ct.CTkTextbox(self, wrap='word')

        self.word_label.grid(row=0, column=0)
        self.definition.grid(row=1, column=0)


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
