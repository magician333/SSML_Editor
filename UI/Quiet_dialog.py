# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Quiet_dialog.ui'
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

class Ui_set_quiet_dialog(object):
    def setupUi(self, set_quiet_dialog):
        if not set_quiet_dialog.objectName():
            set_quiet_dialog.setObjectName(u"set_quiet_dialog")
        set_quiet_dialog.resize(388, 259)
        icon = QIcon()
        icon.addFile(u"editor.png", QSize(), QIcon.Normal, QIcon.Off)
        set_quiet_dialog.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(set_quiet_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(140, 220, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(set_quiet_dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(20, 20, 341, 80))
        self.set_quiet_intensity = QComboBox(self.groupBox)
        self.set_quiet_intensity.setObjectName(u"set_quiet_intensity")
        self.set_quiet_intensity.setGeometry(QRect(110, 30, 201, 22))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 91, 16))
        self.groupBox_2 = QGroupBox(set_quiet_dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 120, 341, 80))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 91, 16))
        self.set_quiet_time = QSlider(self.groupBox_2)
        self.set_quiet_time.setObjectName(u"set_quiet_time")
        self.set_quiet_time.setGeometry(QRect(110, 40, 201, 22))
        self.set_quiet_time.setOrientation(Qt.Horizontal)
        self.show_quiet_time = QLabel(self.groupBox_2)
        self.show_quiet_time.setObjectName(u"show_quiet_time")
        self.show_quiet_time.setGeometry(QRect(190, 20, 54, 12))

        self.retranslateUi(set_quiet_dialog)
        self.buttonBox.accepted.connect(set_quiet_dialog.accept)
        self.buttonBox.rejected.connect(set_quiet_dialog.reject)

        QMetaObject.connectSlotsByName(set_quiet_dialog)
    # setupUi

    def retranslateUi(self, set_quiet_dialog):
        set_quiet_dialog.setWindowTitle(QCoreApplication.translate("set_quiet_dialog", u"\u8bbe\u7f6e\u9759\u97f3", None))
        self.groupBox.setTitle(QCoreApplication.translate("set_quiet_dialog", u"\u7c7b\u578b", None))
        self.label.setText(QCoreApplication.translate("set_quiet_dialog", u"\u8bbe\u7f6e\u9759\u97f3\u7c7b\u578b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("set_quiet_dialog", u"\u65f6\u95f4", None))
        self.label_2.setText(QCoreApplication.translate("set_quiet_dialog", u"\u8bbe\u7f6e\u6301\u7eed\u65f6\u95f4", None))
        self.show_quiet_time.setText(QCoreApplication.translate("set_quiet_dialog", u"0ms", None))
    # retranslateUi

