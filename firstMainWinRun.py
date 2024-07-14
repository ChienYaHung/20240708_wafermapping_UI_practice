# -*- coding: utf-8 -*-
from mainUI import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import *
import sys
import os
import ntpath


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


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 初始參數
        self.selected_wafer = None
        self.df_all_ma2 = pd.DataFrame()
        self.select_draw_parameter = 'Ir1'

        # 設定狀態列
        self.read_wafer_status_label = QLabel('尚未讀取任何檔案')
        self.chip_count_status_label = QLabel('Chip數：0')
        self.statusBar_chip_count = QStatusBar()
        # self.wafer_count_bar.setMinimumWidth(80)
        self.wafer_count_bar.addWidget(self.statusBar_chip_count)
        self.wafer_count_bar.addWidget(self.read_wafer_status_label)
        self.statusBar_chip_count.addWidget(self.chip_count_status_label)

        # 上下限只能打數字
        self.min_spec_input.setValidator(QDoubleValidator(-9999, 9999, 2))
        self.max_spec_input.setValidator(QDoubleValidator(-9999, 9999, 2))

        # slot區
        self.read_data_button.clicked.connect(
            self.read_ma2_CSV)  # 儲存資訊至表格
        self.wafer_id_box.activated.connect(
            lambda x: self.set_Wafer_Select(self.wafer_id_box))
        self.view_item_box.activated.connect(
            lambda x: self.set_Parameter_Select(self.view_item_box))
        self.mapping_button.clicked.connect(
            lambda x: self.draw_Wafer_Mapping(self.df_all_ma2, self.selected_wafer, self.select_draw_parameter))

    # 讀ma2檔
    @Slot()
    def read_ma2_CSV(self):

        # 取得讀檔路徑
        read_ma2_list, _ = QFileDialog.getOpenFileNames(self, caption='開啟舊檔', dir=os.path.expanduser("~/Desktop"),
                                                        filter="CSV UTF-8(逗號分隔)(*.csv)")
        # 初始化ma2 list
        self.df_ma2_list = []

        # 建立所有ma2的dataframe
        self.set_ma2_dataframe(read_ma2_list)

        # 呼叫"將ma2檔檔名加入下拉式清單"
        self.add_combobox_item(self.wafer_name_list)

        # 呼叫"狀態列設定"
        self.set_status_bar_text(self.df_all_ma2, self.wafer_name_list)

        # 初始參數設定
        self.selected_wafer = self.wafer_name_list[0]

        # 測試訊息
        # self.test_meaasge_box.setPlainText(str(self.df_all_ma2.shape))

    # 使用下拉式選單選wafer後，寫入參數內

    @Slot()
    def set_Wafer_Select(self, combo_box: QComboBox) -> None:
        self.selected_wafer = combo_box.currentText()
        self.test_meaasge_box.setPlainText(str(self.selected_wafer))

    # 使用下拉式選單選繪圖項目後，寫入參數內
    @Slot()
    def set_Parameter_Select(self, combo_box: QComboBox) -> None:
        self.select_draw_parameter = combo_box.currentText()
        self.test_meaasge_box.setPlainText(str(self.select_draw_parameter))

    # 繪製wafer mapping圖
    def draw_Wafer_Mapping(self, all_wafer_data: pd.DataFrame, wafer: str, draw_item):

        if self.selected_wafer:
            # 取出指定wafer
            df_select_wafer = all_wafer_data[all_wafer_data['Wafer ID'] == wafer].copy(
            )
            # 將df轉為二維
            df_select_wafer_2d = df_select_wafer.pivot_table(
                index='Y', columns='X', values=draw_item, fill_value=-200, observed=True)

            # mask
            wafer_2d_array = df_select_wafer_2d.to_numpy(copy=True)
            wafer_masked = np.ma.masked_where(
                wafer_2d_array == -200, wafer_2d_array)

            plt.figure(1)
            plt.imshow(wafer_masked, interpolation='none')
            plt.colorbar()

            plt.show()
        else:
            self.draw_before_read_file_message()

    # TODO:圖檔標題為繪製項目
    # TODO:視窗名稱為wafer ID
    # TODO:滑過wafer mapping時顯示相關資訊

    # 沒有讀檔就畫圖的警告
    def draw_before_read_file_message(self):
        msgBox = QMessageBox.warning(
            self, '無法繪圖', '請先選擇並讀取ma2檔', QMessageBox.Ok, QMessageBox.Ok)

    # csv檔轉為dataframe
    def set_ma2_dataframe(self, ma2_list):

        self.wafer_name_list = []

        for ma2_path in ma2_list:

            # 讀檔
            df_single_wafer = pd.read_csv(ma2_path, header=7, index_col=False,
                                          usecols=['SN', 'Vf1', 'Vf2', 'Vr1', 'Ir1', 'Rs',
                                                   'Iv2', 'Wd2', 'Wp2', 'Iv3', 'X', 'Y', 'Vf0'],
                                          dtype={'SN': 'category', 'X': 'category', 'Y': 'category'})

            # 取出wafer名稱
            file_name = self.path_leaf(ma2_path)
            wafer_id, a = file_name.split(".")

            # 建立wafer name欄位
            df_single_wafer['Wafer ID'] = wafer_id

            # 加入list
            self.df_ma2_list.append(df_single_wafer)
            self.wafer_name_list.append(wafer_id)

        # 建立含有所有wafer資訊之df
        self.df_all_ma2 = pd.concat(self.df_ma2_list, ignore_index=True)

    # 取出文件最後的檔名
    def path_leaf(self, path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)

    # 將ma2檔檔名加入下拉式清單
    def add_combobox_item(self, wafer_list):
        self.wafer_id_box.clear()
        self.wafer_id_box.addItems(wafer_list)

    # 狀態列顯示讀取檔案數量
    def set_status_bar_text(self, df: pd.DataFrame, wafer_list: list):

        wafer_count = len(wafer_list)
        chip_count = df.shape[0]

        # 設定狀態列內容
        self.read_wafer_status_label.setText(f'讀取Wafer數量:{wafer_count}')
        self.chip_count_status_label.setText(f'讀取Chip數量:{chip_count}')


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
