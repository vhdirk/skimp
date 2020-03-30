#!/usr/bin/env python3
import os
import sys
import signal
import gettext

SELF_DIR = os.path.dirname(os.path.abspath(__file__))

VERSION = 'dev'
pkgdatadir = os.path.join(SELF_DIR, 'build', 'src')
localedir = os.path.join(SELF_DIR, 'po')

sys.path.insert(0, SELF_DIR)
sys.path.insert(1, pkgdatadir)
signal.signal(signal.SIGINT, signal.SIG_DFL)
gettext.install('skimp', localedir)

if __name__ == '__main__':
    import gi

    os.system("meson build --reconfigure --prefix={}/run".format(SELF_DIR))
    os.system("ninja -C build")

    from gi.repository import Gio
    resource = Gio.Resource.load(os.path.join(pkgdatadir, 'skimp.gresource'))
    resource._register()

    from src import main
    sys.exit(main.main(VERSION))
