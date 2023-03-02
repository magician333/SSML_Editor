# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Style_dialog.ui'
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

class Ui_set_style_dialog(object):
    def setupUi(self, set_style_dialog):
        if not set_style_dialog.objectName():
            set_style_dialog.setObjectName(u"set_style_dialog")
        set_style_dialog.resize(341, 359)
        icon = QIcon()
        icon.addFile(u"editor.png", QSize(), QIcon.Normal, QIcon.Off)
        set_style_dialog.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(set_style_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 320, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(set_style_dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(20, 20, 301, 80))
        self.set_style_style = QComboBox(self.groupBox)
        self.set_style_style.setObjectName(u"set_style_style")
        self.set_style_style.setGeometry(QRect(110, 30, 171, 22))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        self.set_style_style.setFont(font)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 91, 16))
        self.groupBox_2 = QGroupBox(set_style_dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QRect(20, 220, 301, 80))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 91, 16))
        self.set_style_degree = QSlider(self.groupBox_2)
        self.set_style_degree.setObjectName(u"set_style_degree")
        self.set_style_degree.setGeometry(QRect(110, 40, 141, 22))
        self.set_style_degree.setOrientation(Qt.Horizontal)
        self.show_style_degree = QLabel(self.groupBox_2)
        self.show_style_degree.setObjectName(u"show_style_degree")
        self.show_style_degree.setGeometry(QRect(260, 40, 31, 16))
        self.show_style_degree.setFont(font)
        self.groupBox_3 = QGroupBox(set_style_dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 120, 301, 80))
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 91, 16))
        self.set_style_role = QComboBox(self.groupBox_3)
        self.set_style_role.setObjectName(u"set_style_role")
        self.set_style_role.setGeometry(QRect(110, 40, 171, 22))
        self.set_style_role.setFont(font)

        self.retranslateUi(set_style_dialog)
        self.buttonBox.accepted.connect(set_style_dialog.accept)
        self.buttonBox.rejected.connect(set_style_dialog.reject)

        QMetaObject.connectSlotsByName(set_style_dialog)
    # setupUi

    def retranslateUi(self, set_style_dialog):
        set_style_dialog.setWindowTitle(QCoreApplication.translate("set_style_dialog", u"\u8bbe\u7f6e\u98ce\u683c", None))
        self.groupBox.setTitle(QCoreApplication.translate("set_style_dialog", u"\u98ce\u683c", None))
        self.label.setText(QCoreApplication.translate("set_style_dialog", u"\u8bbe\u7f6e\u8bb2\u8bdd\u98ce\u683c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("set_style_dialog", u"\u5f3a\u5ea6", None))
        self.label_2.setText(QCoreApplication.translate("set_style_dialog", u"\u8bbe\u7f6e\u98ce\u683c\u5f3a\u5ea6", None))
        self.show_style_degree.setText(QCoreApplication.translate("set_style_dialog", u"0.01", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("set_style_dialog", u"\u89d2\u8272", None))
        self.label_3.setText(QCoreApplication.translate("set_style_dialog", u"\u8bbe\u7f6e\u626e\u6f14\u89d2\u8272", None))
    # retranslateUi

