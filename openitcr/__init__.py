import os
import sys
import getopt

def enjoy_now():
    print('Welcome to openitcr!')

    sys_argv = sys.argv[1:]
    optlist , args  = getopt.getopt( sys_argv, '' )    
    if len(args) < 1: f.start()
    for a in args:
        # arg 'ts' with test
        if a in [ 's', 'ts' ,'st', 'start' ]:
            from openitcr._ui import _all_u_want
            _all_u_want.to_be_true()

    pass