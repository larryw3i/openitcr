import tkinter as tk
from tkinter import Menu
import tkinter.ttk as ttk
from openitcr.locale import _


class MainFrame:
    def __init__( self, master=None ):
        # build ui
        
        self.master = tk.Tk(  ) if master == None else master

        self.screenwidth = self.master.winfo_screenwidth(  )
        self.screenheight = self.master.winfo_screenheight(  )

        self._mainf = tk.Frame(  self.master  )
        self.mainf = ttk.Frame( self._mainf )

        self.desktopslf = ttk.Labelframe( self.mainf, 
        text = _( 'All desktops' ) )
        self.alldsb = tk.Scrollbar( self.desktopslf )
        self.alldsb.configure( orient='vertical' )
        self.alldsb.pack( side='right' )
        self.desktopslf.pack( side='top' )
        self.mainf.pack( side='top' )
        self.langcbb = ttk.Combobox( self._mainf )
        self.langcbb.configure( justify='right' )
        self.langcbb.pack( anchor='e', side='bottom' )
        self._mainf.pack( side='top' )
        self.config_menubar(  )

        # Main widget
        self.mainwindow = self._mainf

    def config_menubar(  self  ):
        menubar = Menu( self.master )

        filemenu = Menu( menubar, tearoff=0 )
        filemenu.add_command( label="New", command=self.exit )
        filemenu.add_command( label="Open", command=self.exit )
        filemenu.add_command( label="Save", command=self.exit )
        filemenu.add_command( label="Save as...", command=self.exit )
        filemenu.add_command( label="Close", command=self.exit )

        filemenu.add_separator(  )

        filemenu.add_command( label="Exit", command=self.exit )
        menubar.add_cascade( label="File", menu=filemenu )
        editmenu = Menu( menubar, tearoff=0 )
        editmenu.add_command( label="Undo", command=self.exit )

        editmenu.add_separator(  )

        editmenu.add_command( label="Cut", command=self.exit )
        editmenu.add_command( label="Copy", command=self.exit )
        editmenu.add_command( label="Paste", command=self.exit )
        editmenu.add_command( label="Delete", command=self.exit )
        editmenu.add_command( label="Select All", command=self.exit )

        menubar.add_cascade( label="Edit", menu=editmenu )
        helpmenu = Menu( menubar, tearoff=0 )
        helpmenu.add_command( label="Help Index", command=self.exit )
        helpmenu.add_command( label="About...", command=self.exit )
        menubar.add_cascade( label="Help", menu=helpmenu )

        
        self.master.config(  menu = menubar  )

    def exit(  self  ):
        self.master.destroy(  )
        quit(  )

    def run( self ):
        self.mainwindow.mainloop(  )
