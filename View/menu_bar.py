import sys

from PySide6.QtCore import QProcess
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QApplication

from View.Help.app_info_help_page import AppInfoHelpPage
from View.messages import Messages
from View.Help.settings_help_page import SettingsHelpPage
from View.settings_page import SettingsWindow
from language import Language
from project_data import ProjectData


class MenuBar(QMenuBar):
    def __init__(self, parent: "MainPage"):
        # Menu Bar
        super().__init__(parent)
        self.window = parent
        self.extras_menu = self.addMenu(Language.get_language("MenuBar","ExtrasItem"))

        self.help_menu = self.addMenu(Language.get_language("MenuBar","QHelpItem"))

        options_action = QAction(Language.get_language("MenuBar","OptionsItem"), self)
        options_action.triggered.connect(self.open_options)
        self.extras_menu.addAction(options_action)

        help_app_info = QAction(Language.get_language("MenuBar","AppInfoItem"), self)
        help_app_info.triggered.connect(self.open_app_info)
        self.help_menu.addAction(help_app_info)

        help_options_action = QAction(Language.get_language("MenuBar","HelpOptionsItem"), self)
        help_options_action.triggered.connect(self.open_help_options)
        self.help_menu.addAction(help_options_action)


    def open_options(self):
        dialog = SettingsWindow()
        last_language = ProjectData.language
        dialog.exec()  # Blockiert bis Fenster geschlossen
        # Signal an MainPage emitten
        self.window.update_values_signal.emit()
        # Nachdem Fenster geschlossen wurde:
        needs_restart = False

        if ProjectData.language != last_language:
            Messages.set_self_destroying_message(self.window,"Sprache geändert - Neustart erforderlich")
            needs_restart = True

        if needs_restart:
            QProcess.startDetached(sys.executable, sys.argv)
            # Diese App beenden
            QApplication.quit()

    def open_app_info(self):
        dialog = AppInfoHelpPage()

        dialog.exec()

    def open_help_options(self):
        dialog = SettingsHelpPage()

        dialog.exec()


