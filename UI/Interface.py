# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1114, 575)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setBold(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"editor.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(650, 10, 451, 261))
        font1 = QFont()
        font1.setBold(True)
        self.groupBox_4.setFont(font1)
        self.verticalLayoutWidget = QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 431, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 401, 27))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.set_break = QPushButton(self.horizontalLayoutWidget)
        self.set_break.setObjectName(u"set_break")

        self.horizontalLayout.addWidget(self.set_break)

        self.set_quiet = QPushButton(self.horizontalLayoutWidget)
        self.set_quiet.setObjectName(u"set_quiet")

        self.horizontalLayout.addWidget(self.set_quiet)

        self.set_word = QPushButton(self.horizontalLayoutWidget)
        self.set_word.setObjectName(u"set_word")

        self.horizontalLayout.addWidget(self.set_word)

        self.set_sentence = QPushButton(self.horizontalLayoutWidget)
        self.set_sentence.setObjectName(u"set_sentence")

        self.horizontalLayout.addWidget(self.set_sentence)

        self.set_paragraphs = QPushButton(self.horizontalLayoutWidget)
        self.set_paragraphs.setObjectName(u"set_paragraphs")

        self.horizontalLayout.addWidget(self.set_paragraphs)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 404, 27))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.set_phoneme = QPushButton(self.horizontalLayoutWidget_2)
        self.set_phoneme.setObjectName(u"set_phoneme")

        self.horizontalLayout_2.addWidget(self.set_phoneme)

        self.set_sayas = QPushButton(self.horizontalLayoutWidget_2)
        self.set_sayas.setObjectName(u"set_sayas")

        self.horizontalLayout_2.addWidget(self.set_sayas)

        self.set_alias = QPushButton(self.horizontalLayoutWidget_2)
        self.set_alias.setObjectName(u"set_alias")

        self.horizontalLayout_2.addWidget(self.set_alias)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 20, 406, 27))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.set_style = QPushButton(self.horizontalLayoutWidget_3)
        self.set_style.setObjectName(u"set_style")

        self.horizontalLayout_3.addWidget(self.set_style)

        self.set_prosody = QPushButton(self.horizontalLayoutWidget_3)
        self.set_prosody.setObjectName(u"set_prosody")

        self.horizontalLayout_3.addWidget(self.set_prosody)

        self.set_emphasis = QPushButton(self.horizontalLayoutWidget_3)
        self.set_emphasis.setObjectName(u"set_emphasis")

        self.horizontalLayout_3.addWidget(self.set_emphasis)

        self.set_audio = QPushButton(self.horizontalLayoutWidget_3)
        self.set_audio.setObjectName(u"set_audio")

        self.horizontalLayout_3.addWidget(self.set_audio)

        self.set_duration = QPushButton(self.horizontalLayoutWidget_3)
        self.set_duration.setObjectName(u"set_duration")

        self.horizontalLayout_3.addWidget(self.set_duration)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(650, 440, 111, 80))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.paste_text = QPushButton(self.verticalLayoutWidget_2)
        self.paste_text.setObjectName(u"paste_text")
        self.paste_text.setFont(font1)

        self.verticalLayout_2.addWidget(self.paste_text)

        self.copy_text = QPushButton(self.verticalLayoutWidget_2)
        self.copy_text.setObjectName(u"copy_text")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        self.copy_text.setFont(font2)

        self.verticalLayout_2.addWidget(self.copy_text)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(670, 290, 311, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label)

        self.set_speed = QSlider(self.horizontalLayoutWidget_4)
        self.set_speed.setObjectName(u"set_speed")
        self.set_speed.setMaximum(100)
        self.set_speed.setValue(0)
        self.set_speed.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.set_speed)

        self.show_speed = QLabel(self.horizontalLayoutWidget_4)
        self.show_speed.setObjectName(u"show_speed")

        self.horizontalLayout_4.addWidget(self.show_speed)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(670, 330, 311, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.set_tone = QSlider(self.horizontalLayoutWidget_5)
        self.set_tone.setObjectName(u"set_tone")
        self.set_tone.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.set_tone)

        self.show_tone = QLabel(self.horizontalLayoutWidget_5)
        self.show_tone.setObjectName(u"show_tone")

        self.horizontalLayout_5.addWidget(self.show_tone)

        self.Text = QTextEdit(self.centralwidget)
        self.Text.setObjectName(u"Text")
        self.Text.setGeometry(QRect(10, 10, 631, 511))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setUnderline(False)
        self.Text.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1114, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SSML\u7f16\u8f91\u5668", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"SSML\u7f16\u8f91", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u6784\u7f16\u8f91", None))
#if QT_CONFIG(statustip)
        self.set_break.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u5b83\u6765\u6dfb\u52a0\u6216\u9632\u6b62\u8bed\u97f3\u670d\u52a1\u4ee5\u5176\u4ed6\u65b9\u5f0f\u81ea\u52a8\u63d2\u5165\u7684\u6682\u505c", None))
#endif // QT_CONFIG(statustip)
        self.set_break.setText(QCoreApplication.translate("MainWindow", u"\u505c\u987f", None))
#if QT_CONFIG(statustip)
        self.set_quiet.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5728\u4e24\u4e2a\u76f8\u90bb\u53e5\u5b50\u4e4b\u95f4\u6dfb\u52a0\u6682\u505c", None))
#endif // QT_CONFIG(statustip)
        self.set_quiet.setText(QCoreApplication.translate("MainWindow", u"\u9759\u97f3", None))
#if QT_CONFIG(statustip)
        self.set_word.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9009\u4e2d\u5b57\u7b26\u4e3a\u8bcd\u7ec4\u8fdb\u884c\u8fde\u8bfb\uff08\u4e2d\u6587\u53ef\u80fd\u6548\u679c\u4e0d\u4f73\uff09", None))
