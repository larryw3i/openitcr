import tkinter as tk
from tkinter import Menu
import tkinter.ttk as ttk


class MainFrame:
    def __init__(self, master=None):
        # build ui
        
        self.master = tk.Tk() if master == None else master

        self._mainf = tk.Frame( self.master )
        self.mainf = ttk.Frame(self._mainf)

        self.desktopslf = ttk.Labelframe(self.mainf)
        self.alldsb = tk.Scrollbar(self.desktopslf)
        self.alldsb.configure(orient='vertical')
        self.alldsb.pack(side='right')
        self.desktopslf.configure(height='200', text='All desktops', width='450')
        self.desktopslf.pack(side='top')
        self.mainf.pack(side='top')
        self.langcbb = ttk.Combobox(self._mainf)
        self.langcbb.configure(justify='right')
        self.langcbb.pack(anchor='e', side='bottom')
        self._mainf.configure(height='250', width='600')
        self._mainf.pack(side='top')
        self.config_menubar()

        # Main widget
        self.mainwindow = self._mainf

    def config_menubar( self ):
        menubar = Menu(self.master)

        filemenu = Menu(menubar)
        filemenu.add_command(label="Exit" )
        
        menubar.add_cascade(label="File", menu=filemenu)
        
        self.master.config( menu = menubar )

    def run(self):
        self.mainwindow.mainloop()
