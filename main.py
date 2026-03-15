import multiprocessing
import os
import sys
from PySide6.QtWidgets import QApplication
from Controller.main_page_controller import MainPageController
from View.main_page import MainPage
from Service.font_awesome_service import FontAwesomeService
from View.theme_manager import ThemeManager
from project_data import ProjectData
from language import Language
from settings import Settings

# Auf das Verzeichnis der EXE/App wechseln
if getattr(sys, 'frozen', False):
    # Wir sind in einer PyInstaller-Binary
    # Gehe von MacOS/ nach Resources/
    base_path = os.path.dirname(sys.executable)
    work_path = os.path.join(base_path, '..', 'Resources')
    os.chdir(work_path)
    print(f"✅ Arbeitsverzeichnis: {work_path}")  # Zum Debuggen
else:
    # Wir sind im Entwicklungsmodus
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"✅ Entwicklungsmodus: {os.getcwd()}")


class Main:
    def __init__(self, my_app):
        self.app = my_app

        # Load Settings and save them into Project_Data class
        Settings.load_settings()

        # Load Languages from Project Data
        Language.load(ProjectData.language)

        # Fonts
        self.font_awesome_7 = FontAwesomeService.load_font_awesome_free()

        # Theme Manager start
        ThemeManager().initialize(self.app)

        # Controller instance
        self.main_page_controller = MainPageController()

        # MainPage instance and show
        self.main_page = MainPage(self.main_page_controller)
        self.main_page.show()


        print("✅ Main App initialized. Starting...")

    def run(self):
        return self.app.exec()



if __name__ == "__main__":
    # PyInstaller startet sonst startet er mehrere Instanzen der App!
    multiprocessing.freeze_support()

    app = QApplication(sys.argv)
    app.setApplicationName("SelfSearch")
    app.setApplicationDisplayName("SelfSearch")

    main_app = Main(app)
    sys.exit(main_app.run())