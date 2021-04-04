import tkinter as tk
import tkinter.ttk as ttk


class MainFrame:
    def __init__(self, master=None):
        # build ui
        self._mainf = tk.Frame(master)
        self.mainf = ttk.Frame(self._mainf)
        self.titlebarf = ttk.Frame(self.mainf)
        self.tbviewmb = ttk.Menubutton(self.titlebarf)
        self.tbviewmb.configure(text='View')
        self.tbviewmb.pack(anchor='w', side='left')
        self.tbeditmb = ttk.Menubutton(self.titlebarf)
        self.tbeditmb.configure(text='Edit')
        self.tbeditmb.pack(anchor='w', side='left')
        self.tbaboutmb = ttk.Menubutton(self.titlebarf)
        self.tbaboutmb.configure(text='About')
        self.tbaboutmb.pack(anchor='w', side='top')
        self.titlebarf.configure(height='200', width='200')
        self.titlebarf.pack(anchor='w', side='top')
        self.alldesktopslf = ttk.Labelframe(self.mainf)
        self.alldesktopslf.configure(height='200', text='All desktops', width='450')
        self.alldesktopslf.pack(side='top')
        self.mainf.configure(height='200', width='200')
        self.mainf.pack(side='top')
        self.langcbb = ttk.Combobox(self._mainf)
        self.langcbb.pack(anchor='e', side='bottom')
        self._mainf.configure(height='200', width='200')
        self._mainf.pack(side='top')

        # Main widget
        self.mainwindow = self._mainf


    def run(self):
        self.mainwindow.mainloop()
