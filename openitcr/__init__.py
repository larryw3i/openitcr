import os
import sys
import getopt

def enjoy_now():
    print('Welcome to openitcr!')

    from openitcr._ui import _all_you_think

    sys_argv = sys.argv[1:]
    optlist , args  = getopt.getopt( sys_argv, '' )    
    
    if len(args) < 1: 
        _all_you_think.can_come_true()
        return

    for a in args:
        # arg 'ts' with test
        if a in [ 's', 'ts' ,'st', 'start' ]:
            _all_you_think.can_come_true()
