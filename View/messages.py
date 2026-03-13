from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap

class Messages:

    @staticmethod
    def set_self_destroying_message(parent: QWidget, text: str, duration: int = 3000) -> None:
        colors = parent.colors

        # Container als Child-Widget
        container = QWidget(parent)

        layout = QVBoxLayout(container)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)

        # Haupt-Widget für Text + Icon
        msg_widget = QWidget()
        msg_layout = QHBoxLayout(msg_widget)
        msg_layout.setAlignment(Qt.AlignCenter)
        msg_layout.setContentsMargins(25, 20, 25, 20)
        msg_layout.setSpacing(15)

        # Icon
        icon_label = QLabel()
        python_icon = QPixmap("assets/img/pythonFett.png")
        python_icon = python_icon.scaled(32, 32, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(python_icon)

        # Text
        text_label = QLabel(text)
        text_label.setWordWrap(True)

        msg_layout.addWidget(icon_label)
        msg_layout.addWidget(text_label)
        layout.addWidget(msg_widget)

        # Style
        msg_widget.setStyleSheet(f"""
            QWidget {{
                background-color: {colors.UI.CONTAINER_BG.name()};
                border: 2px solid {colors.Primary.MAIN.name()};
                border-radius: 8px;
            }}
            QLabel {{
                color: {colors.Text.PRIMARY.name()};
                font-size: 16px;
                font-weight: 500;
                border: none;
            }}
        """)

        container.show()
        container.adjustSize()

        # Zentrieren über Parent
        x = (parent.width() - container.width()) // 2
        y = (parent.height() - container.height()) // 2
        container.move(x, y)

        # Einfach nach duration löschen
        QTimer.singleShot(duration, container.deleteLater)

    def set_no_path_selected(parent, duration=500):
        """
        Macht den Path-Button und Label kurz dezent rot und setzt danach den normalen Style zurück.
        """
        btn = parent.path_btn
        path = parent.path
        colors = parent.colors

        # Dezentes Rot
        alert_color = "#d9534f"

        # Button kurz rot
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {colors.UI.INPUT_BG.name()};
                border: 2px solid {alert_color};
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 14px;
                color: {alert_color};
                font-weight: bold;
                font-family: "Font Awesome 7 Free";
            }}
        """)

        # Label kurz rot
        path.setStyleSheet(f"color: {alert_color}; font-size: 14px;")

        # Nach duration wieder normalen Style
        QTimer.singleShot(duration, parent.update_path_button_style)
        QTimer.singleShot(duration, parent.update_pfad_label_style)