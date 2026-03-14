from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QScrollArea, QWidget
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QPixmap, QDesktopServices

from View.theme_manager import ThemeManager
from language import Language


class SettingsHelpPage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(Language.get_language("SettingsHelpPage", "window_title"))
        self.setMinimumWidth(600)
        self.setMinimumHeight(650)

        # ThemeManager initialisieren
        self.theme = ThemeManager()
        colors = self.theme.get_colors()

        # Hauptlayout
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(10)

        # Hintergrundfarbe setzen
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {colors.UI.CONTAINER_BG.name()};
            }}
            QScrollArea {{
                border: none;
                background-color: transparent;
            }}
            QWidget#scrollContent {{
                background-color: transparent;
            }}
        """)

        # Überschrift
        title = QLabel(Language.get_language("SettingsHelpPage", "window_title"))
        title.setStyleSheet(f"""
            font-size: 20px; 
            font-weight: bold; 
            color: {colors.Primary.MAIN.name()};
            padding: 10px;
        """)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # Trennlinie
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet(f"""
            background-color: {colors.Text.DISABLED.name()}; 
            max-width: 400px;
        """)
        main_layout.addWidget(line)
        main_layout.setAlignment(line, Qt.AlignCenter)

        # Scrollbereich für den Hilfetext
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")

        # Container für den Scroll-Inhalt
        scroll_content = QWidget()
        scroll_content.setObjectName("scrollContent")
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setSpacing(15)
        scroll_layout.setContentsMargins(20, 10, 20, 10)

        # Supported Extensions Section
        ranking_title = QLabel(Language.get_language("SettingsHelpPage", "supported_extensions_title"))
        ranking_title.setStyleSheet(f"""
            font-size: 14px;
            font-weight: bold;
            color: {colors.Primary.MAIN.name()};
            margin-top: 5px;
        """)
        scroll_layout.addWidget(ranking_title)

        ranking_text = QLabel(Language.get_language("SettingsHelpPage", "supported_extensions"))
        ranking_text.setWordWrap(True)
        ranking_text.setStyleSheet(f"""
            font-size: 12px;
            color: {colors.Text.SECONDARY.name()};
            line-height: 1.4;
            padding-left: 10px;
        """)
        scroll_layout.addWidget(ranking_text)

        # Ranking Section
        ranking_title = QLabel(Language.get_language("SettingsHelpPage", "ranking_title"))
        ranking_title.setStyleSheet(f"""
            font-size: 14px;
            font-weight: bold;
            color: {colors.Primary.MAIN.name()};
            margin-top: 5px;
        """)
        scroll_layout.addWidget(ranking_title)

        ranking_text = QLabel(Language.get_language("SettingsHelpPage", "ranking_description"))
        ranking_text.setWordWrap(True)
        ranking_text.setStyleSheet(f"""
            font-size: 12px;
            color: {colors.Text.SECONDARY.name()};
            line-height: 1.4;
            padding-left: 10px;
        """)
        scroll_layout.addWidget(ranking_text)

        # Results Section - NEU
        results_title = QLabel(Language.get_language("SettingsHelpPage", "results_title"))
        results_title.setStyleSheet(f"""
                    font-size: 14px;
                    font-weight: bold;
                    color: {colors.Primary.MAIN.name()};
                    margin-top: 10px;
                """)
        scroll_layout.addWidget(results_title)

        results_text = QLabel(Language.get_language("SettingsHelpPage", "results_description"))
        results_text.setWordWrap(True)
        results_text.setStyleSheet(f"""
                    font-size: 12px;
                    color: {colors.Text.SECONDARY.name()};
                    line-height: 1.4;
                    padding-left: 10px;
                """)
        scroll_layout.addWidget(results_text)

        # Snippet Section
        snippet_title = QLabel(Language.get_language("SettingsHelpPage", "snippet_title"))
        snippet_title.setStyleSheet(f"""
            font-size: 14px;
            font-weight: bold;
            color: {colors.Primary.MAIN.name()};
            margin-top: 10px;
        """)
        scroll_layout.addWidget(snippet_title)

        snippet_text = QLabel(Language.get_language("SettingsHelpPage", "snippet_description"))
        snippet_text.setWordWrap(True)
        snippet_text.setStyleSheet(f"""
            font-size: 12px;
            color: {colors.Text.SECONDARY.name()};
            line-height: 1.4;
            padding-left: 10px;
        """)
        scroll_layout.addWidget(snippet_text)

        # Search Depth Section
        depth_title = QLabel(Language.get_language("SettingsHelpPage", "search_depth_title"))
        depth_title.setStyleSheet(f"""
            font-size: 14px;
            font-weight: bold;
            color: {colors.Primary.MAIN.name()};
            margin-top: 10px;
        """)
        scroll_layout.addWidget(depth_title)

        depth_text = QLabel(Language.get_language("SettingsHelpPage", "search_depth_description"))
        depth_text.setWordWrap(True)
        depth_text.setStyleSheet(f"""
            font-size: 12px;
            color: {colors.Text.SECONDARY.name()};
            line-height: 1.4;
            padding-left: 10px;
        """)
        scroll_layout.addWidget(depth_text)


        # Default Path Section
        path_title = QLabel(Language.get_language("SettingsHelpPage", "default_path_title"))
        path_title.setStyleSheet(f"""
            font-size: 14px;
            font-weight: bold;
            color: {colors.Primary.MAIN.name()};
            margin-top: 10px;
        """)
        scroll_layout.addWidget(path_title)

        path_text = QLabel(Language.get_language("SettingsHelpPage", "default_path_description"))
        path_text.setWordWrap(True)
        path_text.setStyleSheet(f"""
            font-size: 12px;
            color: {colors.Text.SECONDARY.name()};
            line-height: 1.4;
            padding-left: 10px;
        """)
        scroll_layout.addWidget(path_text)

        # Language Section
        language_title = QLabel(Language.get_language("SettingsHelpPage", "language_title"))
        language_title.setStyleSheet(f"""
            font-size: 14px;
            font-weight: bold;
            color: {colors.Primary.MAIN.name()};
            margin-top: 10px;
        """)
        scroll_layout.addWidget(language_title)

        language_text = QLabel(Language.get_language("SettingsHelpPage", "language_description"))
        language_text.setWordWrap(True)
        language_text.setStyleSheet(f"""
            font-size: 12px;
            color: {colors.Text.SECONDARY.name()};
            line-height: 1.4;
            padding-left: 10px;
            margin-bottom: 10px;
        """)
        scroll_layout.addWidget(language_text)

        # Console Section
        console_title = QLabel(Language.get_language("SettingsHelpPage", "console_title"))
        console_title.setStyleSheet(f"""
            font-size: 14px;
            font-weight: bold;
            color: {colors.Primary.MAIN.name()};
            margin-top: 10px;
        """)
        scroll_layout.addWidget(console_title)

        console_text = QLabel(Language.get_language("SettingsHelpPage", "console_description"))
        console_text.setWordWrap(True)
        console_text.setStyleSheet(f"""
            font-size: 12px;
            color: {colors.Text.SECONDARY.name()};
            line-height: 1.4;
            padding-left: 10px;
        """)
        scroll_layout.addWidget(console_text)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_content)
        main_layout.addWidget(scroll)

        # OK-Button
        button_layout = QHBoxLayout()
        button_layout.addStretch()

        ok_button = QPushButton("OK")
        ok_button.setFixedWidth(120)
        ok_button.setFixedHeight(30)
        ok_button.setStyleSheet(f"""
            QPushButton {{
                background-color: {colors.Primary.MAIN.name()};
                color: {colors.Text.ON_PRIMARY.name()};
                border: none;
                border-radius: 5px;
                font-weight: bold;
                font-size: 12px;
            }}
            QPushButton:hover {{
                background-color: {colors.Primary.DARK.name()};
            }}
        """)
        ok_button.clicked.connect(self.accept)

        button_layout.addWidget(ok_button)
        button_layout.addStretch()

        main_layout.addLayout(button_layout)