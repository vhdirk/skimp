from injector import inject
from gi.repository import GLib, Gtk

from .constants import UI_RESOURCE_PATH, APP_MAIN_UI_NAME

@Gtk.Template(resource_path=UI_RESOURCE_PATH.format(APP_MAIN_UI_NAME))
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    main_header = Gtk.Template.Child()
    _main_paned = Gtk.Template.Child("main_paned")

    @inject
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_titlebar(self.main_header)

        self.connect_signals()

    def connect_signals(self):
        pass