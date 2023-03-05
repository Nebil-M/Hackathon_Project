import tkinter as tk
import customtkinter as ct
from tkinter import ttk
from logic_controller import model


class AnalysisTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.word_table = WordTable(self)
        self.word_table.grid(row=0, column=0, sticky='news', rowspan=2)
        self.definition = Definition(self)
        self.definition.grid(row=0, column=1, sticky='news')
        self.export = Export(self)
        self.export.grid(row=1, column=1, sticky='news')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        # self.configure(fg_color='powder blue')


# This is the table on the left side
class WordTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()

        style.configure('Treeview', rowheight=40)
        style.configure('Treeview.Heading', foreground='dark orchid',
                        font=('Helvetica', 20, 'bold'))
        self.table = ttk.Treeview(self, columns=('Word', 'Frequency'), displaycolumns='#all',
                                  selectmode='browse', show='headings')

        self.table.tag_configure('ttk', font=('Helvetica', 20, 'bold'))

        # makes the headings appear
        self.table.heading(0, text='Word')
        self.table.heading(1, text='Frequency')
        # centers the treeview items
        self.table.column(0, anchor='center')
        self.table.column(1, anchor='center')

        # scrollbars
        self.scroll_x = ct.CTkScrollbar(self, orientation="horizontal", command=self.table.xview)
        self.scroll_y = ct.CTkScrollbar(self, orientation="vertical", command=self.table.yview)
        self.table.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)

        self.scroll_x.grid(row=1, column=0, sticky="ew")
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.table.grid(row=0, column=0, sticky='news')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # self.configure(fg_color='powder blue')

        self.load_words()

    def load_words(self):
        # sorts it by value
        temp = []
        for key, value in model.word_freq.items():
            temp.append((key, value))

        temp.sort(reverse=True, key=lambda x: x[1])
        self.table.delete(*self.table.get_children())
        for key, value in temp:
            self.table.insert('', 'end', values=(key, value), tags='ttk')


class Definition(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.definition = ct.CTkTextbox(self, wrap='word', cursor='')

        ct.CTkLabel(self, text='Definition', font=('Arial', 24)).grid(row=0, column=0)
        self.definition.grid(row=1, column=0, sticky='news', padx=10)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        # self.configure(fg_color='powder blue')


# This is the stuff on the right side
class Export(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        self.min_freq = ct.CTkEntry(self, placeholder_text='0', width=5)
        self.max_freq = ct.CTkEntry(self, placeholder_text='10', width=5)

        self.export_button = ct.CTkButton(self, text='Export', fg_color='medium orchid', border_color='purple1',
                                          hover_color='dark orchid', text_color='white', command=self.export, font=('Arial', 24))

        ct.CTkLabel(self, text='Export words with a frequency between', font=('Arial', 24)).grid(row=0, column=0, columnspan=3, padx=20,
                                                                             pady=(20, 10))
        self.min_freq.grid(row=1, column=0, sticky='ew', padx=(30, 10))
        ct.CTkLabel(self, text='and', font=('Arial', 24)).grid(row=1, column=1)
        self.max_freq.grid(row=1, column=2, sticky='ew', padx=(10, 30))
        self.export_button.grid(row=10, column=0, columnspan=3, pady=(30, 10))

        # haha i love coding ( :
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(10, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # self.configure(fg_color='powder blue')
        self.add_vars()

    def add_vars(self):
        self.min_freq.var = tk.StringVar(value=0)
        self.min_freq.configure(textvariable=self.min_freq.var)
        self.max_freq.var = tk.StringVar(value=5)
        self.max_freq.configure(textvariable=self.max_freq.var)

    def export(self):
        min_value = int(self.min_freq.var.get())
        max_value = int(self.max_freq.var.get())
        model.get_freq_range(min_value, max_value)
        # label that says export created
        tk.messagebox.showinfo(message='Export successfully created! Please open the export.txt file to access it.', title='Export created')

if __name__ == '__main__':
    window = ct.CTk()
    AnalysisTab(window).grid(row=0, column=0, sticky='news')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
