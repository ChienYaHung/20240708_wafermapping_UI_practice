# -*- coding: utf-8 -*-
import sys
import os

from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
#                             QMetaObject, QObject, QPoint, QRect,
#                             QSize, QTime, QUrl, Qt, QFile, QIODevice)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#                            QFont, QFontDatabase, QGradient, QIcon,
#                            QImage, QKeySequence, QLinearGradient, QPainter,
#                            QPalette, QPixmap, QRadialGradient, QTransform, QColor, QFont)
# from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
#                                QHBoxLayout, QHeaderView, QLabel, QLineEdit,
#                                QMainWindow, QMenuBar, QPushButton, QRadioButton,
#                                QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
#                                QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox)
from mainUI import *


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":

    # 建立QApplication物件，管理UI內各種widget
    app = QApplication(sys.argv)

    # 將UI實體化
    myWin = MyMainWindow()

    # 顯示UI
    myWin.show()

    # app.exec()開啟app
    # exec():使app 進入loop並保持開啟，直到exit()被呼叫
    sys.exit(app.exec())
