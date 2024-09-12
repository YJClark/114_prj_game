# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 1000)
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 320, 331, 311))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutWidget_2 = QWidget(Widget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(460, 320, 314, 314))
        self.answer_grid = QGridLayout(self.gridLayoutWidget_2)
        self.answer_grid.setObjectName(u"answer_grid")
        self.answer_grid.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setLayoutDirection(Qt.LeftToRight)

        self.answer_grid.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 100))
        self.label_2.setLayoutDirection(Qt.LeftToRight)

        self.answer_grid.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 100))
        self.label_5.setLayoutDirection(Qt.LeftToRight)

        self.answer_grid.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 100))
        self.label_4.setLayoutDirection(Qt.LeftToRight)

        self.answer_grid.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 100))
        self.label_3.setLayoutDirection(Qt.LeftToRight)

        self.answer_grid.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 100))
        self.label_6.setLayoutDirection(Qt.LeftToRight)

        self.answer_grid.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 100))
        self.label_7.setLayoutDirection(Qt.LeftToRight)

        self.answer_grid.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 100))
        self.label_8.setLayoutDirection(Qt.LeftToRight)

        self.answer_grid.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 100))
        self.label_9.setLayoutDirection(Qt.LeftToRight)

        self.answer_grid.addWidget(self.label_9, 2, 2, 1, 1)

        self.layoutWidget = QWidget(Widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 70, 701, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"manual ", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"kiva", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"puzzle", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"algo1", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"algo2", None))
    # retranslateUi

