
# entry point script

import os
import sys
import getopt
from openitcr.settings import settings_exam_path, settings_path, project_path, \
localedir
import re
import toml

def _now():
    print('Welcome to openitcr!')

    from openitcr._ui import _all_you_think
    _enjoy = Enjoy()
    sys_argv = sys.argv[1:]
    optlist , args  = getopt.getopt( sys_argv, '' )    
    
    if len(args) < 1: 
        _all_you_think.can_come_true()
        return

    for a in args:
        # arg 'ts' with test
        if a in [ 's', 'ts' ,'st', 'start' ]:
            _all_you_think.can_come_true()

class Enjoy():
    '''
    Use only in this script
    '''
    def __init__(self):
        self.lang_reg_str = '^[a-z]{2}_[A-Za-z]{2,}$'
        self.settings_exam = self.get_settings_exam()
        self.settings = None
        self.ready()
    
    def str_is_lang(self, lstr=''):
        return re.match( self.lang_reg_str, lstr )

    def ready( self ):
        if not self.is_initialized(): 
            self.initialize(  )
        if self.settings == None:
            self.settings = toml.load( settings_path )
        os.environ['openitcr_version'] = self.get_version(  )
        os.environ['openitcr_lang'] = self.get_lang()

    def get_lang( self  ):
        locale_langs = [ l for l in os.listdir( f'{project_path}/locale') if  \
        self.str_is_lang( l ) ]
        lang = self.settings['lang']
        lang = 'en_US' if (not lang in locale_langs) else lang
        return lang

    def set_lang( self, lstr='' ):
        if not str_is_lang( lstr ):return
        os.environ['openitcr_lang'] = lstr
        settings['lang']=lstr
        toml.dump( self.settings, settings_path )

    # setting
    def get_settings_exam( self ):
        return toml.load( settings_exam_path )

    def get_settings(self):
        return toml.load( settings_path )

    def get_version( self  ):
        return self.settings_exam['version']
    
    def initialize(self ):
        self.update_settings(  )
        self.pybabel_compile()
        
    
    def pybabel_compile(self):
        for  (dirpath, dirnames, filenames) in os.walk( localedir ):
            for f in filenames:
                if f == 'openitcr.po':
                    abs_d_path = f'{project_path}/{dirpath}'
                    os.system(f'pybabel compile -d {localedir} '\
                    +f'-i {abs_d_path}/openitcr.po -o {abs_d_path}/openitcr.mo')
                    print(f'Compiled -> {abs_d_path}/openitcr.po')

    def is_initialized(self):
        if  os.path.exists( settings_path ) :
            self.settings = toml.load( settings_path )
            if self.settings['version'] == self.settings_exam['version']:
                return True
        return False

    def update_settings( self ):
        if os.path.exists( settings_path ): 
            if self.settings['version'] != self.settings_exam['version']:
                self.settings_exam.update( settings )
                self.settings_exam['version'] = version
                self.settings = self.settings_exam
        toml.dump( self.settings_exam, open(settings_path, 'w') )
        
    #   