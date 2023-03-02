# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Break_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGroupBox, QLabel, QSizePolicy,
    QSlider, QWidget)

class Ui_set_break_dialog(object):
    def setupUi(self, set_break_dialog):
        if not set_break_dialog.objectName():
            set_break_dialog.setObjectName(u"set_break_dialog")
        set_break_dialog.resize(341, 259)
        icon = QIcon()
        icon.addFile(u"editor.png", QSize(), QIcon.Normal, QIcon.Off)
        set_break_dialog.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(set_break_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(140, 220, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(set_break_dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(20, 20, 301, 80))
        self.set_break_intensity = QComboBox(self.groupBox)
        self.set_break_intensity.setObjectName(u"set_break_intensity")
        self.set_break_intensity.setGeometry(QRect(110, 30, 151, 22))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 91, 16))
        self.groupBox_2 = QGroupBox(set_break_dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 120, 301, 80))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 91, 16))
        self.set_break_time = QSlider(self.groupBox_2)
        self.set_break_time.setObjectName(u"set_break_time")
        self.set_break_time.setGeometry(QRect(110, 40, 141, 22))
        self.set_break_time.setOrientation(Qt.Horizontal)
        self.show_break_time = QLabel(self.groupBox_2)
        self.show_break_time.setObjectName(u"show_break_time")
        self.show_break_time.setGeometry(QRect(160, 20, 54, 12))

        self.retranslateUi(set_break_dialog)
        self.buttonBox.accepted.connect(set_break_dialog.accept)
        self.buttonBox.rejected.connect(set_break_dialog.reject)

        QMetaObject.connectSlotsByName(set_break_dialog)
    # setupUi

    def retranslateUi(self, set_break_dialog):
        set_break_dialog.setWindowTitle(QCoreApplication.translate("set_break_dialog", u"\u8bbe\u7f6e\u505c\u987f", None))
        self.groupBox.setTitle(QCoreApplication.translate("set_break_dialog", u"\u5f3a\u5ea6", None))
        self.label.setText(QCoreApplication.translate("set_break_dialog", u"\u8bbe\u7f6e\u505c\u987f\u5f3a\u5ea6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("set_break_dialog", u"\u65f6\u95f4", None))
        self.label_2.setText(QCoreApplication.translate("set_break_dialog", u"\u8bbe\u7f6e\u505c\u987f\u65f6\u95f4", None))
        self.show_break_time.setText(QCoreApplication.translate("set_break_dialog", u"0ms", None))
    # retranslateUi

