# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sayas_dialog.ui'
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
    QDialogButtonBox, QGroupBox, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_set_sayas_dialog(object):
    def setupUi(self, set_sayas_dialog):
        if not set_sayas_dialog.objectName():
            set_sayas_dialog.setObjectName(u"set_sayas_dialog")
        set_sayas_dialog.resize(341, 359)
        icon = QIcon()
        icon.addFile(u"editor.png", QSize(), QIcon.Normal, QIcon.Off)
        set_sayas_dialog.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(set_sayas_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 320, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(set_sayas_dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(20, 20, 301, 80))
        self.set_sayas_type = QComboBox(self.groupBox)
        self.set_sayas_type.setObjectName(u"set_sayas_type")
        self.set_sayas_type.setGeometry(QRect(110, 30, 151, 22))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 91, 16))
        self.groupBox_2 = QGroupBox(set_sayas_dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 120, 301, 80))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 91, 16))
        self.set_sayas_format = QComboBox(self.groupBox_2)
        self.set_sayas_format.setObjectName(u"set_sayas_format")
        self.set_sayas_format.setGeometry(QRect(110, 40, 151, 22))
        self.groupBox_3 = QGroupBox(set_sayas_dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 220, 301, 80))
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 91, 16))
        self.set_sayas_detail = QLineEdit(self.groupBox_3)
        self.set_sayas_detail.setObjectName(u"set_sayas_detail")
        self.set_sayas_detail.setGeometry(QRect(110, 30, 151, 31))

        self.retranslateUi(set_sayas_dialog)
        self.buttonBox.accepted.connect(set_sayas_dialog.accept)
        self.buttonBox.rejected.connect(set_sayas_dialog.reject)

        QMetaObject.connectSlotsByName(set_sayas_dialog)
    # setupUi

    def retranslateUi(self, set_sayas_dialog):
        set_sayas_dialog.setWindowTitle(QCoreApplication.translate("set_sayas_dialog", u"\u8bbe\u7f6e\u8bfb\u6cd5", None))
        self.groupBox.setTitle(QCoreApplication.translate("set_sayas_dialog", u"\u7c7b\u578b", None))
        self.label.setText(QCoreApplication.translate("set_sayas_dialog", u"\u8bbe\u7f6e\u8bfb\u6cd5\u7c7b\u578b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("set_sayas_dialog", u"\u683c\u5f0f", None))
        self.label_2.setText(QCoreApplication.translate("set_sayas_dialog", u"\u8bbe\u7f6e\u8bfb\u6cd5\u683c\u5f0f", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("set_sayas_dialog", u"\u7ec6\u8282", None))
        self.label_3.setText(QCoreApplication.translate("set_sayas_dialog", u"\u8bbe\u7f6e\u8bfb\u6cd5\u7ec6\u8282", None))
    # retranslateUi

