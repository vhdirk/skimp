import os
import sys
import signal
import gettext

VERSION = 'dev'
SELF_DIR = os.path.dirname(os.path.abspath(__file__))
MOD_DIR = os.path.dirname(SELF_DIR)
pkgdatadir = SELF_DIR
localedir = SELF_DIR

sys.path.insert(0, MOD_DIR)
signal.signal(signal.SIGINT, signal.SIG_DFL)
gettext.install('skimp', localedir)

if __name__ == '__main__':
    import gi

    from gi.repository import Gio
    resource = Gio.Resource.load(os.path.join(pkgdatadir, 'skimp.gresource'))
    resource._register()

    from skimp import main
    sys.exit(main.main(VERSION))
