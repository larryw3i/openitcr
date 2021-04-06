import tkinter as tk
from tkinter import Menu, messagebox , Toplevel
import tkinter.ttk as ttk
from openitcr.locale import _
from openitcr.common import str_is_lang
from babel import Locale
from openitcr.settings import localedir, project_url
import os
import webbrowser
from openitcr.common import set_lang, restart_openitcr

def can_come_true():
    
    app = MainFrame()
    app.run()
    

class MainFrame:
    def __init__( self, master=None ):

        # build ui
        self.master = tk.Tk(  ) if master == None else master
        self.lang_dict = self.get_lang_dict()

        self.screenwidth = self.master.winfo_screenwidth(  )
        self.screenheight = self.master.winfo_screenheight(  )
        self.halfswidth = int(self.master.winfo_screenwidth()/2)
        self.halfsheight = int(self.master.winfo_screenheight()/2)

        self.master.geometry( f'{self.halfswidth}x{ self.halfsheight }' )

        self.desktopsf = ttk.Frame( self.master, width = self.halfswidth )
        self.alldsb = tk.Scrollbar( self.desktopsf )
        self.alldsb.configure( orient='vertical' )
        self.alldsb.pack( side='right' )
        self.desktopsf.pack( anchor = 'e', side='top' )
        self.langcbbsv = tk.StringVar( self.master, value = \
        self.get_locale_display_name( os.environ['openitcr_lang'] ) )
        self.langcbb = ttk.Combobox( self.master, textvariable = \
        self.langcbbsv, values = [l for l in self.lang_dict.values()] )
        self.langcbb.pack( anchor='e', side='bottom' )
        self.langcbb.bind("<<ComboboxSelected>>", self.change_lang )
        self.config_menubar()
        # Main widget
        self.mainwindow = self.master

    def change_lang(self, event):
        lang = list(self.lang_dict.keys())[list(self.lang_dict.values())\
        .index(self.langcbbsv.get() )]
        set_lang( lang )
        _exit = messagebox.askyesno(
            _('Exit'), 
            _('Do you want to restart the app now and make it work?')
        )
        if _exit: restart_openitcr()

    def get_locale_display_name( self, identifier ):
        return Locale.parse( identifier , sep='_' ).display_name

    def get_lang_dict(self):
        lang_dict = {}
        for d in os.listdir( localedir ):
            if str_is_lang( d ):
                lang_dict[d] = self.get_locale_display_name( d )

        return lang_dict


    def config_menubar(  self  ):
        menubar = Menu( self.master )

        filemenu = Menu( menubar, tearoff=0 )
        filemenu.add_command( label=_("New"), command=self.exit )
        filemenu.add_command( label=_("Open"), command=self.exit )
        filemenu.add_command( label=_("Save"), command=self.exit )
        filemenu.add_command( label=_("Save as..."), command=self.exit )
        filemenu.add_command( label=_("Close"), command=self.exit )

        filemenu.add_separator(  )

        filemenu.add_command( label=_("Exit"), command=self.exit )
        menubar.add_cascade( label=_("File"), menu=filemenu )
        editmenu = Menu( menubar, tearoff=0 )
        editmenu.add_command( label=_("Undo"), command=self.exit )

        editmenu.add_separator(  )

        editmenu.add_command( label=_("Cut"), command=self.exit )
        editmenu.add_command( label=_("Copy"), command=self.exit )
        editmenu.add_command( label=_("Paste"), command=self.exit )
        editmenu.add_command( label=_("Delete"), command=self.exit )
        editmenu.add_command( label=_("Select All"), command=self.exit )

        menubar.add_cascade( label=_("Edit"), menu=editmenu )
        helpmenu = Menu( menubar, tearoff=0 )
        helpmenu.add_command( label=_("Help Index"), command=self.exit )
        helpmenu.add_command( label=_("About..."), command=self.about )
        menubar.add_cascade( label=_("Help"), menu=helpmenu )

        
        self.master.config(  menu = menubar  )

    def about(self):
        abouttl = Toplevel(self.master)
        abouttl.resizable(0,0)
        openitcrlb = tk.Label( abouttl, text = 'OPENITCR',\
        font=('', 22))

        detaillb = tk.Label( abouttl, text = _('Open Information Technology '+
        "Classroom.\n(In fact, it's just some unities, I do nothing, "+
        "thank you to the developers of all relevant projects)") )


        to_project_url = tk.Label(abouttl, text= project_url, fg="blue", \
        cursor="hand2")
        to_project_url.bind("<Button-1>", \
        lambda e: webbrowser.open_new(project_url))

        openitcrlb.pack()
        detaillb.pack()
        to_project_url.pack()

    def exit(  self  ):
        self.master.destroy()
        quit()

    def run( self ):
        self.mainwindow.mainloop(  )
