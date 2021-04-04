import os
import sys
import getopt
import gettext
import toml

# debug 
args = getopt.getopt( sys.argv[1:], '' )[1]; test_args = ['ts','st','test']
debug =  len( set(args)&set(test_args) ) > 0

# path
project_path = os.path.abspath( os.path.dirname(  __file__  ) )
usr_home = os.path.join( project_path, '.home' ) if debug \
    else os.path.expanduser('~')
base_dir = os.path.join( usr_home , '.openitcr')
localedir =  os.path.join( project_path, 'locale')
settings_exam_path = os.path.join( project_path,'settings.toml.example' )
settings_path = os.join( project_path,'settings.toml' )

# gettext
lang = gettext.translation(
    'openitcr', localedir = localedir, languages = ['en_US'])
lang.install()
_ = lang.gettext

# setting
def get_settings_exam():
    return toml.load( settings_exam_path )

def get_version():
    settings_exam = get_settings_exam()
    return settings_exam['version']

def update_settings():
    settings_exam = get_settings_exam()
    if os.path.exists( settings_path ): 
        settings = toml.load( settings_path )
        if settings['version'] != settings_exam['version']:
            settings_exam.update( settings )
            settings_exam['version'] = version
    toml.dump( settings_exam, settings_path )
    
#