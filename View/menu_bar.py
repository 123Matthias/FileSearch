import sys

from PySide6.QtCore import QProcess
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QApplication

from View.Help.app_info_help_page import AppInfoHelpPage
from View.messages import Messages
from View.Help.settings_help_page import SettingsHelpPage
from View.settings_page import SettingsWindow
from project_data import ProjectData


class MenuBar(QMenuBar):
    def __init__(self, parent: "MainPage"):
        # Menu Bar
        super().__init__(parent)
        self.window = parent
        self.extras_menu = self.addMenu("Extras")
        self.help_menu = self.addMenu("Hilfe")

        settings_action = QAction("Einstellungen", self)
        settings_action.triggered.connect(self.open_settings)
        self.extras_menu.addAction(settings_action)

        help_settings_action = QAction("App Info", self)
        help_settings_action.triggered.connect(self.open_app_info)
        self.help_menu.addAction(help_settings_action)

        help_settings_action = QAction("Einstellungen", self)
        help_settings_action.triggered.connect(self.open_help_settings)
        self.help_menu.addAction(help_settings_action)


    def open_settings(self):
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

    def open_help_settings(self):
        dialog = SettingsHelpPage()

        dialog.exec()


