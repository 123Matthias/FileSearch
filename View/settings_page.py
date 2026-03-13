import os, json
from re import search

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QCheckBox, QComboBox

from language import Language
from project_data import ProjectData
from settings import Settings


class SettingsWindow(QDialog):


    def __init__(self):
        super().__init__()
        self.setWindowTitle(Language.get_language("SettingsPage","title"))
        self.setMinimumWidth(300)

        layout = QVBoxLayout()
        form = QFormLayout()

        # Eingabefelder
        self.keyword_weight = QCheckBox("Aktiv")
        self.search_depth = QLineEdit("4000")
        self.snippet_size = QLineEdit("250")
        self.default_search_path = QLineEdit("")
        self.language = QComboBox()

        # Clear existing items first (optional)
        self.language.clear()

        # Get all files in the languages directory
        language_files = os.listdir("./assets/languages/")

        # Add each filename without extension
        for filename in language_files:
            # Get filename without extension
            name_without_ext = os.path.splitext(filename)[0]
            ext = os.path.splitext(filename)[1]
            if ext == ".json":
                self.language.addItem(name_without_ext)

        form.addRow(Language.get_language("SettingsPage", "searchDepth"), self.search_depth)
        form.addRow(Language.get_language("SettingsPage","snippetSize"), self.snippet_size)
        form.addRow(Language.get_language("SettingsPage","defaultSearchPath"), self.default_search_path)
        form.addRow(Language.get_language("SettingsPage", "language"), self.language)

        layout.addLayout(form)


        def save_and_close():
            Settings.save_settings(
                self.search_depth,
                self.snippet_size,
                self.default_search_path,
                self.language
            )
            self.close()

        save_btn = QPushButton("Speichern")
        save_btn.clicked.connect(save_and_close)

        layout.addWidget(save_btn)
        self.setLayout(layout)

        Settings.load_settings(self)


