# main.py
#
# Copyright 2020 Dirk Van Haerenborgh
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import logging
import signal
from typing import Type, Any
import asyncio

from rx.disposable import CompositeDisposable
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, Gio
import gbulb

from .di import INJECTOR
from .application import Application

logger = logging.getLogger(__name__)


def cleanup() -> None:
    logger.debug("cleanup")
    composite_disposable = INJECTOR.get(CompositeDisposable)
    composite_disposable.dispose()
    # database = INJECTOR.get(SqliteDatabase)
    # database.close()
    # kraken_repository = INJECTOR.get(KrakenRepository)
    # kraken_repository.cleanup()
    # futures.thread._threads_queues.clear()


def handle_exception(exc_type: Type[BaseException], exc_value: BaseException, exc_traceback: Any) -> None:
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    cleanup()
    sys.exit(1)


sys.excepthook = handle_exception


def main(version: str) -> int:
    logger.debug("main")

    gbulb.install(gtk=True)
    loop = asyncio.get_event_loop()

    application: Application = INJECTOR.get(Application)
    GLib.unix_signal_add(GLib.PRIORITY_DEFAULT, signal.SIGINT, application.quit)
    loop.run_forever(application=application, argv=sys.argv)

    # no idea how to get the exit status
    cleanup()
    return sys.exit(0)


