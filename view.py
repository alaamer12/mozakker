import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QTimer, QEasingCurve


class View(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: #333; color: white; padding: 10px; border-radius: 5px;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        self.label = QLabel("Hello, world!")
        layout.addWidget(self.label)

        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setStartValue(QRect(800, 1000, 200, 50))
        self.animation.setEndValue(self.calculate_end_position())
        self.animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.hide_notification)

    def calculate_end_position(self):
        desktop = QApplication.desktop()
        screen_geometry = desktop.screenGeometry()
        window_geometry = self.geometry()
        x = screen_geometry.width() - window_geometry.width() - 10  # 10 pixels margin
        y = screen_geometry.height() - window_geometry.height() - 10  # 10 pixels margin
        return QRect(x, y, window_geometry.width(), window_geometry.height())

    def showEvent(self, event):
        self.animation.start()
        self.timer.start(3000)  # Hide after 3 seconds

    def hide_notification(self):
        self.animation.setStartValue(self.geometry())
        self.animation.setEndValue(QRect(800, 1000, 200, 50))
        self.animation.finished.connect(self.hide)
        self.animation.start()

    def main(self, app):
        self.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = View(None)
    view.main(app)
