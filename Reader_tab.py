import customtkinter as ct
from tkinter import ttk
import tkinter as tk


# Combining both sides
class ReaderTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Creating and griding
        text_read = TextRead(self)
        text_read.grid(row=0, column=0, sticky='news', padx=10, pady=10)

        word = Word(self)
        word.grid(row=0, column=1, sticky='news', padx=10, pady=10)


# The left side
class TextRead(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.text = ct.CTkTextbox(self, wrap='word', padx=30, pady=30)
        self.text.grid(row=0, column=0, sticky='news', padx=20, pady=10)

        self.text.insert("0.0", "new text to insert")

# The right side
class Word(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Layout
        #self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.word = tk.StringVar(value='word')
        self.word_label = ct.CTkLabel(self, textvariable=self.word, font=('arial', 25))
        self.definition = ct.CTkTextbox(self, wrap='word')


        self.word_label.grid(row=0, column=0, padx=10, pady=10)
        self.definition.grid(row=1, column=0, sticky='news', padx=10, pady=10)


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
