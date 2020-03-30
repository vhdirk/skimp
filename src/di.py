from typing import Optional, NewType
import logging
from gi.repository import Gtk
from injector import Module, provider, singleton, Injector
# from peewee import SqliteDatabase
from rx.disposable import CompositeDisposable
from rx.subject import Subject

from .constants import APP_PACKAGE_NAME, APP_MAIN_UI_NAME, UI_RESOURCE_PATH

logger = logging.getLogger(__name__)

MainBuilder = NewType('MainBuilder', Gtk.Builder)
# SpeedProfileChangedSubject = NewType("SpeedProfileChangedSubject", Subject)
# SpeedStepChangedSubject = NewType("SpeedStepChangedSubject", Subject)
# EditSpeedProfileBuilder = NewType('EditSpeedProfileBuilder', Gtk.Builder)
# PreferencesBuilder = NewType('PreferencesBuilder', Gtk.Builder)

class ProviderModule(Module):
    @singleton
    @provider
    def provide_main_builder(self) -> MainBuilder:
        logger.debug("provide Gtk.Builder")
        builder = MainBuilder(Gtk.Builder())
        builder.set_translation_domain(APP_PACKAGE_NAME)
        builder.add_from_resource(UI_RESOURCE_PATH.format(APP_MAIN_UI_NAME))
        return builder

    # @singleton
    # @provider
    # def provide_edit_speed_profile_builder(self) -> EditSpeedProfileBuilder:
    #     logger.debug("provide Gtk.Builder")
    #     builder = EditSpeedProfileBuilder(Gtk.Builder())
    #     builder.set_translation_domain(APP_PACKAGE_NAME)
    #     builder.add_from_resource(UI_RESOURCE_PATH.format(APP_EDIT_SPEED_PROFILE_UI_NAME))
    #     return builder

    # @singleton
    # @provider
    # def provide_preferences_builder(self) -> PreferencesBuilder:
    #     logger.debug("provide Gtk.Builder")
    #     builder = PreferencesBuilder(Gtk.Builder())
    #     builder.set_translation_domain(APP_PACKAGE_NAME)
    #     builder.add_from_resource(UI_RESOURCE_PATH.format(APP_PREFERENCES_UI_NAME))
    #     return builder

    @singleton
    @provider
    def provide_thread_pool_scheduler(self) -> CompositeDisposable:
        logger.debug("provide CompositeDisposable")
        return CompositeDisposable()

    # @singleton
    # @provider
    # def provide_database(self) -> SqliteDatabase:
    #     logger.debug("provide CompositeDisposable")
    #     return SqliteDatabase(get_config_path(APP_DB_NAME))

    # @provider
    # def provide_kraken_two_driver(self) -> Optional[KrakenTwoDriver]:
    #     logger.debug("provide KrakenTwoDriver")
    #     return next((dev for dev in find_liquidctl_devices() if isinstance(dev, KrakenTwoDriver)), None)

    # @singleton
    # @provider
    # def provide_speed_profile_changed_subject(self) -> SpeedProfileChangedSubject:
    #     return SpeedProfileChangedSubject(Subject())

    # @singleton
    # @provider
    # def provide_speed_step_changed_subject(self) -> SpeedStepChangedSubject:
    #     return SpeedStepChangedSubject(Subject())


INJECTOR = Injector(ProviderModule)
