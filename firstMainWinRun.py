# -*- coding: utf-8 -*-
from mainUI import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_bases import *
import pandas as pd
from PySide6.QtWidgets import *
from PySide6.QtGui import *
# from PySide6.QtUiTools import QUiLoader
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
        # self.img_max_value = None
        # self.img_min_value = None
        self.select_draw_parameter = 'Ir1'  # 先設定需繪圖項目，預設為Ir1
        self.table_item = ['Wafer ID', 'X', 'Y', 'Vf1',
                           'Vf2', 'Vr1', 'Ir1', 'Rs', 'Iv2', 'Wd2', 'Vf0']  # 表格內的對應項目
        # self.df_all_ma2 = pd.DataFrame()  # 空的dataframe, 拿來裝所有wafer的mapping資訊
        self.df_specific_ma2 = pd.DataFrame(
            columns=self.table_item)  # 空的dataframe, 拿來裝被選取的chip資訊

        # 設定狀態列
        self.read_wafer_status_label = QLabel('尚未讀取任何Chip')
        self.chip_count_status_label = QLabel('尚未擷取任何檔案')
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
        if read_ma2_list:  # 如果有選擇檔案
            # 測試訊息
            # self.test_meaasge_box.setPlainText(str(read_ma2_list))

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
        else:
            self.no_read_file_message()

    # 使用下拉式選單選wafer後，寫入參數內
    @Slot()
    def set_Wafer_Select(self, combo_box: QComboBox) -> None:
        self.selected_wafer = combo_box.currentText()
        # self.test_meaasge_box.setPlainText(str(self.selected_wafer))  # 測試訊息

    # 使用下拉式選單選繪圖項目後，寫入參數內
    @Slot()
    def set_Parameter_Select(self, combo_box: QComboBox) -> None:
        self.select_draw_parameter = combo_box.currentText()
        # self.test_meaasge_box.setPlainText(
        #     str(self.select_draw_parameter))  # 測試訊息

    # 繪製wafer mapping圖
    @Slot()
    def draw_Wafer_Mapping(self, all_wafer_data: pd.DataFrame, wafer: str, draw_item):

        # 判斷是否有讀檔
        # selected_wafer是否有被賦值
        if self.selected_wafer:

            # 設定最大/最小值
            self.img_max_value = self.max_spec_input.text()
            self.img_min_value = self.min_spec_input.text()

            # 判斷上下限是否設定完全
            if (len(self.img_max_value) == 0 and len(self.img_min_value) != 0) or (
                    len(self.img_max_value) != 0 and len(self.img_min_value) == 0):

                self.only_single_limit_message()  # 上下限設定不完全則直接退出

            else:
                # self.test_meaasge_box.setPlainText(
                #     f'最小值: {self.img_min_value}\n最大值: {self.img_max_value}\n最小值格式: {type(self.img_min_value)}\n最大值格式: {type(self.img_max_value)}')

                # 取出指定wafer
                self.df_select_wafer = all_wafer_data[all_wafer_data['Wafer ID'] == wafer].copy(
                )

                # 設定index
                self.df_select_wafer.set_index(keys='XY index', inplace=True)

                # 測試
                # self.df_select_wafer.to_clipboard()

                # 設定該wafer的最大/最小之XY座標
                x_range = list(self.df_select_wafer['X'].cat.categories)
                y_range = list(self.df_select_wafer['Y'].cat.categories)

                # 將df轉為二維
                df_select_wafer_2d = self.df_select_wafer.pivot_table(
                    index='Y', columns='X', values=draw_item, fill_value=-200, observed=True)

                # mask，標示t-key
                wafer_2d_array = df_select_wafer_2d.to_numpy(copy=True)
                wafer_masked = np.ma.masked_where(
                    wafer_2d_array == -200, wafer_2d_array)

                # 繪圖
                fig = plt.figure(figsize=(12, 9))  # 建立figure
                ax = fig.add_subplot(111)  # 建立axes
                fig.suptitle(f'{wafer} {draw_item} mapping')  # 設定圖檔標題
                im = plt.pcolormesh(
                    x_range, y_range, wafer_masked, cmap='jet', shading='nearest', edgecolors='black')  # 圖像繪製
                # ax.tick_params(axis='both', which='both',
                #                bottom=False, top=False, labelbottom=False)

                # 將上下限加入圖表內
                if self.img_max_value and self.img_min_value:

                    self.img_max_value = float(self.max_spec_input.text())
                    self.img_min_value = float(self.min_spec_input.text())

                    im.set_clim(vmin=self.img_min_value,
                                vmax=self.img_max_value)

                plt.colorbar()
                binding_id = plt.connect(
                    'motion_notify_event', self.mouse_on_move)  # 設定滑鼠滑動與function的connection
                plt.connect('button_press_event', self.mouse_on_click)
                # plt.axis('off')

                plt.show()

        # 若沒有讀檔就繪圖，顯示錯誤訊息
        else:
            self.draw_before_read_file_message()

    # 沒有讀檔就畫圖的警告
    def draw_before_read_file_message(self):
        msgBox = QMessageBox.information(
            self, '無法繪圖', '請先讀取並選擇ma2檔', QMessageBox.Ok, QMessageBox.Ok)

    # 開啟讀檔介面後沒讀檔的警告
    def no_read_file_message(self):
        msgBox = QMessageBox.question(
            self, '沒有讀檔', '你怎麼叫出介面又不選檔案？', QMessageBox.Ok, QMessageBox.Ok)

    # 只設定上限或下限的警告
    def only_single_limit_message(self):
        msgBox = QMessageBox.warning(
            self, '上下限設定錯誤', '只有設定上限或下限', QMessageBox.Ok, QMessageBox.Ok)

    # csv檔轉為dataframe
    def set_ma2_dataframe(self, ma2_list):

        self.wafer_name_list = []

        for ma2_path in ma2_list:

            # 讀檔
            df_single_wafer = pd.read_csv(ma2_path, header=7, index_col=False,
                                          usecols=['SN', 'Vf1', 'Vf2', 'Vr1', 'Ir1', 'Rs',
                                                   'Iv2', 'Wd2', 'Wp2', 'Iv3', 'X', 'Y', 'Vf0'],
                                          dtype={'SN': 'category'})

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

        # 建立唯一的xy軸索引
        self.df_all_ma2['XY index'] = self.df_all_ma2['X'].apply(
            lambda x: 'X' + str(x)) + self.df_all_ma2['Y'].apply(lambda y: 'Y' + str(y))

        # 將X/Y設為category
        self.df_all_ma2['X'] = self.df_all_ma2['X'].astype(dtype='category')
        self.df_all_ma2['Y'] = self.df_all_ma2['Y'].astype(dtype='category')
        self.df_all_ma2['XY index'] = self.df_all_ma2['XY index'].astype(
            dtype='category')

        # 測試
        # self.df_all_ma2.to_clipboard()

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
        self.chip_count_status_label.setText(
            f'讀取Wafer數量:{wafer_count}  讀取Chip數量:{chip_count}')
        # self.chip_count_status_label.setText(f'讀取Chip數量:{chip_count}')

    # 滑動滑鼠的motion
    # 將df內對應資訊填入表格內
    def mouse_on_move(self, event: MouseEvent):
        if event.inaxes:

            xy_index_of_mouse = self.get_mouse_cord(event)  # 將鼠標位置轉換為index

            # 找出index的df內對應資訊
            for i, item_name in enumerate(self.table_item):

                try:
                    # 若index有對應資訊

                    # 找出df內對應項目
                    _item_of_mouse = self.df_select_wafer.loc[xy_index_of_mouse, item_name]
                    # 需轉成Item格式
                    _item_of_view_table = QTableWidgetItem(f'{_item_of_mouse}')
                    # 設定table item為read-only
                    _item_of_view_table.setFlags(
                        _item_of_view_table.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    # 寫入表格
                    self.view_data_table.setItem(0, i, _item_of_view_table)

                except KeyError:
                    # 若index沒有對應資訊
                    # 啥也不做，也不更新資料
                    pass

    # TODO:點選chip後可以儲存chip資訊
    def mouse_on_click(self, event: MouseEvent):

        # 當按下左鍵
        # 儲存所在地chip資訊
        if event.button is MouseButton.LEFT:

            xy_index_of_mouse = self.get_mouse_cord(event)  # 將鼠標位置轉換為index

            try:

                # 擷取chip資訊，順驗驗證index是否有對應項目
                _series_of_mouse = self.df_select_wafer.loc[xy_index_of_mouse]

                '''
                若index有對應資訊
                '''

                # 表格多插入一列
                row_count = self.specific_chip_table.rowCount()
                self.specific_chip_table.insertRow(row_count)

                for i, item_name in enumerate(self.table_item):

                    # 找出df內對應項目
                    _item_of_mouse = self.df_select_wafer.loc[xy_index_of_mouse, item_name]

                    '''
                        此處處理UI表格部分
                        按下左鍵後表格會寫入chip資訊
                        '''

                    # 需轉成Item格式
                    _item_of_specific_table = QTableWidgetItem(
                        f'{_item_of_mouse}')
                    # 設定table item為read-only
                    _item_of_specific_table.setFlags(
                        _item_of_specific_table.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    # 寫入表格
                    self.specific_chip_table.setItem(
                        row_count, i, _item_of_specific_table)

                '''
                    此處處理df表格部分
                    按下左鍵後df會寫入chip資訊
                    (不在迴圈內)
                '''
                self.df_specific_ma2.loc[len(
                    self.df_specific_ma2)] = _series_of_mouse

                # 測試用，檢查df
                self.df_specific_ma2.to_clipboard()

                # 顯示"已儲存chip相關資訊"
                self.read_wafer_status_label.setText(
                    f'已擷取Chip數量:{len(self.df_specific_ma2)}')

            except KeyError:
                '''
                若index沒有對應資訊
                '''
                # 啥也不做，也不更新資料
                pass

        # 當在圖面按下右鍵
        # 刪除最後一筆chip資訊
        elif event.button is MouseButton.RIGHT:

            '''
            此處處理UI表格部分
            按下右鍵後會刪除UI最後一列資訊
            '''
            row_count_2 = self.specific_chip_table.rowCount()-1
            self.specific_chip_table.removeRow(row_count_2)

            '''
            此處處理df表格部分
            按下右鍵後會刪除df最後一列資訊
            '''
            self.df_specific_ma2 = self.df_specific_ma2[:-1]

            # 顯示"已儲存chip相關資訊"
            self.read_wafer_status_label.setText(
                f'已擷取Chip數量:{len(self.df_specific_ma2)}')

            # 測試用，檢查df
            self.df_specific_ma2.to_clipboard()

    # 得到鼠標現在座標
    def get_mouse_cord(self, event: MouseEvent):

        # 回傳鼠標所在地的XY座標
        x_cord_of_mouse = int(np.round(event.xdata, 0))
        y_cord_of_mouse = int(np.round(event.ydata, 0))

        # 設定XY index
        # 指向df內的資訊
        xy_index_of_mouse = f'X{x_cord_of_mouse}Y{y_cord_of_mouse}'

        # 測試訊息
        # self.test_meaasge_box.setPlainText(f'X座標: {x_cord_of_mouse}\nY座標:
        #                                    {y_cord_of_mouse}\n{xy_index_of_mouse}')

        return xy_index_of_mouse

    # TODO:儲存擷取chip相關資訊
    # TODO:將mapping圖放入UI內


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
