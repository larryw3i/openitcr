# THis script is public
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
settings_path = os.path.join( project_path,'settings.toml' )

project_url = 'https://github.com/larryw3i/openitcr'
