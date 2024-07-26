# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainUI.ui'
##
# Created by: Qt User Interface Compiler version 6.6.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                               QHeaderView, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
                               QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(976, 613)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 0))
        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(40, 20, 901, 569))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_8 = QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_3.addWidget(self.label_8)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.wafer_id_box = QComboBox(self.verticalLayoutWidget_4)
        self.wafer_id_box.setObjectName(u"wafer_id_box")

        self.horizontalLayout_4.addWidget(self.wafer_id_box)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.view_item_box = QComboBox(self.verticalLayoutWidget_4)
        self.view_item_box.addItem("")
        self.view_item_box.addItem("")
        self.view_item_box.addItem("")
        self.view_item_box.addItem("")
        self.view_item_box.addItem("")
        self.view_item_box.addItem("")
        self.view_item_box.addItem("")
        self.view_item_box.addItem("")
        self.view_item_box.addItem("")
        self.view_item_box.setObjectName(u"view_item_box")

        self.horizontalLayout_5.addWidget(self.view_item_box)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.max_spec_input = QLineEdit(self.verticalLayoutWidget_4)
        self.max_spec_input.setObjectName(u"max_spec_input")
        self.max_spec_input.setInputMethodHints(Qt.ImhDigitsOnly)

        self.horizontalLayout.addWidget(self.max_spec_input)

        self.horizontalSpacer = QSpacerItem(
            300, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.min_spec_input = QLineEdit(self.verticalLayoutWidget_4)
        self.min_spec_input.setObjectName(u"min_spec_input")
        self.min_spec_input.setInputMethodHints(Qt.ImhDigitsOnly)

        self.horizontalLayout_2.addWidget(self.min_spec_input)

        self.horizontalSpacer_2 = QSpacerItem(
            300, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.verticalLayoutWidget_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.horizontalSpacer_5 = QSpacerItem(
            80, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.read_data_button = QPushButton(self.verticalLayoutWidget_4)
        self.read_data_button.setObjectName(u"read_data_button")
        self.read_data_button.setMinimumSize(QSize(100, 0))
        self.read_data_button.setFont(font)

        self.verticalLayout_5.addWidget(self.read_data_button)

        self.mapping_button = QPushButton(self.verticalLayoutWidget_4)
        self.mapping_button.setObjectName(u"mapping_button")
        self.mapping_button.setFont(font)

        self.verticalLayout_5.addWidget(self.mapping_button)

        self.save_chip_info_button = QPushButton(self.verticalLayoutWidget_4)
        self.save_chip_info_button.setObjectName(u"save_chip_info_button")
        self.save_chip_info_button.setFont(font)

        self.verticalLayout_5.addWidget(self.save_chip_info_button)

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_6 = QSpacerItem(
            80, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(
            20, 30, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.line = QFrame(self.verticalLayoutWidget_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(
            20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.view_data_table = QTableWidget(self.verticalLayoutWidget_4)
        if (self.view_data_table.columnCount() < 11):
            self.view_data_table.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.view_data_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.view_data_table.rowCount() < 1):
            self.view_data_table.setRowCount(1)
        self.view_data_table.setObjectName(u"view_data_table")
        self.view_data_table.setMinimumSize(QSize(0, 40))
        self.view_data_table.setFocusPolicy(Qt.NoFocus)
        self.view_data_table.setInputMethodHints(Qt.ImhNone)
        self.view_data_table.setAutoScroll(True)
        self.view_data_table.setRowCount(1)
        self.view_data_table.horizontalHeader().setDefaultSectionSize(80)
        self.view_data_table.horizontalHeader().setHighlightSections(False)
        self.view_data_table.verticalHeader().setVisible(False)
        self.view_data_table.verticalHeader().setCascadingSectionResizes(False)
        self.view_data_table.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.view_data_table)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.verticalLayoutWidget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.specific_chip_table = QTableWidget(self.verticalLayoutWidget_4)
        if (self.specific_chip_table.columnCount() < 11):
            self.specific_chip_table.setColumnCount(11)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            9, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.specific_chip_table.setHorizontalHeaderItem(
            10, __qtablewidgetitem21)
        # if (self.specific_chip_table.rowCount() < 1):
        #     self.specific_chip_table.setRowCount(1)
        self.specific_chip_table.setObjectName(u"specific_chip_table")
        self.specific_chip_table.setMinimumSize(QSize(0, 40))
        self.specific_chip_table.setFocusPolicy(Qt.NoFocus)
        self.specific_chip_table.setInputMethodHints(Qt.ImhNone)
        self.specific_chip_table.setAutoScroll(True)
        self.specific_chip_table.setRowCount(0)
        self.specific_chip_table.horizontalHeader().setDefaultSectionSize(80)
        self.specific_chip_table.horizontalHeader().setHighlightSections(False)
        self.specific_chip_table.verticalHeader().setVisible(False)
        self.specific_chip_table.verticalHeader().setCascadingSectionResizes(False)
        self.specific_chip_table.verticalHeader().setHighlightSections(False)

        self.verticalLayout.addWidget(self.specific_chip_table)

        self.verticalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.wafer_count_bar = QStatusBar(MainWindow)
        self.wafer_count_bar.setObjectName(u"wafer_count_bar")
        MainWindow.setStatusBar(self.wafer_count_bar)

        self.retranslateUi(MainWindow)

        self.view_item_box.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"Wafer mapping", None))
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Wafer ID:", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"\u7e6a\u5716\u9805\u76ee\uff1a", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Color Bar \u4e0a\u9650\uff1a", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Color Bar \u4e0b\u9650\uff1a", None))
        self.view_item_box.setItemText(
            0, QCoreApplication.translate("MainWindow", u"Vf1", None))
        self.view_item_box.setItemText(
            1, QCoreApplication.translate("MainWindow", u"Vf2", None))
        self.view_item_box.setItemText(
            2, QCoreApplication.translate("MainWindow", u"Vr1", None))
        self.view_item_box.setItemText(
            3, QCoreApplication.translate("MainWindow", u"Ir1", None))
        self.view_item_box.setItemText(
            4, QCoreApplication.translate("MainWindow", u"Rs", None))
        self.view_item_box.setItemText(
            5, QCoreApplication.translate("MainWindow", u"Iv2", None))
        self.view_item_box.setItemText(
            6, QCoreApplication.translate("MainWindow", u"Wd2", None))
        self.view_item_box.setItemText(
            7, QCoreApplication.translate("MainWindow", u"Wp2", None))
        self.view_item_box.setItemText(
            8, QCoreApplication.translate("MainWindow", u"Vf0", None))

        self.read_data_button.setText(QCoreApplication.translate(
            "MainWindow", u"\u8b80\u53d6\u6a94\u6848", None))
        self.mapping_button.setText(QCoreApplication.translate(
            "MainWindow", u"\u7e6a\u88fd\u5716\u50cf", None))
        self.save_chip_info_button.setText(QCoreApplication.translate(
            "MainWindow", u"\u5132\u5b58chip\u8cc7\u8a0a", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Data table", None))
        ___qtablewidgetitem = self.view_data_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate(
            "MainWindow", u"\u7247\u865f", None))
        ___qtablewidgetitem1 = self.view_data_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"X", None))
        ___qtablewidgetitem2 = self.view_data_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"Y", None))
        ___qtablewidgetitem3 = self.view_data_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", u"Vf1", None))
        ___qtablewidgetitem4 = self.view_data_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"Vf2", None))
        ___qtablewidgetitem5 = self.view_data_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(
            QCoreApplication.translate("MainWindow", u"Vr1", None))
        ___qtablewidgetitem6 = self.view_data_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(
            QCoreApplication.translate("MainWindow", u"Ir1", None))
        ___qtablewidgetitem7 = self.view_data_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(
            QCoreApplication.translate("MainWindow", u"Rs", None))
        ___qtablewidgetitem8 = self.view_data_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(
            QCoreApplication.translate("MainWindow", u"Iv2", None))
        ___qtablewidgetitem9 = self.view_data_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(
            QCoreApplication.translate("MainWindow", u"Wd2", None))
        ___qtablewidgetitem10 = self.view_data_table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(
            QCoreApplication.translate("MainWindow", u"Vf0", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"\u88ab\u9078\u53d6chip\u7684\u8cc7\u8a0a", None))
        ___qtablewidgetitem11 = self.specific_chip_table.horizontalHeaderItem(
            0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate(
            "MainWindow", u"\u7247\u865f", None))
        ___qtablewidgetitem12 = self.specific_chip_table.horizontalHeaderItem(
            1)
        ___qtablewidgetitem12.setText(
            QCoreApplication.translate("MainWindow", u"X", None))
        ___qtablewidgetitem13 = self.specific_chip_table.horizontalHeaderItem(
            2)
        ___qtablewidgetitem13.setText(
            QCoreApplication.translate("MainWindow", u"Y", None))
        ___qtablewidgetitem14 = self.specific_chip_table.horizontalHeaderItem(
            3)
        ___qtablewidgetitem14.setText(
            QCoreApplication.translate("MainWindow", u"Vf1", None))
        ___qtablewidgetitem15 = self.specific_chip_table.horizontalHeaderItem(
            4)
        ___qtablewidgetitem15.setText(
            QCoreApplication.translate("MainWindow", u"Vf2", None))
        ___qtablewidgetitem16 = self.specific_chip_table.horizontalHeaderItem(
            5)
        ___qtablewidgetitem16.setText(
            QCoreApplication.translate("MainWindow", u"Vr1", None))
        ___qtablewidgetitem17 = self.specific_chip_table.horizontalHeaderItem(
            6)
        ___qtablewidgetitem17.setText(
            QCoreApplication.translate("MainWindow", u"Ir1", None))
        ___qtablewidgetitem18 = self.specific_chip_table.horizontalHeaderItem(
            7)
        ___qtablewidgetitem18.setText(
            QCoreApplication.translate("MainWindow", u"Rs", None))
        ___qtablewidgetitem19 = self.specific_chip_table.horizontalHeaderItem(
            8)
        ___qtablewidgetitem19.setText(
            QCoreApplication.translate("MainWindow", u"Iv2", None))
        ___qtablewidgetitem20 = self.specific_chip_table.horizontalHeaderItem(
            9)
        ___qtablewidgetitem20.setText(
            QCoreApplication.translate("MainWindow", u"Wd2", None))
        ___qtablewidgetitem21 = self.specific_chip_table.horizontalHeaderItem(
            10)
        ___qtablewidgetitem21.setText(
            QCoreApplication.translate("MainWindow", u"Vf0", None))
    # retranslateUi
