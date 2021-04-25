import os
import gettext
from openitcr.settings import localedir
from openitcr.common import pybabel_compile

enus_mo_path =  os.path.join(localedir , 'en_US', 'LC_MESSAGES', 'openitcr.mo' )
if not os.path.exists( enus_mo_path ):
    pybabel_compile()

# gettext
lang = gettext.translation(
    'openitcr', localedir = localedir, languages = \
    [ os.environ['openitcr_lang'] ])
lang.install()
_ = lang.gettext
