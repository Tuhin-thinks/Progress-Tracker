import sys
from PySide2.QtWidgets import QMainWindow, QApplication


from UI import ui_home

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = ui_home.Ui_MainWindow()
        self.ui.setupUi(self)

        # TODO connect signals and slots

        # TODO fetch ui_data from database (call schema using get_ui_data())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())