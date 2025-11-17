import sys

from PySide6 import QtWidgets, QtGui

from counter_app.ui_gen.ui_MainWindow import Ui_MainWindow

from counter_app._version import __version__

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PyQt6.QtWinExtras import QtWin
    myappid = 'com.learnpyqt.examples.counter'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass


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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icons/counter.ico'))
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
 