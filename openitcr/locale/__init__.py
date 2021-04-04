import os
import gettext
from openitcr.settings import localedir


# gettext
lang = gettext.translation(
    'openitcr', localedir = localedir, languages = ['en_US'])
lang.install()
_ = lang.gettext