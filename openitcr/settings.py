import os
import sys
import getopt
import gettext


# debug 
args = getopt.getopt( sys.argv[1:], '' )[1]; test_args = ['ts','st','test']
debug =  len( set(args)&set(test_args) ) > 0

# path
project_path = os.path.abspath( os.path.dirname(  __file__  ) )
usr_home = os.path.join( project_path, '.home' ) if debug \
    else os.path.expanduser('~')
base_dir = os.path.join( usr_home , '.openitcr')
localedir =  os.path.join( project_path, 'locale')

# gettext
lang = gettext.translation(
    'openitcr', localedir = localedir, languages = ['en_US'])
lang.install()
_ = lang.gettext

#