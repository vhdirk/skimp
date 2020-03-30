from typing import Dict, Any

APP_PACKAGE_NAME = "skimp"
APP_NAME = "Skimp"
APP_ID = "com.github.vhdirk.skimp"
APP_VERSION = "0.1.0"
APP_ICON_NAME = APP_ID
APP_ICON_NAME_SYMBOLIC = APP_ID + "-symbolic"
APP_MAIN_UI_NAME = "main.ui"
APP_DESKTOP_ENTRY_NAME = APP_PACKAGE_NAME + ".desktop"
APP_DESCRIPTION = 'Notmuch email'
APP_SOURCE_URL = 'https://gitlab.com/vhdirk/skimp'
APP_AUTHOR = 'Dirk Van Haerenborgh'
APP_AUTHOR_EMAIL = 'vhdirk@gmail.com'

UI_RESOURCE_PATH = "/com/github/vhdirk/skimp/{}"


DESKTOP_ENTRY: Dict[str, str] = {
    'Type': 'Application',
    'Encoding': 'UTF-8',
    'Name': APP_NAME,
    'Comment': APP_DESCRIPTION,
    'Terminal': 'false',
    'Categories': 'System;Settings;',
}
