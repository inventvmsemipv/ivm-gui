import PyQt5
dir(PyQt5)
from PyQt5 import QtWidgets as qtw
#from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

# Only needed for access to command line arguments
import sys

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test App")
        button = qtw.QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = qtw.QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()
