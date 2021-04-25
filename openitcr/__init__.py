
# entry point script

import os
import sys
import getopt
from openitcr.settings import settings_exam_path, settings_path, project_path, \
localedir, debug
import re
import toml
import locale
from openitcr.common import str_is_lang, pybabel_compile

def _now():
    print('Welcome to openitcr!')

    _enjoy = Enjoy()

    from openitcr._ui import all_you_think
    sys_argv = sys.argv[1:]
    optlist , args  = getopt.getopt( sys_argv, '' )

    if debug:
        print( f'optlist:\n\t{optlist}\nargs\n\t{args}' )

    if len(args) < 1:
        all_you_think.can_come_true()
        return

    for a in args:
        if a in ['c_po']:
            pybabel_compile()

    for a in args:
        # arg 'ts' with test
        if a in [ 's', 'ts' ,'st', 'start' ]:
            all_you_think.can_come_true()

class Enjoy():
    '''
    Use only in this script
    '''
    def __init__(self):
        self.settings_exam = None
        self.settings = None
        self.ready()

    def ready( self ):
        if not self.is_initialized():
            self.initialize(  )
        os.environ['openitcr_version'] = self.get_version(  )
        os.environ['openitcr_lang'] = self.get_lang()

    def get_lang( self  ):
        locale_langs = [ l for l in os.listdir( f'{project_path}/locale') if  \
        str_is_lang( l ) ]
        sys_lang = locale.getdefaultlocale()[0]
        st_lang = self.settings['lang']
        lang = sys_lang if st_lang == 'en_US' and sys_lang in locale_langs \
        else st_lang
        return lang

    # setting
    def get_settings_exam( self ):
        if self.settings_exam == None:
            self.settings_exam = toml.load( settings_exam_path )
        return self.settings_exam

    def get_settings(self):
        if self.settings != None: return self.settings
        if os.path.exists( settings_path ):
            self.settings =  toml.load( settings_path )
            return self.settings

    def get_version( self  ):
        return self.settings_exam['version']

    def initialize(self ):
        self.update_settings(  )
        self.pybabel_compile()

    def is_initialized(self):
        settings = self.get_settings()
        settings_exam = self.get_settings_exam()
        if settings == None: return False
        if settings['version'] == self.settings_exam['version']: return True
        return False

    def update_settings( self ):
        settings_exam = self.get_settings_exam()
        if os.path.exists( settings_path ):
            settings = self.get_settings()
            version = settings_exam['version']
            settings_exam.update( settings )
            settings_exam['version'] = version

        self.settings = self.settings_exam =  settings_exam
        toml.dump( self.settings_exam, open(settings_path, 'w') )

    #
