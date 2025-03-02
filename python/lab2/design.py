# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1109, 847)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: #222;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLineEdit,\n"
"QDoubleSpinBox,\n"
"QSpinBox {\n"
"	background-color: #eee;\n"
"	border: 2px solid #333;\n"
"	border-radius: 10px;\n"
"	font-size: 18px;\n"
"	font-weight: 700;\n"
"	padding: 3px 6px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #1F77B4;\n"
"	color: white;\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	padding: 8px;\n"
"	border-radius: 10px;\n"
"	margin-top: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #1D6DA6;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.topFrame = QFrame(self.centralwidget)
        self.topFrame.setObjectName(u"topFrame")
        self.horizontalLayout = QHBoxLayout(self.topFrame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.params = QFrame(self.topFrame)
        self.params.setObjectName(u"params")
        self.params.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: #eee;\n"
"}")
        self.params.setFrameShape(QFrame.Shape.StyledPanel)
        self.params.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.params)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, -1, 15, 15)
        self.label = QLabel(self.params)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Segoe UI Historic"])
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"margin-bottom: 2px;")
        self.label.setLineWidth(1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_2 = QLabel(self.params)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Historic"])
        font1.setPointSize(11)
        font1.setItalic(True)
        font1.setKerning(True)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.funcVal = QLineEdit(self.params)
        self.funcVal.setObjectName(u"funcVal")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.funcVal.sizePolicy().hasHeightForWidth())
        self.funcVal.setSizePolicy(sizePolicy2)
        self.funcVal.setFrame(True)

        self.verticalLayout_2.addWidget(self.funcVal)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_3 = QLabel(self.params)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_3)

        self.startVal = QDoubleSpinBox(self.params)
        self.startVal.setObjectName(u"startVal")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.startVal.sizePolicy().hasHeightForWidth())
        self.startVal.setSizePolicy(sizePolicy3)
        self.startVal.setMinimumSize(QSize(0, 36))
        self.startVal.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.startVal.setAccelerated(False)
        self.startVal.setDecimals(6)
        self.startVal.setMinimum(-1000000000.000000000000000)
        self.startVal.setMaximum(1000000000.000000000000000)
        self.startVal.setValue(-0.000100000000000)

        self.verticalLayout_4.addWidget(self.startVal)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_4 = QLabel(self.params)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_4)

        self.endVal = QDoubleSpinBox(self.params)
        self.endVal.setObjectName(u"endVal")
        sizePolicy3.setHeightForWidth(self.endVal.sizePolicy().hasHeightForWidth())
        self.endVal.setSizePolicy(sizePolicy3)
        self.endVal.setMinimumSize(QSize(0, 36))
        self.endVal.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.endVal.setDecimals(6)
        self.endVal.setMinimum(-1000000000.000000000000000)
        self.endVal.setMaximum(1000000000.000000000000000)
        self.endVal.setValue(1.000000000000000)

        self.verticalLayout_5.addWidget(self.endVal)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_5 = QLabel(self.params)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_5)

        self.maxIterVal = QSpinBox(self.params)
        self.maxIterVal.setObjectName(u"maxIterVal")
        sizePolicy3.setHeightForWidth(self.maxIterVal.sizePolicy().hasHeightForWidth())
        self.maxIterVal.setSizePolicy(sizePolicy3)
        self.maxIterVal.setMinimumSize(QSize(0, 36))
        self.maxIterVal.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.maxIterVal.setMinimum(1)
        self.maxIterVal.setMaximum(1000000000)
        self.maxIterVal.setSingleStep(50)
        self.maxIterVal.setValue(1000)

        self.verticalLayout_6.addWidget(self.maxIterVal)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_6 = QLabel(self.params)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_6)

        self.epsVal = QDoubleSpinBox(self.params)
        self.epsVal.setObjectName(u"epsVal")
        sizePolicy3.setHeightForWidth(self.epsVal.sizePolicy().hasHeightForWidth())
        self.epsVal.setSizePolicy(sizePolicy3)
        self.epsVal.setMinimumSize(QSize(0, 36))
        self.epsVal.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.epsVal.setDecimals(12)
        self.epsVal.setMinimum(0.000000000000000)
        self.epsVal.setMaximum(1.000000000000000)
        self.epsVal.setSingleStep(0.000001000000000)
        self.epsVal.setValue(0.000001000000000)

        self.verticalLayout_7.addWidget(self.epsVal)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_7 = QLabel(self.params)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_7)

        self.stepVal = QDoubleSpinBox(self.params)
        self.stepVal.setObjectName(u"stepVal")
        sizePolicy3.setHeightForWidth(self.stepVal.sizePolicy().hasHeightForWidth())
        self.stepVal.setSizePolicy(sizePolicy3)
        self.stepVal.setMinimumSize(QSize(0, 36))
        self.stepVal.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.stepVal.setDecimals(6)
        self.stepVal.setMinimum(0.000001000000000)
        self.stepVal.setMaximum(1000000000.000000000000000)
        self.stepVal.setSingleStep(0.000001000000000)
        self.stepVal.setValue(0.003998000000000)

        self.verticalLayout_8.addWidget(self.stepVal)


        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buildGraph = QPushButton(self.params)
        self.buildGraph.setObjectName(u"buildGraph")
        self.buildGraph.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.buildGraph)


        self.horizontalLayout.addWidget(self.params)

        self.graphContainer = QFrame(self.topFrame)
        self.graphContainer.setObjectName(u"graphContainer")
        self.graphContainer.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: #eee;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.graphContainer)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.horizontalLayout.addWidget(self.graphContainer)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout_3.addWidget(self.topFrame)

        self.tableContainer = QFrame(self.centralwidget)
        self.tableContainer.setObjectName(u"tableContainer")
        self.tableContainer.setStyleSheet(u"QFrame {\n"
"	border-radius: 10px;\n"
"	background-color: #eee;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.tableContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.table = QTableWidget(self.tableContainer)
        if (self.table.columnCount() < 6):
            self.table.setColumnCount(6)
        self.table.setObjectName(u"table")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Historic"])
        font2.setPointSize(12)
        self.table.setFont(font2)
        self.table.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: #1D6DA6;\n"
"	color: white;\n"
"	padding: 4px;\n"
"	border: none;\n"
"	font-size: 15px;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	background-color: #aaa;\n"
"}\n"
"\n"
"QTableWidget::item { \n"
"	text-align: center; \n"
"	width: 1000px;\n"
"}")
        self.table.setFrameShadow(QFrame.Shadow.Sunken)
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table.setAutoScroll(False)
        self.table.setTabKeyNavigation(False)
        self.table.setProperty(u"showDropIndicator", False)
        self.table.setGridStyle(Qt.PenStyle.SolidLine)
        self.table.setSortingEnabled(False)
        self.table.setRowCount(0)
        self.table.setColumnCount(6)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setHighlightSections(False)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setHighlightSections(False)

        self.verticalLayout_10.addWidget(self.table)


        self.verticalLayout_3.addWidget(self.tableContainer)

        self.verticalLayout_3.setStretch(0, 6)
        self.verticalLayout_3.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"  \u0424\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.funcVal.setInputMask("")
        self.funcVal.setText(QCoreApplication.translate("MainWindow", u"exp(x)*sin(100*x)", None))
        self.funcVal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448\u0430 \u0444\u0443\u043d\u043a\u0446\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"  \u041d\u0430\u0447\u0430\u043b\u043e", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"  \u041a\u043e\u043d\u0435\u0446", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"  \u041c\u0430\u043a\u0441. \u0447\u0438\u0441\u043b\u043e \u0438\u0442\u0435\u0440\u0430\u0446\u0438\u0439", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"  \u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c eps", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"  \u0428\u0430\u0433 \u0440\u0430\u0437\u0431\u0438\u0435\u043d\u0438\u044f", None))
        self.buildGraph.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
    # retranslateUi

