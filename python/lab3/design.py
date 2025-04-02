# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_wndw(object):
    def setupUi(self, wndw):
        if not wndw.objectName():
            wndw.setObjectName(u"wndw")
        wndw.resize(926, 600)
        wndw.setStyleSheet(u"#centralwidget {\n"
"background-color: #222;\n"
"}")
        self.centralwidget = QWidget(wndw)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"    background-color: #DDD;\n"
"	border: 2px solid #DDD;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #AAA;\n"
"    color: #222; \n"
"	font-weight: 700;\n"
"	font-size: 16px;\n"
"    padding: 6px 10px;\n"
"	margin-left: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: #DDD;\n"
"}\n"
"")
        self.encode_tab = QWidget()
        self.encode_tab.setObjectName(u"encode_tab")
        self.encode_tab.setStyleSheet(u"background-color: #DDD;")
        self.horizontalLayout_2 = QHBoxLayout(self.encode_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.encode_tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.cur_len_label = QLabel(self.encode_tab)
        self.cur_len_label.setObjectName(u"cur_len_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cur_len_label.sizePolicy().hasHeightForWidth())
        self.cur_len_label.setSizePolicy(sizePolicy1)
        self.cur_len_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.cur_len_label)

        self.label_4 = QLabel(self.encode_tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.max_len_label = QLabel(self.encode_tab)
        self.max_len_label.setObjectName(u"max_len_label")
        sizePolicy1.setHeightForWidth(self.max_len_label.sizePolicy().hasHeightForWidth())
        self.max_len_label.setSizePolicy(sizePolicy1)
        self.max_len_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.max_len_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.encode_text = QPlainTextEdit(self.encode_tab)
        self.encode_text.setObjectName(u"encode_text")
        self.encode_text.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #2B2B2B;\n"
"    color: #FFFFFF;\n"
"    selection-background-color: #4C97FF;\n"
"    selection-color: #FFFFFF;\n"
"    border: 2px solid #3C3F41;\n"
"    border-radius: 8px;\n"
"    font-family: 'Consolas';\n"
"    font-size: 14px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4C97FF;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #3C3F41;\n"
"    width: 12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #555555;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")

        self.verticalLayout_3.addWidget(self.encode_text)

        self.encode_button = QPushButton(self.encode_tab)
        self.encode_button.setObjectName(u"encode_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.encode_button.sizePolicy().hasHeightForWidth())
        self.encode_button.setSizePolicy(sizePolicy2)
        self.encode_button.setMaximumSize(QSize(9999, 16777215))
        self.encode_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.encode_button.setStyleSheet(u"QPushButton {\n"
"	border-radius: 8px;\n"
"	padding: 5px 20px;\n"
"	background-color: #C1415D;\n"
"	font-size: 15px;\n"
"	font-weight: 700;\n"
"	color: white;\n"
"}")

        self.verticalLayout_3.addWidget(self.encode_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.encode_open = QPushButton(self.encode_tab)
        self.encode_open.setObjectName(u"encode_open")
        sizePolicy2.setHeightForWidth(self.encode_open.sizePolicy().hasHeightForWidth())
        self.encode_open.setSizePolicy(sizePolicy2)
        self.encode_open.setMaximumSize(QSize(150, 16777215))
        self.encode_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.encode_open.setStyleSheet(u"QPushButton {\n"
"	border-radius: 8px;\n"
"	padding: 5px 20px;\n"
"	background-color: #C1415D;\n"
"	font-size: 15px;\n"
"	font-weight: 700;\n"
"	color: white;\n"
"}")

        self.horizontalLayout_3.addWidget(self.encode_open)

        self.encode_save = QPushButton(self.encode_tab)
        self.encode_save.setObjectName(u"encode_save")
        sizePolicy2.setHeightForWidth(self.encode_save.sizePolicy().hasHeightForWidth())
        self.encode_save.setSizePolicy(sizePolicy2)
        self.encode_save.setMaximumSize(QSize(150, 16777215))
        self.encode_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.encode_save.setStyleSheet(u"QPushButton {\n"
"	border-radius: 8px;\n"
"	padding: 5px 20px;\n"
"	background-color: #8E41C1;\n"
"	font-size: 15px;\n"
"	font-weight: 700;\n"
"	color: white;\n"
"}")

        self.horizontalLayout_3.addWidget(self.encode_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.encode_img = QLabel(self.encode_tab)
        self.encode_img.setObjectName(u"encode_img")
        self.encode_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.encode_img)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9999999)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)
        self.tabWidget.addTab(self.encode_tab, "")
        self.decode_tab = QWidget()
        self.decode_tab.setObjectName(u"decode_tab")
        self.decode_tab.setStyleSheet(u"background-color: #DDD;")
        self.horizontalLayout = QHBoxLayout(self.decode_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.decode_tab)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.decode_text = QPlainTextEdit(self.decode_tab)
        self.decode_text.setObjectName(u"decode_text")
        self.decode_text.setStyleSheet(u"QPlainTextEdit {\n"
"    background-color: #2B2B2B;\n"
"    color: #FFFFFF;\n"
"    selection-background-color: #4C97FF;\n"
"    selection-color: #FFFFFF;\n"
"    border: 2px solid #3C3F41;\n"
"    border-radius: 8px;\n"
"    font-family: 'Consolas';\n"
"    font-size: 14px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4C97FF;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background: #3C3F41;\n"
"    width: 12px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #555555;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}")
        self.decode_text.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.decode_text)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.decode_open = QPushButton(self.decode_tab)
        self.decode_open.setObjectName(u"decode_open")
        sizePolicy2.setHeightForWidth(self.decode_open.sizePolicy().hasHeightForWidth())
        self.decode_open.setSizePolicy(sizePolicy2)
        self.decode_open.setMaximumSize(QSize(200, 16777215))
        self.decode_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.decode_open.setStyleSheet(u"QPushButton {\n"
"	border-radius: 8px;\n"
"	padding: 5px 20px;\n"
"	background-color: #C1415D;\n"
"	font-size: 15px;\n"
"	font-weight: 700;\n"
"	color: white;\n"
"}")

        self.horizontalLayout_5.addWidget(self.decode_open)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.decode_img = QLabel(self.decode_tab)
        self.decode_img.setObjectName(u"decode_img")
        self.decode_img.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.decode_img)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 9999999)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)
        self.tabWidget.addTab(self.decode_tab, "")
        self.info = QWidget()
        self.info.setObjectName(u"info")
        self.info.setStyleSheet(u"background-color: #DDD;")
        self.horizontalLayout_6 = QHBoxLayout(self.info)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.label_7 = QLabel(self.info)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_8 = QLabel(self.info)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_9 = QLabel(self.info)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.label_6 = QLabel(self.info)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/imgs/ya_programmist.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setMargin(30)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 4)
        self.tabWidget.addTab(self.info, "")

        self.verticalLayout.addWidget(self.tabWidget)

        wndw.setCentralWidget(self.centralwidget)

        self.retranslateUi(wndw)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(wndw)
    # setupUi

    def retranslateUi(self, wndw):
        wndw.setWindowTitle(QCoreApplication.translate("wndw", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("wndw", u"Text:", None))
        self.cur_len_label.setText(QCoreApplication.translate("wndw", u"0", None))
        self.label_4.setText(QCoreApplication.translate("wndw", u"/", None))
        self.max_len_label.setText(QCoreApplication.translate("wndw", u"0", None))
        self.encode_button.setText(QCoreApplication.translate("wndw", u"Encode", None))
        self.encode_open.setText(QCoreApplication.translate("wndw", u"Open", None))
        self.encode_save.setText(QCoreApplication.translate("wndw", u"Save", None))
        self.encode_img.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encode_tab), QCoreApplication.translate("wndw", u"Encode", None))
        self.label_5.setText(QCoreApplication.translate("wndw", u"Decoded text", None))
        self.decode_open.setText(QCoreApplication.translate("wndw", u"Open", None))
        self.decode_img.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.decode_tab), QCoreApplication.translate("wndw", u"Decode", None))
        self.label_7.setText(QCoreApplication.translate("wndw", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u043b: \u041f\u044d\u043a\u044d\u043b\u044d\u0443 \u0414\u0430\u043d\u0438\u0438\u043b", None))
        self.label_8.setText(QCoreApplication.translate("wndw", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442 \u0418\u04237-26\u0411", None))
        self.label_9.setText(QCoreApplication.translate("wndw", u"\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b: \u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0438 \u0434\u0435\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0435\u0439\u0441\u044f \u0432 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u043c \u0432\u0438\u0434\u0435 \u0432 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0438", None))
        self.label_6.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.info), QCoreApplication.translate("wndw", u"Info", None))
    # retranslateUi

