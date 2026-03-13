import sys
from PySide6.QtWidgets import QApplication
from Controller.main_page_controller import MainPageController
from View.main_page import MainPage
from Service.font_awesome_service import FontAwesomeService
from View.theme_manager import ThemeManager
from project_data import ProjectData
from language import Language
from settings import Settings


class Main:
    def __init__(self, my_app):  # 👈 app Parameter
        self.app = my_app


        Settings.load_settings()

        # Sprache laden
        Language.load(ProjectData.language)
        print(f"✅ {Language.get_language('MainPage', 'noPathMessage')}")


        # Fonts
        self.font_awesome_7 = FontAwesomeService.load_font_awesome_free()
        self.python_font = FontAwesomeService.load_python_selfmade()

        # Theme
        ThemeManager().initialize(self.app)  # 👈 self.app

        # Controller
        self.main_page_controller = MainPageController()

        # MainPage erstellen und anzeigen
        self.main_page = MainPage(self.main_page_controller)
        self.main_page.show()


        print("✅ Main fertig")

    def run(self):
        return self.app.exec()  # 👈 self.app


    def load_and_reload_page(self):
        # Controller
        self.main_page_controller = MainPageController()

        # MainPage erstellen und anzeigen
        self.main_page = MainPage(self.main_page_controller)
        self.main_page.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("KeySearch")
    app.setApplicationDisplayName("KeySearch")

    main_app = Main(app)  # 👈 app übergeben
    sys.exit(main_app.run())