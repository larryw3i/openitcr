import tkinter as tk
from tkinter import Menu
import tkinter.ttk as ttk


class MainFrame:
    def __init__(self, master=None):
        # build ui
        if master == None:
            _main = tk.Tk()

            menubar = Menu(_main)
            filemenu = Menu(menubar)
            filemenu.add_command(label="Exit" )
            menubar.add_cascade(label="File", menu=filemenu)
            
            _main.config( menu = menubar )

        self._mainf = tk.Frame(_main)
        self.mainf = ttk.Frame(self._mainf)

        self.alldesktopslf = ttk.Labelframe(self.mainf)
        self.alldsb = tk.Scrollbar(self.alldesktopslf)
        self.alldsb.configure(orient='vertical')
        self.alldsb.pack(side='right')
        self.alldesktopslf.configure(height='200', text='All desktops', width='450')
        self.alldesktopslf.pack(side='top')
        self.mainf.pack(side='top')
        self.langcbb = ttk.Combobox(self._mainf)
        self.langcbb.configure(justify='right')
        self.langcbb.pack(anchor='e', side='bottom')
        self._mainf.configure(height='250', width='600')
        self._mainf.pack(side='top')

        # Main widget
        self.mainwindow = self._mainf


    def run(self):
        self.mainwindow.mainloop()
