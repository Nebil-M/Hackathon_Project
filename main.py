import customtkinter as ct
from tkinter import ttk
import tkinter as tk
from Reader_tab import ReaderTab
from gui_analysis import AnalysisTab
from logic_controller import model


def limited_weight_cells(parent):
    for child in parent.winfo_children():
        if "row" in child.grid_info() and 'column' in child.grid_info():
            parent.rowconfigure(child.grid_info()['row'], weight=1)
            parent.columnconfigure(child.grid_info()['column'], weight=1)
            if child.grid_info() and not isinstance(child, ct.windows.widgets.ctk_button.CTkButton):
                limited_weight_cells(child)


class Controller:
    def __init__(self, view, model):
        self.text = view.reader.text_read.text
        self.word = view.reader.word.word
        self.definition = view.reader.word.definition

        self.word_table = view.analysis.word_table
        self.definition2 = view.analysis.definition.definition

        self.bindings()

    def bindings(self):
        txt = self.text.get('0.0', 'end')
        self.text.bind('<ButtonRelease-1>', lambda e: self.select_word(txt, self.text.index(tk.INSERT)))

        self.word_table.table.bind('<ButtonRelease-1>', lambda e: self.table_select())
    def select_word(self, string, index):
        cursor = len(self.text.get('0.0', index))
        pi = cursor
        pf = cursor
        stopers = [' ', ',', '.', '', '?', '/', '']
        while pi != 0 and string[pi] not in stopers:
            pi -= 1
        while pf < len(string) and string[pf] not in stopers:
            pf += 1

        selected = string[pi:pf + 1]
        word = ''.join([l for l in selected if l.isalpha()])

        model.add_freq(word)
        self.update(word)

        return word

    def table_select(self):
        selected_item = self.word_table.table.focus()
        word = self.word_table.table.item(selected_item)['values'][0]
        self.definition2.delete("0.0", 'end')
        self.definition2.insert("0.0", model.get_definition(word))

    def update(self, word):
        self.word.set(word)

        self.definition.delete("0.0", 'end')
        self.definition.insert("0.0", model.get_definition(word))

        self.word_table.load_words()


class App(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reader_button = ct.CTkButton(self, text='Reader', command=lambda: self.switch('reader'), fg_color='medium orchid', border_color='purple1',
                                          hover_color='dark orchid', text_color='white')
        self.analysis_button = ct.CTkButton(self, text='Analysis', command=lambda: self.switch('analysis'), fg_color='medium orchid', border_color='purple1',
                                          hover_color='dark orchid', text_color='white')

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
        # self.configure(fg_color='thistle1')

    def switch(self, tab):
        for widget in self.grid_slaves():
            widget.grid_forget()

        self.reader_button.grid(row=0, column=0, sticky='news', padx=50, pady=10)
        self.analysis_button.grid(row=0, column=1, sticky='news', padx=50, pady=10)

        if tab == 'reader':
            self.reader.grid(row=1, column=0, sticky='news', columnspan=2)
        else:
            self.analysis.grid(row=1, column=0, sticky='news', columnspan=2)


def select_word(string, cursor):
    pi = cursor
    pf = cursor
    stopers = [' ', ',', '.', '', ]
    while pi != 0 and string[pi] not in stopers:
        pi -= 1
    while pf < len(string) and string[pf] not in stopers:
        pf += 1

    selected = string[pi:pf + 1]
    word = ''.join([l for l in selected if l.isalpha()])
    return word


if __name__ == '__main__':
    window = ct.CTk()
    #ct.set_appearance_mode("dark")
    #ct.set_default_color_theme("dark-blue")
    app = App(window)
    app.grid(row=0, column=0, sticky='news')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    c = Controller(app, model)

    window.mainloop()
