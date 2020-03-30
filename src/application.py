import logging

from gi.repository import Gio, Gtk
from injector import inject

from .main_window import MainWindow

logger = logging.getLogger(__name__)


class Application(Gtk.Application):

    @inject
    def __init__(self):
        super().__init__(application_id='com.github.vhdirk.skimp',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()
