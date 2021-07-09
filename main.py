# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stardew_toolbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
"""
MIT License

Copyright (c) 2021 MSProgrammerPy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from toolbox import SAVES_PATH, ToolBox
import os

REPOSITORY = "https://github.com/MSProgrammerPy/stardew_toolbox"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # <------------------- MainWindow ------------------->
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        MainWindow.setFixedSize(800, 650)
        MainWindow.setWindowTitle("Stardew ToolBox")
        MainWindow.setAccessibleDescription("")

        # <------------------- centralwidget ------------------->
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAccessibleDescription("")
        self.centralwidget.setObjectName("centralwidget")

        # <------------------- tabWidget ------------------->
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 645))
        self.tabWidget.setAccessibleDescription("")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")

        # <------------------- ToolBox Tab ------------------->
        self.tab_toolbox = QtWidgets.QWidget()
        self.tab_toolbox.setAccessibleDescription("")
        self.tab_toolbox.setObjectName("tab_toolbox")

        # <------------------- Choose Save Frame ------------------->
        self.frm_choose_save = QtWidgets.QFrame(self.tab_toolbox)
        self.frm_choose_save.setGeometry(QtCore.QRect(0, 0, 800, 150))
        self.frm_choose_save.setAccessibleDescription("")
        self.frm_choose_save.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_choose_save.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_choose_save.setObjectName("frm_choose_save")

        # <------------------- Choose Save Label ------------------->
        self.lbl_choose_save = QtWidgets.QLabel(self.frm_choose_save)
        self.lbl_choose_save.setGeometry(QtCore.QRect(30, 60, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_choose_save.setFont(font)
        self.lbl_choose_save.setAccessibleDescription("")
        self.lbl_choose_save.setText("Choose your save:")
        self.lbl_choose_save.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lbl_choose_save.setObjectName("lbl_choose_save")

        # <------------------- Saves ComboBox ------------------->
        self.cb_saves = QtWidgets.QComboBox(self.frm_choose_save)
        self.cb_saves.setGeometry(QtCore.QRect(190, 64, 150, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cb_saves.setFont(font)
        self.cb_saves.setAccessibleDescription("")
        self.cb_saves.setCurrentText("")
        self.cb_saves.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cb_saves.setPlaceholderText("")
        self.cb_saves.setObjectName("cb_saves")

        for _save in os.listdir(SAVES_PATH):
            if os.path.isdir(os.path.join(SAVES_PATH, _save)):
                self.cb_saves.addItem(_save)

        self.cb_saves.currentIndexChanged.connect(self.update_line_edits_text)

        # <------------------- Profile GroupBox ------------------->
        self.gb_profile = QtWidgets.QGroupBox(self.tab_toolbox)
        self.gb_profile.setGeometry(QtCore.QRect(0, 152, 800, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gb_profile.setFont(font)
        self.gb_profile.setAccessibleDescription("")
        self.gb_profile.setTitle("Profile")
        self.gb_profile.setObjectName("gb_profile")

        # <------------------- Change Name Frame ------------------->
        self.frm_ch_name = QtWidgets.QFrame(self.gb_profile)
        self.frm_ch_name.setGeometry(QtCore.QRect(20, 30, 240, 180))
        self.frm_ch_name.setAccessibleDescription("")
        self.frm_ch_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ch_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ch_name.setObjectName("frm_ch_name")

        # <------------------- Change Name Label ------------------->
        self.lbl_ch_name = QtWidgets.QLabel(self.frm_ch_name)
        self.lbl_ch_name.setGeometry(QtCore.QRect(70, 30, 101, 30))
        self.lbl_ch_name.setAccessibleDescription("")
        self.lbl_ch_name.setText("Name")
        self.lbl_ch_name.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ch_name.setObjectName("lbl_ch_name")

        # <------------------- Change Name LineEdit ------------------->
        self.input_ch_name = QtWidgets.QLineEdit(self.frm_ch_name)
        self.input_ch_name.setGeometry(QtCore.QRect(50, 80, 140, 27))
        self.input_ch_name.setAccessibleDescription("")
        self.input_ch_name.setText("")
        self.input_ch_name.setObjectName("input_ch_name")

        # <------------------- Change Name Button ------------------->
        self.btn_ch_name = QtWidgets.QPushButton(self.frm_ch_name)
        self.btn_ch_name.setGeometry(QtCore.QRect(50, 125, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_name.setFont(font)
        self.btn_ch_name.setAccessibleDescription("")
        self.btn_ch_name.setText("Change")
        self.btn_ch_name.setObjectName("btn_ch_name")
        self.btn_ch_name.clicked.connect(self.change_name)

        # <------------------- Change Farm Name Frame ------------------->
        self.frm_ch_fname = QtWidgets.QFrame(self.gb_profile)
        self.frm_ch_fname.setGeometry(QtCore.QRect(280, 30, 240, 180))
        self.frm_ch_fname.setAccessibleDescription("")
        self.frm_ch_fname.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ch_fname.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ch_fname.setObjectName("frm_ch_fname")

        # <------------------- Change Farm Name Label ------------------->
        self.lbl_ch_fname = QtWidgets.QLabel(self.frm_ch_fname)
        self.lbl_ch_fname.setGeometry(QtCore.QRect(60, 30, 121, 30))
        self.lbl_ch_fname.setAccessibleDescription("")
        self.lbl_ch_fname.setText("Farm Name")
        self.lbl_ch_fname.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ch_fname.setObjectName("lbl_ch_fname")

        # <------------------- Change Farm Name LineEdit ------------------->
        self.input_ch_fname = QtWidgets.QLineEdit(self.frm_ch_fname)
        self.input_ch_fname.setGeometry(QtCore.QRect(50, 80, 140, 27))
        self.input_ch_fname.setAccessibleDescription("")
        self.input_ch_fname.setText("")
        self.input_ch_fname.setObjectName("input_ch_fname")

        # <------------------- Change Farm Name Button ------------------->
        self.btn_ch_fname = QtWidgets.QPushButton(self.frm_ch_fname)
        self.btn_ch_fname.setGeometry(QtCore.QRect(50, 125, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_fname.setFont(font)
        self.btn_ch_fname.setAccessibleDescription("")
        self.btn_ch_fname.setText("Change")
        self.btn_ch_fname.setObjectName("btn_ch_fname")
        self.btn_ch_fname.clicked.connect(self.change_farm_name)

        # <------------------- Change Favorite Thing Frame ------------------->
        self.frm_ch_fthing = QtWidgets.QFrame(self.gb_profile)
        self.frm_ch_fthing.setGeometry(QtCore.QRect(540, 30, 240, 180))
        self.frm_ch_fthing.setAccessibleDescription("")
        self.frm_ch_fthing.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ch_fthing.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ch_fthing.setObjectName("frm_ch_fthing")

        # <------------------- Change Favorite Thing Label ------------------->
        self.lbl_ch_fthing = QtWidgets.QLabel(self.frm_ch_fthing)
        self.lbl_ch_fthing.setGeometry(QtCore.QRect(50, 30, 141, 30))
        self.lbl_ch_fthing.setAccessibleDescription("")
        self.lbl_ch_fthing.setText("Favorite Thing")
        self.lbl_ch_fthing.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ch_fthing.setObjectName("lbl_ch_fthing")

        # <------------------- Change Favorite Thing LineEdit ------------------->
        self.input_ch_fthing = QtWidgets.QLineEdit(self.frm_ch_fthing)
        self.input_ch_fthing.setGeometry(QtCore.QRect(50, 80, 140, 27))
        self.input_ch_fthing.setText("")
        self.input_ch_fthing.setObjectName("input_ch_fthing")

        # <------------------- Change Favorite Thing Button ------------------->
        self.btn_ch_fthing = QtWidgets.QPushButton(self.frm_ch_fthing)
        self.btn_ch_fthing.setGeometry(QtCore.QRect(50, 125, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_fthing.setFont(font)
        self.btn_ch_fthing.setAccessibleDescription("")
        self.btn_ch_fthing.setText("Change")
        self.btn_ch_fthing.setObjectName("btn_ch_fthing")
        self.btn_ch_fthing.clicked.connect(self.change_favorite_thing)

        # <------------------- Economy GroupBox ------------------->
        self.gb_economy = QtWidgets.QGroupBox(self.tab_toolbox)
        self.gb_economy.setGeometry(QtCore.QRect(0, 375, 800, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gb_economy.setFont(font)
        self.gb_economy.setAccessibleDescription("")
        self.gb_economy.setTitle("Economy")
        self.gb_economy.setObjectName("gb_economy")

        # <------------------- Change Money Frame ------------------->
        self.frm_ch_money = QtWidgets.QFrame(self.gb_economy)
        self.frm_ch_money.setGeometry(QtCore.QRect(20, 30, 240, 180))
        self.frm_ch_money.setAccessibleDescription("")
        self.frm_ch_money.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ch_money.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ch_money.setObjectName("frm_ch_money")

        # <------------------- Change Money Label ------------------->
        self.lbl_ch_money = QtWidgets.QLabel(self.frm_ch_money)
        self.lbl_ch_money.setGeometry(QtCore.QRect(60, 30, 121, 30))
        self.lbl_ch_money.setAccessibleDescription("")
        self.lbl_ch_money.setText("Money")
        self.lbl_ch_money.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ch_money.setObjectName("lbl_ch_money")

        # <------------------- Change Money LineEdit ------------------->
        self.input_ch_money = QtWidgets.QLineEdit(self.frm_ch_money)
        self.input_ch_money.setGeometry(QtCore.QRect(50, 80, 140, 27))
        self.input_ch_money.setAccessibleDescription("")
        self.input_ch_money.setText("")
        self.input_ch_money.setObjectName("input_ch_money")

        # <------------------- Change Money Button ------------------->
        self.btn_ch_money = QtWidgets.QPushButton(self.frm_ch_money)
        self.btn_ch_money.setGeometry(QtCore.QRect(50, 125, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_money.setFont(font)
        self.btn_ch_money.setAccessibleDescription("")
        self.btn_ch_money.setText("Change")
        self.btn_ch_money.setObjectName("btn_ch_money")
        self.btn_ch_money.clicked.connect(self.change_money)

        # <------------------- Gold Image ------------------->
        self.img_gold = QtWidgets.QLabel(self.frm_ch_money)
        self.img_gold.setGeometry(QtCore.QRect(10, 80, 27, 27))
        self.img_gold.setAccessibleDescription("")
        self.img_gold.setText("")
        self.img_gold.setPixmap(QtGui.QPixmap("img/Gold.png"))
        self.img_gold.setScaledContents(True)
        self.img_gold.setAlignment(QtCore.Qt.AlignCenter)
        self.img_gold.setObjectName("img_gold")

        # <------------------- Change Qi Coins Frame ------------------->
        self.frm_ch_qicoins = QtWidgets.QFrame(self.gb_economy)
        self.frm_ch_qicoins.setGeometry(QtCore.QRect(280, 30, 240, 180))
        self.frm_ch_qicoins.setAccessibleDescription("")
        self.frm_ch_qicoins.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_ch_qicoins.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_ch_qicoins.setObjectName("frm_ch_qicoins")

        # <------------------- Change Qi Coins Label ------------------->
        self.lbl_ch_qicoins = QtWidgets.QLabel(self.frm_ch_qicoins)
        self.lbl_ch_qicoins.setGeometry(QtCore.QRect(60, 30, 121, 30))
        self.lbl_ch_qicoins.setAccessibleDescription("")
        self.lbl_ch_qicoins.setText("Qi Coins")
        self.lbl_ch_qicoins.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ch_qicoins.setObjectName("lbl_ch_qicoins")

        # <------------------- Change Qi Coins LineEdit ------------------->
        self.input_ch_qicoins = QtWidgets.QLineEdit(self.frm_ch_qicoins)
        self.input_ch_qicoins.setGeometry(QtCore.QRect(50, 80, 140, 27))
        self.input_ch_qicoins.setAccessibleDescription("")
        self.input_ch_qicoins.setText("")
        self.input_ch_qicoins.setObjectName("input_ch_qicoins")

        # <------------------- Change Qi Coins Button ------------------->
        self.btn_ch_qicoins = QtWidgets.QPushButton(self.frm_ch_qicoins)
        self.btn_ch_qicoins.setGeometry(QtCore.QRect(50, 125, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_ch_qicoins.setFont(font)
        self.btn_ch_qicoins.setAccessibleDescription("")
        self.btn_ch_qicoins.setText("Change")
        self.btn_ch_qicoins.setObjectName("btn_ch_qicoins")
        self.btn_ch_qicoins.clicked.connect(self.change_qicoins)

        # <------------------- Qi Coin Image ------------------->
        self.img_qicoin = QtWidgets.QLabel(self.frm_ch_qicoins)
        self.img_qicoin.setGeometry(QtCore.QRect(10, 80, 27, 27))
        self.img_qicoin.setAccessibleDescription("")
        self.img_qicoin.setText("")
        self.img_qicoin.setPixmap(QtGui.QPixmap("img/QiCoin.png"))
        self.img_qicoin.setScaledContents(True)
        self.img_qicoin.setAlignment(QtCore.Qt.AlignCenter)
        self.img_qicoin.setObjectName("img_qicoin")

        # <------------------- tabWidget ------------------->
        self.tabWidget.addTab(self.tab_toolbox, "ToolBox")

        # <------------------- About Tab ------------------->
        self.tab_about = QtWidgets.QWidget()
        self.tab_about.setAccessibleDescription("")
        self.tab_about.setObjectName("tab_about")

        # <------------------- Note Frame ------------------->
        self.frm_note = QtWidgets.QFrame(self.tab_about)
        self.frm_note.setGeometry(QtCore.QRect(0, 0, 800, 161))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)

        self.frm_note.setPalette(palette)
        self.frm_note.setAccessibleDescription("")
        self.frm_note.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_note.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_note.setObjectName("frm_note")

        # <------------------- Note Label ------------------->
        self.lbl_note = QtWidgets.QLabel(self.frm_note)
        self.lbl_note.setGeometry(QtCore.QRect(10, 10, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_note.setFont(font)
        self.lbl_note.setAccessibleDescription("")
        self.lbl_note.setText("<html><head/><body><p><span style=\" font-weight:600;\">Note:</span></p></body></html>")
        self.lbl_note.setObjectName("lbl_note")

        # <------------------- Note 1 Label ------------------->
        self.lbl_note1 = QtWidgets.QLabel(self.frm_note)
        self.lbl_note1.setGeometry(QtCore.QRect(20, 40, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_note1.setFont(font)
        self.lbl_note1.setAccessibleDescription("")
        self.lbl_note1.setText(
            "<html><head/><body><p><span style=\" font-weight:600;\">Please make backup of your Saves before using!</span></p></body></html>")
        self.lbl_note1.setObjectName("lbl_note1")

        # <------------------- Note 2 Label ------------------->
        self.lbl_note2 = QtWidgets.QLabel(self.frm_note)
        self.lbl_note2.setGeometry(QtCore.QRect(20, 70, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_note2.setFont(font)
        self.lbl_note2.setAccessibleDescription("")
        self.lbl_note2.setText(
            "<html><head/><body><p><span style=\" font-weight:600;\">Close the game before using this software.</span></p></body></html>")
        self.lbl_note2.setObjectName("lbl_note2")

        # <------------------- Saves Label ------------------->
        self.lbl_saves = QtWidgets.QLabel(self.frm_note)
        self.lbl_saves.setGeometry(QtCore.QRect(10, 120, 161, 31))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

        self.lbl_saves.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_saves.setFont(font)
        self.lbl_saves.setAccessibleDescription("")
        self.lbl_saves.setText("Your saves are here:")
        self.lbl_saves.setObjectName("lbl_saves")

        # <------------------- Saves Path Label ------------------->
        self.lbl_saves_path = QtWidgets.QLabel(self.frm_note)
        self.lbl_saves_path.setGeometry(QtCore.QRect(180, 120, 571, 31))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

        self.lbl_saves_path.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_saves_path.setFont(font)
        self.lbl_saves_path.setAccessibleDescription("")
        self.lbl_saves_path.setText(SAVES_PATH)
        self.lbl_saves_path.setOpenExternalLinks(False)
        self.lbl_saves_path.setObjectName("lbl_saves_path")

        # <------------------- Source Code Label ------------------->
        self.lbl_source_code = QtWidgets.QLabel(self.tab_about)
        self.lbl_source_code.setGeometry(QtCore.QRect(10, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_source_code.setFont(font)
        self.lbl_source_code.setAccessibleDescription("")
        self.lbl_source_code.setText("Source Code:")
        self.lbl_source_code.setObjectName("lbl_source_code")

        # <------------------- Repository Label ------------------->
        self.lbl_repo = QtWidgets.QLabel(self.tab_about)
        self.lbl_repo.setGeometry(QtCore.QRect(120, 180, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_repo.setFont(font)
        self.lbl_repo.setAccessibleDescription("")
        self.lbl_repo.setText(
            f"<html><head/><body><p><a href=\"{REPOSITORY}\"><span style=\" text-decoration: none; color: inherit;\">{REPOSITORY}</span></a></p></body></html>")
        self.lbl_repo.setOpenExternalLinks(True)
        self.lbl_repo.setObjectName("lbl_repo")

        # <------------------- License GroupBox ------------------->
        self.gb_license = QtWidgets.QGroupBox(self.tab_about)
        self.gb_license.setGeometry(QtCore.QRect(0, 230, 800, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gb_license.setFont(font)
        self.gb_license.setTitle("License")
        self.gb_license.setObjectName("gb_license")

        # <------------------- License textBrowser ------------------->
        self.textBrowser_license = QtWidgets.QTextBrowser(self.gb_license)
        self.textBrowser_license.setGeometry(QtCore.QRect(20, 30, 761, 321))
        self.textBrowser_license.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MIT License</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright (c) 2021 MSProgrammerPy</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Permission is hereby granted, free of charge, to any person obtaining a copy</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of this software and associated documentation files (the &quot;Software&quot;), to deal</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in the Software without restriction, including without limitation the rights</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to use, copy, modify, merge, publish, distribute, sublicense, and/or sell</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copies of the Software, and to permit persons to whom the Software is</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">furnished to do so, subject to the following conditions:</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The above copyright notice and this permission notice shall be included in all</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copies or substantial portions of the Software.</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE</p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SOFTWARE.</p></body></html>")
        self.textBrowser_license.setObjectName("textBrowser_license")

        # <------------------- tabWidget ------------------->
        self.tabWidget.addTab(self.tab_about, "About")

        # <------------------- MainWindow ------------------->
        MainWindow.setCentralWidget(self.centralwidget)

        # <------------------- statusbar ------------------->
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAccessibleDescription("")
        self.statusbar.setObjectName("statusbar")

        # <------------------- MainWindow ------------------->
        MainWindow.setStatusBar(self.statusbar)

        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.update_line_edits_text()

    def update_line_edits_text(self):
        if self.check_save():
            save = ToolBox(save_name=self.cb_saves.currentText())

            self.input_ch_name.setText(save.get(key="name"))
            self.input_ch_fname.setText(save.get(key="farmName"))
            self.input_ch_fthing.setText(save.get(key="favoriteThing"))
            self.input_ch_money.setText(save.get(key="money"))
            self.input_ch_qicoins.setText(save.get(key="clubCoins"))

    @staticmethod
    def generate_msg_box(title: str, text: str, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setIcon(icon)

        return msg_box

    def check_save(self):
        """
        This function checks to see if there is a save named 'save_name'
        or if there are save files in that save folder.
        """
        save_name = self.cb_saves.currentText()
        if len(save_name) == 0:
            msg_box = self.generate_msg_box(
                title="Error",
                text="There is no save in your saves folder!",
                icon=QMessageBox.Critical
            )
            msg_box.exec_()
            return False

        else:
            if not ToolBox.save_exists(name=save_name):
                msg_box = self.generate_msg_box(
                    title="Error",
                    text=f"There is no \"SaveGameInfo\" file or \"{save_name}\" file in the {save_name} folder!",
                    icon=QMessageBox.Critical
                )
                msg_box.exec_()
                return False

            return True

    def change_name(self):
        if self.check_save():
            save = ToolBox(save_name=self.cb_saves.currentText())
            new_name = self.input_ch_name.text()

            save.change_name(new_name=new_name)
            save.save()

    def change_farm_name(self):
        if self.check_save():
            save = ToolBox(save_name=self.cb_saves.currentText())
            new_name = self.input_ch_fname.text()

            save.change_farm_name(new_name=new_name)
            save.save()

    def change_favorite_thing(self):
        save = ToolBox(save_name=self.cb_saves.currentText())
        value = self.input_ch_fthing.text()

        save.change_favorite_thing(value=value)
        save.save()

    def change_money(self):
        save = ToolBox(save_name=self.cb_saves.currentText())
        value = self.input_ch_money.text()

        save.change_money(value=value)
        save.save()

    def change_qicoins(self):
        save = ToolBox(save_name=self.cb_saves.currentText())
        value = self.input_ch_qicoins.text()

        save.change_qicoins(value=value)
        save.save()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
