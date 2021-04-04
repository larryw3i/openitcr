
import sys
import re
import os
import toml
from openitcr.settings import settings_path

lang_reg_str = '^[a-z]{2}_[A-Za-z]{2,}$'
    
def str_is_lang(lstr=''):
    return re.match( lang_reg_str, lstr )

def set_lang(  lstr='' ):
    if not str_is_lang( lstr ):return
    settings  = toml.load( settings_path )
    os.environ['openitcr_lang'] = lstr
    settings['lang']=lstr
    toml.dump( settings, open(settings_path, 'w') )

def restart_openitcr():
    _python = sys.executable
    os.execl( _python, _python, *sys.argv)