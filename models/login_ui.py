# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 500)
        Dialog.setMinimumSize(QSize(900, 500))
        Dialog.setMaximumSize(QSize(900, 500))
        Dialog.setStyleSheet(u"QFrame#main_frame {\n"
"	\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#logo_frame {\n"
"\n"
"	padding-left: 0px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton {\n"
"	background-color:  #687069;\n"
"	border-radius: 10px;\n"
"\n"
"	font: 700 11pt \"Candara\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #9b9e91;\n"
"}\n"
"\n"
"QLabel {\n"
"	font: 700 11pt \"Candara\";\n"
"	color:#687069;\n"
"}\n"
"QLineEdit {\n"
"	border-radius: 5px;\n"
"	color: #ced9cf;\n"
"	background-color: #687069;\n"
"\n"
"	font: 700 11pt \"Candara\";\n"
"}\n"
"\n"
"QCheckBox {\n"
"	font: 700 11pt \"Candara\";\n"
"	color: #687069;\n"
"}\n"
"\n"
"QCheckBox:indicator {\n"
"	border: 1px solid #687069;;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-repeat: no-repeat;\n"
"    background-position: right;\n"
"}\n"
"\n"
"QLineEdit#username_input {\n"
"	background-position: right ;\n"
"	background-image: url(:/main/assets/username_colorized.png);\n"
"}\n"
"QLineEdit#password_input {\n"
"	background-image: url("
                        ":/main/assets/password_colorized.png);\n"
"}\n"
"QLineEdit#pwd_input {\n"
"\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color: #687069;\n"
"	\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: #222422;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo_frame = QFrame(self.frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMinimumSize(QSize(300, 0))
        self.logo_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.logo_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 5, 5)
        self.sidebar_icon = QLabel(self.logo_frame)
        self.sidebar_icon.setObjectName(u"sidebar_icon")
        self.sidebar_icon.setMaximumSize(QSize(300, 478))
        self.sidebar_icon.setFrameShape(QFrame.Shape.NoFrame)
        self.sidebar_icon.setPixmap(QPixmap(u":/main/assets/vixgon_main.png"))
        self.sidebar_icon.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.sidebar_icon)


        self.horizontalLayout.addWidget(self.logo_frame)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 10, -1, -1)

        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.username_text = QLabel(self.frame_4)
        self.username_text.setObjectName(u"username_text")
        self.username_text.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.username_text, 0, Qt.AlignmentFlag.AlignHCenter)

        self.username_input = QLineEdit(self.frame_4)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(200, 30))
        self.username_input.setMaximumSize(QSize(200, 30))

        self.verticalLayout_5.addWidget(self.username_input, 0, Qt.AlignmentFlag.AlignHCenter)

        self.password_input = QLineEdit(self.frame_4)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(200, 30))
        self.password_input.setMaximumSize(QSize(200, 30))

        self.verticalLayout_5.addWidget(self.password_input, 0, Qt.AlignmentFlag.AlignHCenter)

        self.loading_icon_frame = QFrame(self.frame_4)
        self.loading_icon_frame.setObjectName(u"loading_icon_frame")
        self.loading_icon_frame.setMinimumSize(QSize(0, 70))
        self.loading_icon_frame.setMaximumSize(QSize(16777215, 70))
        self.loading_icon_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.loading_icon_frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.loading_icon_frame)

        self.status_label = QLabel(self.frame_4)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_5.addWidget(self.status_label)

        self.checkbox_user_creds = QCheckBox(self.frame_4)
        self.checkbox_user_creds.setObjectName(u"checkbox_user_creds")
        self.checkbox_user_creds.setMinimumSize(QSize(0, 30))
        self.checkbox_user_creds.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_5.addWidget(self.checkbox_user_creds, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.exit_btn = QPushButton(self.frame_5)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.exit_btn)

        self.login_btn = QPushButton(self.frame_5)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.login_btn)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.sidebar_icon.setText("")
        self.username_text.setText("")
        self.username_input.setText("")
        self.username_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"Kullan\u0131c\u0131 ad\u0131 giriniz", None))
        self.password_input.setText("")
        self.password_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u015eifre giriniz", None))
        self.status_label.setText("")
        self.checkbox_user_creds.setText(QCoreApplication.translate("Dialog", u"Giri\u015f Bilgilerini Kaydet", None))
        self.exit_btn.setText(QCoreApplication.translate("Dialog", u"\u00c7\u0131k\u0131\u015f", None))
        self.login_btn.setText(QCoreApplication.translate("Dialog", u"Biri\u015f", None))
    # retranslateUi

