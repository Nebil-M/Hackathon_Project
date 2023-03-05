import tkinter as tk
import customtkinter as ct
from tkinter import ttk


class AnalysisTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        WordTable(self).grid(row=0, column=0, sticky='news', rowspan=2)
        Definition(self).grid(row=0, column=1, sticky='news')
        Export(self).grid(row=1, column=1, sticky='news')


# This is the table on the left side
class WordTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.table = ttk.Treeview(self, columns=('Word', 'Frequency', 'Definition'), displaycolumns='#all',
                                  selectmode='none')

        self.scroll_x = ct.CTkScrollbar(self, orientation="horizontal", command=self.table.xview)
        self.scroll_y = ct.CTkScrollbar(self, orientation="vertical", command=self.table.yview)
        self.table.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.grid(row=1, column=0, sticky="ew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.table.grid(row=0, column=0, sticky='news')


class Definition(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.definition = ct.CTkTextbox(self, wrap='word')

        ct.CTkLabel(self, text='Definition').grid(row=0, column=0)
        self.definition.grid(row=1, column=0, sticky='news')


# This is the stuff on the right side
class Export(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_freq = ct.CTkEntry(self, placeholder_text='0', width=5)
        self.max_freq = ct.CTkEntry(self, placeholder_text='10', width=5)
        self.export_button = ct.CTkButton(self, text='Export')

        ct.CTkLabel(self, text='Export words with a frequency between').grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10))
        self.min_freq.grid(row=1, column=0, sticky='ew', padx=(30, 10))
        ct.CTkLabel(self, text='and').grid(row=1, column=1)
        self.max_freq.grid(row=1, column=2, sticky='ew', padx=(10, 30))
        self.export_button.grid(row=10, column=0, columnspan=3, pady=(30, 10))


if __name__ == '__main__':
    window = ct.CTk()
    AnalysisTab(window).grid(row=0, column=0, sticky='news')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
