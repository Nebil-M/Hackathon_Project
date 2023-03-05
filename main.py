import customtkinter as ct
from tkinter import ttk
import tkinter as tk
from Reader_tab import ReaderTab
from gui_analysis import AnalysisTab


class controller:
    def __init__(self):
        pass


class App(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        tabview = ct.CTkTabview(self)

        tabview.add('Reader')
        tabview.add('Analysis')
        tabview.set('Reader')

        tabview.grid(row=0, column=0, padx=10, pady=10, sticky='news')

        r = ReaderTab(tabview.tab('Reader'))
        r.grid(row=0, column=0, padx=10, pady=10, sticky='news')
        a = AnalysisTab(tabview.tab('Analysis'))
        a.grid(row=0, column=0, padx=10, pady=10, sticky='news')

        # Layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)





if __name__ == '__main__':
    window = ct.CTk()
    App(window).grid(row=0, column=0, sticky='news')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
