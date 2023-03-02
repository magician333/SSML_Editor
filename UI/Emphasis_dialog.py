# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Emphasis_dialog.ui'
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
    QWidget)

class Ui_set_emphasis_dialog(object):
    def setupUi(self, set_emphasis_dialog):
        if not set_emphasis_dialog.objectName():
            set_emphasis_dialog.setObjectName(u"set_emphasis_dialog")
        set_emphasis_dialog.resize(341, 165)
        icon = QIcon()
        icon.addFile(u"editor.png", QSize(), QIcon.Normal, QIcon.Off)
        set_emphasis_dialog.setWindowIcon(icon)
        self.buttonBox = QDialogButtonBox(set_emphasis_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(140, 120, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(set_emphasis_dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(20, 20, 301, 80))
        self.set_emphasis_intensity = QComboBox(self.groupBox)
        self.set_emphasis_intensity.setObjectName(u"set_emphasis_intensity")
        self.set_emphasis_intensity.setGeometry(QRect(110, 30, 151, 22))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 91, 16))

        self.retranslateUi(set_emphasis_dialog)
        self.buttonBox.accepted.connect(set_emphasis_dialog.accept)
        self.buttonBox.rejected.connect(set_emphasis_dialog.reject)

        QMetaObject.connectSlotsByName(set_emphasis_dialog)
    # setupUi

    def retranslateUi(self, set_emphasis_dialog):
        set_emphasis_dialog.setWindowTitle(QCoreApplication.translate("set_emphasis_dialog", u"\u8bbe\u7f6e\u505c\u987f", None))
        self.groupBox.setTitle(QCoreApplication.translate("set_emphasis_dialog", u"\u5f3a\u5ea6", None))
        self.label.setText(QCoreApplication.translate("set_emphasis_dialog", u"\u8bbe\u7f6e\u5f3a\u8c03\u5f3a\u5ea6", None))
    # retranslateUi

