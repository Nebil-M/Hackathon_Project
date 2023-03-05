import customtkinter as ct
from tkinter import ttk
import tkinter as tk
from Reader_tab import ReaderTab
from gui_analysis import AnalysisTab


def limited_weight_cells(parent):
    for child in parent.winfo_children():
        if "row" in child.grid_info() and 'column' in child.grid_info():
            parent.rowconfigure(child.grid_info()['row'], weight=1)
            parent.columnconfigure(child.grid_info()['column'], weight=1)
            if child.grid_info() and not isinstance(child, ct.windows.widgets.ctk_button.CTkButton):
                limited_weight_cells(child)


class Controller:
    def __init__(self):
        pass


class App(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reader_button = ct.CTkButton(self, text='Reader', command=lambda: self.switch('reader'))
        self.analysis_button = ct.CTkButton(self, text='Analysis', command=lambda: self.switch('analysis'))

        self.reader_button.grid(row=0, column=0, sticky='news', padx=50, pady=10)
        self.analysis_button.grid(row=0, column=1, sticky='news', padx=50, pady=10)

        self.reader = ReaderTab(self)
        self.analysis = AnalysisTab(self)

        self.reader.grid(row=1, column=0, sticky='news', columnspan=2)

        # Layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.rowconfigure(1, weight=10)
        self.columnconfigure(1, weight=1)

    def switch(self, tab):
        for widget in self.grid_slaves():
            widget.grid_forget()

        self.reader_button.grid(row=0, column=0, sticky='news', padx=50, pady=10)
        self.analysis_button.grid(row=0, column=1, sticky='news', padx=50, pady=10)

        if tab == 'reader':
            self.reader.grid(row=1, column=0, sticky='news', columnspan=2)
        else:
            self.analysis.grid(row=1, column=0, sticky='news', columnspan=2)


if __name__ == '__main__':
    window = ct.CTk()
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")
    App(window).grid(row=0, column=0, sticky='news')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    window.mainloop()
