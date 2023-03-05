import tkinter as tk
import customtkinter as ct
from tkinter import ttk


class AnalysisTab(ct.CTkFrame):
    WordTable(window).grid(row=0, column=0, sticky='news')
    Export(window).grid(row=0, column=1, sticky='news')


# This is the table on the left side
class WordTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.table = ttk.Treeview(self, columns=('Word', 'Frequency', 'Definition'), displaycolumns='#all',
                                  selectmode='none')

        self.table.grid(row=0, column=0, sticky='news')


# This is the stuff on the right side
class Export(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_freq = ct.CTkEntry(self, placeholder_text='0', width=3)
        self.max_freq = ct.CTkEntry(self, placeholder_text='10', width=3)
        self.export_button = ct.CTkButton(self, text='Export')

        ct.CTkLabel(self, text='Export words with a frequency between').grid(row=0, column=0, columnspan=3)
        self.min_freq.grid(row=1, column=0)
        ct.CTkLabel(self, text='and').grid(row=1, column=1)
        self.max_freq.grid(row=1, column=2)
        self.export_button.grid(row=10, column=0, columnspan=3)


if __name__ == '__main__':
    window = ct.CTk()
    AnalysisTab(window)
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
