# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vixgon_main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import sys
sys.path.append(os.path.dirname(__file__))
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(756, 604)
        icon = QIcon()
        icon.addFile(u":/main/assets/vixgon_window.icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QFrame {\n"
"	background-color: #222422;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 700 11pt \"Candara\";\n"
"}\n"
"\n"
"QStackedWidget {\n"
"	background-color: #222422;\n"
"	border: 1px solid gray;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 10px;\n"
"	background-color:#687069;\n"
"}\n"
"\n"
"QLineEdit#item_search_lineedit {\n"
"	background-image: url(:/main/assets/search_colorized.png);\n"
"    background-position: right;\n"
"    background-repeat: no-repeat;\n"
"    color:  #ced9cf;\n"
"	font: 700 11pt \"Candara\";\n"
"}\n"
"\n"
"QComboBox {\n"
"	height: 30px;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        MainWindow.setIconSize(QSize(32, 32))
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout = QVBoxLayout(self.main_widget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.main_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_bar = QFrame(self.frame)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setMinimumSize(QSize(100, 0))
        self.side_bar.setMaximumSize(QSize(110, 16777215))
        self.side_bar.setStyleSheet(u"QToolButton {\n"
" 	height: 50px;\n"
"	width: 80px;\n"
"	font: 700 9pt \"Candara\";\n"
"	color: #687069;\n"
"	padding-top: 2px;\n"
"	background-color: #222422;\n"
"	border: 1px solid transparent;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"	background-color: #9b9e91;\n"
"	border-radius: 10px;\n"
"}")
        self.side_bar.setFrameShape(QFrame.Shape.NoFrame)
        self.side_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_bar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, 9)
        self.vixgon_app_icon = QLabel(self.side_bar)
        self.vixgon_app_icon.setObjectName(u"vixgon_app_icon")
        self.vixgon_app_icon.setMinimumSize(QSize(100, 100))
        self.vixgon_app_icon.setMaximumSize(QSize(100, 100))
        self.vixgon_app_icon.setPixmap(QPixmap(u":/main/assets/vixgon_main.png"))
        self.vixgon_app_icon.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.vixgon_app_icon, 0, Qt.AlignmentFlag.AlignHCenter)

        self.item_search = QToolButton(self.side_bar)
        self.item_search.setObjectName(u"item_search")
        icon1 = QIcon()
        icon1.addFile(u":/main/assets/search_colorized.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.item_search.setIcon(icon1)
        self.item_search.setIconSize(QSize(32, 32))
        self.item_search.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.item_search)

        self.item_management = QToolButton(self.side_bar)
        self.item_management.setObjectName(u"item_management")
        self.item_management.setStyleSheet(u"font: 700 8pt \"Candara\";")
        icon2 = QIcon()
        icon2.addFile(u":/main/assets/item_management_colorized.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.item_management.setIcon(icon2)
        self.item_management.setIconSize(QSize(32, 32))
        self.item_management.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.item_management)

        self.shelf_add = QToolButton(self.side_bar)
        self.shelf_add.setObjectName(u"shelf_add")
        icon3 = QIcon()
        icon3.addFile(u":/main/assets/shelf_colorized.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shelf_add.setIcon(icon3)
        self.shelf_add.setIconSize(QSize(32, 32))
        self.shelf_add.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.shelf_add)

        self.item_io = QToolButton(self.side_bar)
        self.item_io.setObjectName(u"item_io")
        icon4 = QIcon()
        icon4.addFile(u":/main/assets/item_io.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.item_io.setIcon(icon4)
        self.item_io.setIconSize(QSize(32, 32))
        self.item_io.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.item_io)

        self.user_actions = QToolButton(self.side_bar)
        self.user_actions.setObjectName(u"user_actions")
        self.user_actions.setStyleSheet(u"font: 700 8pt \"Candara\";")
        self.user_actions.setIconSize(QSize(32, 32))
        self.user_actions.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.user_actions)

        self.about_btn = QToolButton(self.side_bar)
        self.about_btn.setObjectName(u"about_btn")
        icon5 = QIcon()
        icon5.addFile(u":/main/assets/agreement_colorized.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.about_btn.setIcon(icon5)
        self.about_btn.setIconSize(QSize(32, 32))
        self.about_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_2.addWidget(self.about_btn)

        self.username_text = QLabel(self.side_bar)
        self.username_text.setObjectName(u"username_text")
        self.username_text.setStyleSheet(u"color:  #687069;")
        self.username_text.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.username_text)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.exit_frame = QFrame(self.side_bar)
        self.exit_frame.setObjectName(u"exit_frame")
        self.exit_frame.setMinimumSize(QSize(0, 70))
        self.exit_frame.setMaximumSize(QSize(16777215, 50))
        self.exit_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.exit_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.exit_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.exit_frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(0, 30))
        icon6 = QIcon()
        icon6.addFile(u":/main/assets/logout_colorized.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon6)
        self.toolButton.setIconSize(QSize(32, 32))
        self.toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.toolButton)


        self.verticalLayout_2.addWidget(self.exit_frame)


        self.horizontalLayout.addWidget(self.side_bar)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.item_search_page = QWidget()
        self.item_search_page.setObjectName(u"item_search_page")
        self.verticalLayout_7 = QVBoxLayout(self.item_search_page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.item_search_frame = QFrame(self.item_search_page)
        self.item_search_frame.setObjectName(u"item_search_frame")
        self.item_search_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.item_search_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.item_search_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_6 = QFrame(self.item_search_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 40, -1, -1)
        self.item_search_lineedit = QLineEdit(self.frame_6)
        self.item_search_lineedit.setObjectName(u"item_search_lineedit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_search_lineedit.sizePolicy().hasHeightForWidth())
        self.item_search_lineedit.setSizePolicy(sizePolicy)
        self.item_search_lineedit.setMinimumSize(QSize(600, 38))
        self.item_search_lineedit.setMaximumSize(QSize(1900, 38))
        self.item_search_lineedit.setClearButtonEnabled(False)

        self.verticalLayout_9.addWidget(self.item_search_lineedit, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.checkBox = QCheckBox(self.frame_6)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_9.addWidget(self.checkBox)

        self.filter_frame = QFrame(self.frame_6)
        self.filter_frame.setObjectName(u"filter_frame")
        self.filter_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.filter_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.filter_frame)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(self.filter_frame)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.filter_frame)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.filter_frame)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_2.addWidget(self.comboBox_3)


        self.verticalLayout_9.addWidget(self.filter_frame)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.item_search_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_8.addWidget(self.frame_7)


        self.verticalLayout_7.addWidget(self.item_search_frame)

        self.stackedWidget.addWidget(self.item_search_page)
        self.item_management_page = QWidget()
        self.item_management_page.setObjectName(u"item_management_page")
        self.stackedWidget.addWidget(self.item_management_page)
        self.shelf_management_page = QWidget()
        self.shelf_management_page.setObjectName(u"shelf_management_page")
        self.stackedWidget.addWidget(self.shelf_management_page)
        self.user_info_page = QWidget()
        self.user_info_page.setObjectName(u"user_info_page")
        self.verticalLayout_10 = QVBoxLayout(self.user_info_page)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.user_info_frame = QFrame(self.user_info_page)
        self.user_info_frame.setObjectName(u"user_info_frame")
        self.user_info_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.user_info_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.user_info_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.user_icon_frame = QFrame(self.user_info_frame)
        self.user_icon_frame.setObjectName(u"user_icon_frame")
        self.user_icon_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.user_icon_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.user_icon_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.user_icon = QLabel(self.user_icon_frame)
        self.user_icon.setObjectName(u"user_icon")
        self.user_icon.setMinimumSize(QSize(200, 150))

        self.verticalLayout_12.addWidget(self.user_icon, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_11.addWidget(self.user_icon_frame)

        self.frame_4 = QFrame(self.user_info_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.username_label = QLabel(self.frame_8)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout_13.addWidget(self.username_label)

        self.name_label = QLabel(self.frame_8)
        self.name_label.setObjectName(u"name_label")

        self.verticalLayout_13.addWidget(self.name_label)

        self.surname_label = QLabel(self.frame_8)
        self.surname_label.setObjectName(u"surname_label")

        self.verticalLayout_13.addWidget(self.surname_label)

        self.age_label = QLabel(self.frame_8)
        self.age_label.setObjectName(u"age_label")

        self.verticalLayout_13.addWidget(self.age_label)

        self.gender_label = QLabel(self.frame_8)
        self.gender_label.setObjectName(u"gender_label")

        self.verticalLayout_13.addWidget(self.gender_label)

        self.registration_label = QLabel(self.frame_8)
        self.registration_label.setObjectName(u"registration_label")

        self.verticalLayout_13.addWidget(self.registration_label)

        self.user_type_label = QLabel(self.frame_8)
        self.user_type_label.setObjectName(u"user_type_label")

        self.verticalLayout_13.addWidget(self.user_type_label)


        self.horizontalLayout_3.addWidget(self.frame_8)

        self.text_frame = QFrame(self.frame_4)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.text_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.text_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.username_text_2 = QLabel(self.text_frame)
        self.username_text_2.setObjectName(u"username_text_2")

        self.verticalLayout_14.addWidget(self.username_text_2)

        self.name_text = QLabel(self.text_frame)
        self.name_text.setObjectName(u"name_text")

        self.verticalLayout_14.addWidget(self.name_text)

        self.surname_text = QLabel(self.text_frame)
        self.surname_text.setObjectName(u"surname_text")

        self.verticalLayout_14.addWidget(self.surname_text)

        self.age_text = QLabel(self.text_frame)
        self.age_text.setObjectName(u"age_text")

        self.verticalLayout_14.addWidget(self.age_text)

        self.gender_text = QLabel(self.text_frame)
        self.gender_text.setObjectName(u"gender_text")

        self.verticalLayout_14.addWidget(self.gender_text)

        self.registration_text = QLabel(self.text_frame)
        self.registration_text.setObjectName(u"registration_text")

        self.verticalLayout_14.addWidget(self.registration_text)

        self.user_type_text = QLabel(self.text_frame)
        self.user_type_text.setObjectName(u"user_type_text")

        self.verticalLayout_14.addWidget(self.user_type_text)


        self.horizontalLayout_3.addWidget(self.text_frame)


        self.verticalLayout_11.addWidget(self.frame_4)


        self.verticalLayout_10.addWidget(self.user_info_frame)

        self.stackedWidget.addWidget(self.user_info_page)
        self.user_management_page = QWidget()
        self.user_management_page.setObjectName(u"user_management_page")
        self.stackedWidget.addWidget(self.user_management_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.verticalLayout_5 = QVBoxLayout(self.about_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.about_page_frame = QFrame(self.about_page)
        self.about_page_frame.setObjectName(u"about_page_frame")
        self.about_page_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.about_page_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.about_page_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.app_icon = QLabel(self.about_page_frame)
        self.app_icon.setObjectName(u"app_icon")
        self.app_icon.setMaximumSize(QSize(200, 200))
        self.app_icon.setPixmap(QPixmap(u":/main/assets/vixgon_main.png"))
        self.app_icon.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.app_icon, 0, Qt.AlignmentFlag.AlignHCenter)

        self.about_text = QLabel(self.about_page_frame)
        self.about_text.setObjectName(u"about_text")
        self.about_text.setStyleSheet(u"color: #687069;")

        self.verticalLayout_6.addWidget(self.about_text, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_5.addWidget(self.about_page_frame)

        self.stackedWidget.addWidget(self.about_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vixgon", None))
        self.vixgon_app_icon.setText("")
        self.item_search.setText(QCoreApplication.translate("MainWindow", u"\u00dcR\u00dcN ARAMA", None))
        self.item_management.setText(QCoreApplication.translate("MainWindow", u"\u00dcR\u00dcN Y\u00d6NET\u0130M\u0130", None))
        self.shelf_add.setText(QCoreApplication.translate("MainWindow", u"RAF Y\u00d6NET\u0130M\u0130", None))
        self.item_io.setText(QCoreApplication.translate("MainWindow", u"\u00dcR\u00dcN TAK\u0130B\u0130", None))
        self.user_actions.setText("")
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"HAKKINDA", None))
        self.username_text.setText("")
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"\u00c7IKI\u015e", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Filtreleri dahil et", None))
        self.user_icon.setText("")
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"KULLANICI ADI", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"ISIM", None))
        self.surname_label.setText(QCoreApplication.translate("MainWindow", u"SOY \u0130SM\u0130", None))
        self.age_label.setText(QCoreApplication.translate("MainWindow", u"YA\u015e", None))
        self.gender_label.setText(QCoreApplication.translate("MainWindow", u"CINSIYET", None))
        self.registration_label.setText(QCoreApplication.translate("MainWindow", u"KAYIT TARIHI", None))
        self.user_type_label.setText(QCoreApplication.translate("MainWindow", u"KULLANICI T\u0130P\u0130", None))
        self.username_text_2.setText("")
        self.name_text.setText("")
        self.surname_text.setText("")
        self.age_text.setText("")
        self.gender_text.setText("")
        self.registration_text.setText("")
        self.user_type_text.setText("")
        self.app_icon.setText("")
        self.about_text.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Alperen \u00c7avu\u015f \u2013 T\u00fcm Haklar\u0131 Sakl\u0131d\u0131r\n"
"\n"
"Bu yaz\u0131l\u0131m\u0131n t\u00fcm fikr\u00ee ve hukuki haklar\u0131 Alperen \u00c7avu\u015f\u2019a aittir.\n"
"\n"
"Bu program ticari ama\u00e7larla kullan\u0131lamaz, sat\u0131lamaz, kiralanamaz\n"
"veya herhangi bir gelir elde edecek \u015fekilde da\u011f\u0131t\u0131lamaz.\n"
"\n"
"Program i\u00e7erisinde yer alan yazar ad\u0131, telif bilgileri ve aidiyet\n"
"ifadeleri hi\u00e7bir \u015fekilde de\u011fi\u015ftirilemez, kald\u0131r\u0131lamaz veya gizlenemez.\n"
"\n"
"Bu yaz\u0131l\u0131m\u0131n kaynak kodu, derlenmi\u015f h\u00e2li veya herhangi bir par\u00e7as\u0131\n"
"de\u011fi\u015ftirilemez, d\u00fczenlenemez, tersine m\u00fchendisli\u011fe tabi tutulamaz\n"
"ve ba\u015fka bir projede k\u0131smen ya da tamamen kullan\u0131lamaz.\n"
"\n"
"Bu yaz\u0131l\u0131m\u0131n kullan\u0131lmas\u0131, yukar\u0131daki \u015fartlar\u0131n kabul edildi\u011fi\n"
"anlam\u0131na gelir.\n"
"", None))
    # retranslateUi

