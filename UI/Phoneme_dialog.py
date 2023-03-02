# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Phoneme_dialog.ui'
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

class Ui_set_phoneme_dialog(object):
    def setupUi(self, set_phoneme_dialog):
        if not set_phoneme_dialog.objectName():
            set_phoneme_dialog.setObjectName(u"set_phoneme_dialog")
        set_phoneme_dialog.resize(388, 259)
        icon = QIcon()
        icon.addFile(u"editor.png", QSize(), QIcon.Normal, QIcon.Off)
        set_phoneme_dialog.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(set_phoneme_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(140, 220, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(set_phoneme_dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(20, 20, 341, 80))
        self.set_phoneme_type = QComboBox(self.groupBox)
        self.set_phoneme_type.setObjectName(u"set_phoneme_type")
        self.set_phoneme_type.setGeometry(QRect(110, 30, 201, 22))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 91, 16))
        self.groupBox_2 = QGroupBox(set_phoneme_dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 120, 341, 80))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 91, 16))
        self.set_phoneme_ph = QLineEdit(self.groupBox_2)
        self.set_phoneme_ph.setObjectName(u"set_phoneme_ph")
        self.set_phoneme_ph.setGeometry(QRect(100, 20, 211, 31))

        self.retranslateUi(set_phoneme_dialog)
        self.buttonBox.accepted.connect(set_phoneme_dialog.accept)
        self.buttonBox.rejected.connect(set_phoneme_dialog.reject)

        QMetaObject.connectSlotsByName(set_phoneme_dialog)
    # setupUi

    def retranslateUi(self, set_phoneme_dialog):
        set_phoneme_dialog.setWindowTitle(QCoreApplication.translate("set_phoneme_dialog", u"\u8bbe\u7f6e\u97f3\u6807(\u62fc\u97f3)", None))
        self.groupBox.setTitle(QCoreApplication.translate("set_phoneme_dialog", u"\u7c7b\u578b", None))
        self.label.setText(QCoreApplication.translate("set_phoneme_dialog", u"\u8bbe\u7f6e\u97f3\u6807\u5b57\u6bcd\u8868", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("set_phoneme_dialog", u"\u97f3\u6807", None))
        self.label_2.setText(QCoreApplication.translate("set_phoneme_dialog", u"\u8bbe\u7f6e\u53d1\u97f3\u97f3\u6807", None))
    # retranslateUi

