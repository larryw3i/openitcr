#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import sys
import os

sys.path.append( os.getcwd() )

from openitcr import _now

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(_now())

