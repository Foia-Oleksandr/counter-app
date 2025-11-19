import sys

from PySide6 import QtWidgets, QtGui

from counter_app.AtomsView import AtomsView
from counter_app.ViewController import ViewController
from counter_app.ui_gen.ui_MainWindow import Ui_MainWindow

from counter_app._version import __version__
from counter_app.view_chanel_data import subscribe_view_changed


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)

        # Set value of counter
        self.counter = 0
        self.update_counter()

        # Bind
        self.btn_inc.clicked.connect(self.inc)
        self.btn_dec.clicked.connect(self.dec)
        self.btn_reset.clicked.connect(self.reset)

        self.atomsView = AtomsView(self.atomsViewArea)

        view_controller = ViewController(self)
        subscribe_view_changed(view_controller.show_view)

        # Show the version in the status bar
        self.statusbar.showMessage(f"Version v{__version__}")

    def update_counter(self):
        self.label.setText(str(self.counter))

    def inc(self):
        self.counter += 1
        self.update_counter()

    def dec(self):
        self.counter -= 1
        self.update_counter()

    def reset(self):
        self.counter = 0
        self.update_counter()
        self.atomsView.reset_view()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icons/counter.ico'))
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
