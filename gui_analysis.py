import tkinter as tk
import customtkinter as ct
from tkinter import ttk


class AnalysisTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        WordTable(self).grid(row=0, column=0, sticky='news', rowspan=2)
        Definition(self).grid(row=0, column=1, sticky='news')
        Export(self).grid(row=1, column=1, sticky='news')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)


# This is the table on the left side
class WordTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()

        style.configure('Treeview', fieldbackground='#343638', rowheight=40)
        style.configure('Treeview.Heading', background="#343638", foreground='dark orchid', font=('Helvetica', 20, 'bold'),
                        fieldbackground='#343638')

        self.table = ttk.Treeview(self, columns=('Word', 'Frequency'), displaycolumns='#all',
                                  selectmode='none', show='headings')

        self.table.insert('', 'end', 'widgets', text='Widget Tour', values=('sadness', 3), tags='ttk')
        self.table.tag_configure('ttk', font=('Helvetica', 20, 'bold'), foreground='gray74', background='#343638')

        # makes the headings appear
        self.table.heading(0, text='Word')
        self.table.heading(1, text='Frequency')
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


class Definition(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.definition = ct.CTkTextbox(self, wrap='word')

        ct.CTkLabel(self, text='Definition').grid(row=0, column=0)
        self.definition.grid(row=1, column=0, sticky='news', padx=10)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)




# This is the stuff on the right side
class Export(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.min_freq = ct.CTkEntry(self, placeholder_text='0', width=5)
        self.max_freq = ct.CTkEntry(self, placeholder_text='10', width=5)
        self.export_button = ct.CTkButton(self, text='Export', fg_color='medium orchid', border_color='purple1', hover_color='dark orchid')

        ct.CTkLabel(self, text='Export words with a frequency between').grid(row=0, column=0, columnspan=3, padx=20, pady=(20, 10))
        self.min_freq.grid(row=1, column=0, sticky='ew', padx=(30, 10))
        ct.CTkLabel(self, text='and').grid(row=1, column=1)
        self.max_freq.grid(row=1, column=2, sticky='ew', padx=(10, 30))
        self.export_button.grid(row=10, column=0, columnspan=3, pady=(30, 10))

        # haha i love coding ( :
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(10, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)


if __name__ == '__main__':
    window = ct.CTk()
    AnalysisTab(window).grid(row=0, column=0, sticky='news')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
