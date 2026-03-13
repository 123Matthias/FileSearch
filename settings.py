import json
import os

from PySide6.QtWidgets import QWidget

from project_data import ProjectData


def get_settings_path():
    home = os.path.expanduser("~")
    settings_dir = os.path.join(home, "keysearch_app_settings")
    os.makedirs(settings_dir, exist_ok=True)
    return os.path.join(settings_dir, "settings.json")

class Settings:


    @staticmethod
    def save_settings(keyword_weight, search_depth, snippet_size, default_search_path, language):
        data = {
            "keyword_weight": keyword_weight.isChecked(),
            "search_depth": search_depth.text(),
            "snippet_size": snippet_size.text(),
            "default_search_path": default_search_path.text(),
            "language": language.currentText(),
        }
        with open(get_settings_path(), "w") as f:
            json.dump(data, f, indent=4)
        ProjectData.set(
            keyword_weight=keyword_weight.isChecked(),
            search_depth=int(search_depth.text()),
            snippet_size=int(snippet_size.text()),
            default_search_path=default_search_path.text(),
            language=language.currentText(),
        )

    @staticmethod
    def load_settings(window=None):
        path = get_settings_path()
        keyword_weight = False
        search_depth = 4000
        snippet_size = 250
        default_search_path = ""
        language = "English"
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
                keyword_weight = data.get("keyword_weight", False)
                search_depth = data.get("search_depth", 4000)
                snippet_size = data.get("snippet_size", 250)
                default_search_path = data.get("default_search_path", "~")
                language = data.get("language", "English")

        # ProjectData updaten
        ProjectData.set(
            keyword_weight=keyword_weight,
            search_depth=search_depth,
            snippet_size=snippet_size,
            default_search_path=default_search_path,
            language=language,
        )

        # Optional: Widgets in SettingsWindow setzen
        if window:
            window.keyword_weight.setChecked(keyword_weight)
            window.search_depth.setText(str(search_depth))
            window.snippet_size.setText(str(snippet_size))
            window.default_search_path.setText(default_search_path)
            # Prüfe ob die Sprache im ComboBox vorhanden ist
            index = window.language.findText(language)
            if index != -1:
                window.language.setCurrentIndex(index)