#endif // QT_CONFIG(statustip)
        self.set_word.setText(QCoreApplication.translate("MainWindow", u"\u8bcd\u7ec4", None))
#if QT_CONFIG(statustip)
        self.set_sentence.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9009\u4e2d\u5b57\u7b26\u4e3a\u53e5\u5b50", None))
#endif // QT_CONFIG(statustip)
        self.set_sentence.setText(QCoreApplication.translate("MainWindow", u"\u53e5\u5b50", None))
#if QT_CONFIG(statustip)
        self.set_paragraphs.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9009\u4e2d\u5b57\u7b26\u4e3a\u6bb5\u843d", None))
#endif // QT_CONFIG(statustip)
        self.set_paragraphs.setText(QCoreApplication.translate("MainWindow", u"\u6bb5\u843d", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53d1\u97f3\u7f16\u8f91", None))
#if QT_CONFIG(statustip)
        self.set_phoneme.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9009\u4e2d\u6587\u672c\u7684\u8bfb\u97f3\uff08\u97f3\u6807\u6216\u62fc\u97f3\u7b49\uff09", None))
#endif // QT_CONFIG(statustip)
        self.set_phoneme.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u6807", None))
#if QT_CONFIG(statustip)
        self.set_sayas.setStatusTip(QCoreApplication.translate("MainWindow", u"\u4e3a\u8bed\u97f3\u5408\u6210\u5f15\u64ce\u63d0\u4f9b\u6709\u5173\u5982\u4f55\u6717\u8bfb\u6587\u672c\u7684\u6307\u5bfc", None))
#endif // QT_CONFIG(statustip)
        self.set_sayas.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u6cd5", None))
#if QT_CONFIG(statustip)
        self.set_alias.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9009\u4e2d\u6587\u672c\u5e94\u8bfb\u51fa\u7684\u522b\u540d\u5c5e\u6027\u6587\u672c\u503c\uff0c\u800c\u4e0d\u662f\u5143\u7d20\u4e2d\u5305\u542b\u7684\u6587\u672c", None))
#endif // QT_CONFIG(statustip)
        self.set_alias.setText(QCoreApplication.translate("MainWindow", u"\u522b\u540d", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u98ce\u683c\u7f16\u8f91", None))
#if QT_CONFIG(statustip)
        self.set_style.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9009\u4e2d\u6587\u672c\u58f0\u97f3\u7279\u5b9a\u7684\u8bb2\u8bdd\u98ce\u683c\u548c\u626e\u6f14\u7684\u89d2\u8272\uff08\u4ec5\u652f\u6301\u81ea\u5b9a\u4e49\u503c\uff09", None))
#endif // QT_CONFIG(statustip)
        self.set_style.setText(QCoreApplication.translate("MainWindow", u"\u98ce\u683c", None))
#if QT_CONFIG(statustip)
        self.set_prosody.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7528\u4e8e\u8bbe\u7f6e\u9009\u4e2d\u6587\u672c\u7684\u97f3\u8282\u3001\u8c03\u578b\u3001\u8303\u56f4\u3001\u901f\u7387\u548c\u97f3\u91cf\u7684\u53d8\u5316", None))
#endif // QT_CONFIG(statustip)
        self.set_prosody.setText(QCoreApplication.translate("MainWindow", u"\u97f5\u5f8b", None))
#if QT_CONFIG(statustip)
        self.set_emphasis.setStatusTip(QCoreApplication.translate("MainWindow", u"\u7528\u4e8e\u8bbe\u7f6e\u6587\u672c\u7684\u5355\u8bcd\u7ea7\u5f3a\u8c03", None))
#endif // QT_CONFIG(statustip)
        self.set_emphasis.setText(QCoreApplication.translate("MainWindow", u"\u5f3a\u8c03", None))
        self.set_audio.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891", None))
#if QT_CONFIG(statustip)
        self.set_duration.setStatusTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u9009\u4e2d\u6587\u672c\u7684\u6301\u7eed\u65f6\u95f4", None))
#endif // QT_CONFIG(statustip)
        self.set_duration.setText(QCoreApplication.translate("MainWindow", u"\u6301\u7eed\u65f6\u95f4", None))
#if QT_CONFIG(tooltip)
        self.paste_text.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ec5\u5728\u8bbe\u7f6e\u8bed\u97f3\u5408\u6210API\u540e\u6709\u6548", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.paste_text.setStatusTip(QCoreApplication.translate("MainWindow", u"\u5c06\u6587\u672c\u7c98\u8d34\u5230\u6587\u672c\u6846\u4e2d", None))
#endif // QT_CONFIG(statustip)
        self.paste_text.setText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34\u6587\u672c", None))
#if QT_CONFIG(statustip)
        self.copy_text.setStatusTip(QCoreApplication.translate("MainWindow", u"\u63a8\u8350\uff1a\u590d\u5236\u6587\u672c\u5230\u76f8\u5173\u8bed\u97f3\u751f\u6210\u7cfb\u7edf\u4e2d", None))
#endif // QT_CONFIG(statustip)
        self.copy_text.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u6587\u672c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u901f", None))
#if QT_CONFIG(tooltip)
        self.set_speed.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ec5\u5728\u8bbe\u7f6e\u8bed\u97f3\u5408\u6210API\u540e\u6709\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.show_speed.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u8c03", None))
#if QT_CONFIG(tooltip)
        self.set_tone.setToolTip(QCoreApplication.translate("MainWindow", u"\u4ec5\u5728\u8bbe\u7f6e\u8bed\u97f3\u5408\u6210API\u540e\u6709\u6548", None))
#endif // QT_CONFIG(tooltip)
        self.show_tone.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

