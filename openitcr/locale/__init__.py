import os
import gettext
from openitcr.settings import localedir


# gettext
lang = gettext.translation(
    'openitcr', localedir = localedir, languages = \
    [ os.environ['openitcr_lang'] ])
lang.install()
_ = lang.gettext