import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QInputDialog, QMessageBox
from UI.Interface import Ui_MainWindow
from UI import Break_dialog, Quiet_dialog, Phoneme_dialog, Sayas_dialog, Style_dialog,Emphasis_dialog
import qdarktheme

Text = ""


class Break_Dialog(QDialog):
    def __init__(self, Text, selected):
        super(Break_Dialog, self).__init__()
        self.ui = Break_dialog.Ui_set_break_dialog()
        self.ui.setupUi(self)

        self.data = {"无停顿": 0, "很弱": 250, "弱": 500,
                     "中等(默认)": 750, "强": 1000, "很强": 1250, "最大": 5000}
        self.defalut_break = 750
        self.ui.set_break_intensity.addItems(self.data.keys())
        self.ui.set_break_intensity.setCurrentIndex(3)
        self.ui.set_break_time.setMaximum(5000)
        self.ui.set_break_time.setMinimum(0)
        self.ui.set_break_time.setValue(self.defalut_break)
        self.break_time = self.data[self.ui.set_break_intensity.currentText()]
        self.ui.show_break_time.setText(str(self.break_time)+"ms")
        self.Text = Text
        self.selected = selected

        self.ui.set_break_intensity.currentIndexChanged.connect(
            self.intensity_changed)
        self.ui.set_break_time.valueChanged.connect(self.time_changed)
        self.ui.buttonBox.accepted.connect(self.set_break)

    def intensity_changed(self):
        self.break_time = self.data[self.ui.set_break_intensity.currentText()]
        self.ui.set_break_time.setValue(self.break_time)
        self.ui.show_break_time.setText(str(self.break_time)+"ms")

    def time_changed(self):
        self.break_time = self.ui.set_break_time.value()
        self.ui.show_break_time.setText(str(self.break_time)+"ms")

        if self.break_time == 0:
            self.ui.set_break_intensity.setCurrentIndex(0)
        elif self.break_time > 0 and self.break_time <= 250:
            self.ui.set_break_intensity.setCurrentIndex(1)
        elif self.break_time > 250 and self.break_time <= 500:
            self.ui.set_break_intensity.setCurrentIndex(2)
        elif self.break_time > 500 and self.break_time <= 750:
            self.ui.set_break_intensity.setCurrentIndex(3)
        elif self.break_time > 750 and self.break_time <= 1000:
            self.ui.set_break_intensity.setCurrentIndex(4)
        elif self.break_time > 1000 and self.break_time <= 1250:
            self.ui.set_break_intensity.setCurrentIndex(5)
        elif self.break_time > 1250 and self.break_time < 5000:
            self.ui.set_break_intensity.setCurrentIndex(5)
        elif self.break_time == 5000:
            self.ui.set_break_intensity.setCurrentIndex(6)

    def set_break(self):
        global Text
        format_text = self.selected[0] + "<break time=\"" + \
            str(self.break_time) + "\"/>" + self.selected[2]+self.selected[1]
        self.Text.setPlainText(format_text)


class Quiet_Dialog(QDialog):
    def __init__(self, Text, selected):
        super(Quiet_Dialog, self).__init__()
        self.ui = Quiet_dialog.Ui_set_quiet_dialog()
        self.ui.setupUi(self)
        self.selected = selected
        self.Text = Text

        self.quiet_intensity = "Leading"
        self.data = {"文本开头的附加静音": "Leading",
                     "*文本开头的静音": "Leading-exact",
                     "文本末尾的附加静音": "Tailing",
                     "*文本末尾的静音": "Tailing-exact",
                     "相邻句子之间的附加静音": "Sentenceboundary",
                     "*相邻句子之间的静音": "Sentenceboundary-exact",
                     "*半角或全角格式的逗号处的静音": "Comma-exact",
                     "*半角或全角格式的分号处的静音": "Semicolon-exact",
                     "*全角格式的枚举逗号处的静音": "Enumerationcomma-exact"
                     }
        self.ui.set_quiet_intensity.addItems(self.data.keys())
        self.ui.set_quiet_time.setMaximum(5000)
        self.ui.set_quiet_time.setMinimum(0)
        self.quiet_time = 0

        self.ui.set_quiet_time.valueChanged.connect(self.time_changed)
        self.ui.buttonBox.accepted.connect(self.set_quiet)
        self.ui.set_quiet_intensity.currentIndexChanged.connect(
            self.intensity_changed)

    def intensity_changed(self):
        self.quiet_intensity = self.data[self.ui.set_quiet_intensity.currentText(
        )]

    def time_changed(self):
        self.quiet_time = self.ui.set_quiet_time.value()
        self.ui.show_quiet_time.setText(str(self.quiet_time)+"ms")

    def set_quiet(self):
        global Text
        format_text = self.selected[0] + "<mstts:silence  type=\""+self.quiet_intensity + \
            "\" value=\""+str(self.quiet_time)+"ms\"/>" + \
            self.selected[2]+self.selected[1]
        self.Text.setPlainText(format_text)


class Phoneme_Dialog(QDialog):
    def __init__(self, Text, selected):
        super(Phoneme_Dialog, self).__init__()
        self.ui = Phoneme_dialog.Ui_set_phoneme_dialog()
        self.ui.setupUi(self)
        self.selected = selected
        self.Text = Text

        self.phoneme_type = ["ipa", "spai", "ups", "x-sampa"]
        self.ui.set_phoneme_type.addItems(self.phoneme_type)

        self.ui.buttonBox.accepted.connect(self.set_phoneme)

    def set_phoneme(self):
        self.phoneme_type = self.ui.set_phoneme_type.currentText()
        self.phoneme_ph = self.ui.set_phoneme_ph.text()
        format_text = self.selected[0] + "<phoneme alphabet=\""+self.phoneme_type + \
            "\" ph=\""+self.phoneme_ph+"\">" + \
            self.selected[2]+"</phoneme>"+self.selected[1]
        self.Text.setPlainText(format_text)


class Sayas_Dialog(QDialog):
    def __init__(self, Text, selected):
        super(Sayas_Dialog, self).__init__()
        self.ui = Sayas_dialog.Ui_set_sayas_dialog()
        self.ui.setupUi(self)
        self.selected = selected
        self.Text = Text

        self.sayas_type = {"拼读": "characters", "基数": "cardinal", "序数": "ordinal", "序列": "number_digit", "分数": "fraction",
                           "日期": "date", "时间": "time", "持续时间": "duration", "电话号码": "telephone", "货币": "currency", "地址": "address", "人名": "name"}
        self.sayas_format = ""
        self.sayas_type_flag = ""  # 设置flag来确定从哪个format字典中读取数据 只需要日期、时间、持续时间三个有format的值即可

        self.ui.set_sayas_type.addItems(self.sayas_type.keys())
        self.ui.set_sayas_type.currentIndexChanged.connect(
            self.sayas_type_changed)
        self.ui.set_sayas_format.currentIndexChanged.connect(
            self.sayas_format_changed)
        self.ui.buttonBox.accepted.connect(self.set_sayas)

    def sayas_type_changed(self):
        if self.ui.set_sayas_type.currentText() == "日期":
            self.ui.set_sayas_format.clear()
            self.date_format = {"日-月-年": "dmy", "月-日-年": "mdy", "年-月-日": "ymd", "年-日-月": "ydm",
                                "年-月": "ym", "月-年": "my", "月-日": "md", "日-月": "dm", "日": "d", "月": "m", "年": "y"}
            self.ui.set_sayas_format.addItems(self.date_format)
            self.sayas_type_flag = "date"
            self.sayas_format = "dmy"  # 只有combox变化sayas_format_changed函数才生效，设置format默认值为第一项
        elif self.ui.set_sayas_type.currentText() == "时间":
            self.ui.set_sayas_format.clear()
            self.time_format = {"十二小时制": "hms12", "二十四小时制": "hms24"}
            self.ui.set_sayas_format.addItems(self.time_format)
            self.sayas_type_flag = "time"
            self.sayas_format = "hms12"  # 只有combox变化sayas_format_changed函数才生效，设置format默认值为第一项
        elif self.ui.set_sayas_type.currentText() == "持续时间":
            self.ui.set_sayas_format.clear()
            self.duration_format = {"时分秒": "hms", "时分": "hm", "分秒": "ms"}
            self.ui.set_sayas_format.addItems(self.duration_format)
            self.sayas_type_flag = "duration"
            self.sayas_format = "hms"  # 只有combox变化sayas_format_changed函数才生效，设置format默认值为第一项
        else:
            self.ui.set_sayas_format.clear()

    def sayas_format_changed(self):
        if self.sayas_type_flag == "date":
            self.sayas_format = self.date_format[self.ui.set_sayas_format.currentText(
            )]
        elif self.sayas_type_flag == "time":
            self.sayas_format = self.time_format[self.ui.set_sayas_format.currentText(
            )]
        elif self.sayas_type_flag == "duration":
            self.sayas_format = self.duration_format[self.ui.set_sayas_format.currentText(
            )]
        else:
            self.sayas_format = ""

    def set_sayas(self):
        self.sayas_detail = self.ui.set_sayas_detail.text()
        self.sayas_type_vaule = self.sayas_type[self.ui.set_sayas_type.currentText(
        )]
        if self.sayas_format == "" and self.sayas_detail == "":
            format_text = self.selected[0] + "<say-as interpret-as=\"" + \
                self.sayas_type_vaule+"\">" + \
                self.selected[2]+"</say-as>"+self.selected[1]
        elif self.sayas_format != "" and self.sayas_detail == "":
            format_text = self.selected[0] + "<say-as interpret-as=\""+self.sayas_type_vaule + \
                "\" format=\""+self.sayas_format+"\">" + \
                self.selected[2]+"</say-as>"+self.selected[1]
        elif self.sayas_format == "" and self.sayas_detail != "":
            format_text = self.selected[0] + "<say-as interpret-as=\""+self.sayas_type_vaule + \
                "\" detail=\""+self.sayas_detail+"</say-as>"+self.selected[1]
        elif self.sayas_format != "" and self.sayas_detail != "":
            format_text = self.selected[0] + "<say-as interpret-as=\""+self.sayas_type_vaule+"\" format=\"" + \
                self.sayas_format+"\" detail=\""+self.sayas_detail + \
                "\">"+self.selected[2]+"</say-as>"+self.selected[1]
        self.Text.setPlainText(format_text)


class Style_Dialog(QDialog):
    def __init__(self, Text, selected):
        super(Style_Dialog, self).__init__()
        self.ui = Style_dialog.Ui_set_style_dialog()
        self.ui.setupUi(self)
        self.selected = selected
        self.Text = Text

        self.style_data = ["advertisement_upbeat", "affectionate", "angry", "assistant", "calm", "chat", "cheerful", "customerservice", "depressed", "disgruntled", "documentary-narration", "embarrassed", "empathetic", "envious", "excited", "fearful", "friendly", "gentle",
                           "hopeful", "lyrical", "narration-professional", "narration-relaxed", "newscast", "newscast-casual", "newscast-formal", "poetry-reading", "sad", "serious", "shouting", "sports_commentary", "sports_commentary_excited", "whispering", "terrified", "unfriendly"]
        self.style_role = {"无":"","女孩":"Girl","男孩":"Boy","年轻女性":"YoungAdultFemale","年轻男性":"YoungAdultMale","年长女性":"OlderAdultFemale","年长男性":"OlderAdultMale","年老女性":"SeniorFemale","年老男性":"SeniorMale"}
        self.ui.set_style_style.addItems(self.style_data)
        self.ui.set_style_role.addItems(self.style_role.keys())
        self.ui.set_style_degree.setMaximum(2)
        self.ui.set_style_degree.setMinimum(0.01)
        self.ui.set_style_degree.setSingleStep(0.01)#步长存在bug，应当为0.01
        self.ui.set_style_degree.setValue(0.01)
        self.ui.set_style_degree.valueChanged.connect(self.degree_changed)
        self.ui.buttonBox.accepted.connect(self.set_style)

    def degree_changed(self):
        self.style_degree = self.ui.set_style_degree.value()
        self.ui.show_style_degree.setText(str(self.style_degree))
    
    def set_style(self):
        self.style_degree = str(self.ui.set_style_degree.value())
        self.style_style = self.ui.set_style_style.currentText()
        self.style_role = self.style_role[self.ui.set_style_role.currentText()] 

        format_text = self.selected[0]+"<mstts:express-as style=\""+self.style_style+"\" role=\""+self.style_role+"\" styledegree=\""+self.style_degree+">"+self.selected[2]+"</mstts:express-as>"+self.selected[1]
        self.Text.setPlainText(format_text)

class Emphasis_Dialog(QDialog):
    def __init__(self, Text, selected):
        super(Emphasis_Dialog, self).__init__()
        self.ui = Emphasis_dialog.Ui_set_emphasis_dialog()
        self.ui.setupUi(self)
        self.selected = selected
        self.Text = Text

        self.emphasis_data = {"减少":"reduced","无":"none","温和":"moderate","增强":"strong"}
        self.ui.set_emphasis_intensity.addItems(self.emphasis_data.keys())
        self.ui.set_emphasis_intensity.setCurrentIndex(2)

        self.ui.buttonBox.accepted.connect(self.set_emphasis)
    
    def set_emphasis(self):
        self.emphasis_intensity = self.emphasis_data[self.ui.set_emphasis_intensity.currentText()]
        format_text = self.selected[0]+"<emphasis level=\""+self.emphasis_intensity+"\">"+self.selected[2]+"</emphasis>"+self.selected[1]
        self.Text.setPlainText(format_text)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.set_break.clicked.connect(self.set_fun_break)
        self.ui.set_alias.clicked.connect(self.set_fun_alias)
        self.ui.set_quiet.clicked.connect(self.set_fun_quiet)
        self.ui.set_word.clicked.connect(self.set_fun_word)
        self.ui.set_sentence.clicked.connect(self.set_fun_sentence)
        self.ui.set_paragraphs.clicked.connect(self.set_fun_paragraphs)
        self.ui.set_phoneme.clicked.connect(self.set_fun_phoneme)
        self.ui.set_sayas.clicked.connect(self.set_fun_sayas)
        self.ui.set_style.clicked.connect(self.set_fun_style)
        self.ui.set_emphasis.clicked.connect(self.set_fun_emphasis)
        self.ui.set_audio.clicked.connect(self.set_fun_audio)
        self.ui.set_duration.clicked.connect(self.set_fun_duration)
        self.ui.copy_text.clicked.connect(self.set_fun_copytext)
        self.ui.paste_text.clicked.connect(self.set_fun_pastetext)

    def get_selected(self):
        global Text
        Text = self.ui.Text.toPlainText()
        start = Text[0:self.ui.Text.textCursor().selectionStart()]
        end = Text[self.ui.Text.textCursor().selectionEnd():]
        selected_text = self.ui.Text.textCursor().selectedText()
        return start, end, selected_text

    def set_fun_copytext(self):
        QApplication.clipboard().setText(self.ui.Text.toPlainText())

    def set_fun_pastetext(self):
        self.ui.Text.setPlainText(
            self.ui.Text.toPlainText()+QApplication.clipboard().text())

    def set_fun_break(self):
        self.break_dialog = Break_Dialog(self.ui.Text, self.get_selected())
        self.break_dialog.show()

    def set_fun_quiet(self):
        self.quiet_dialog = Quiet_Dialog(self.ui.Text, self.get_selected())
        self.quiet_dialog.show()

    def set_fun_alias(self):
        if self.get_selected()[2] != "":
            read_text = QInputDialog.getText(self, "别名", "请输入读取的别名")[0]
            if read_text != "":
                format_text = self.get_selected()[0]+"<sub alias=\""+read_text + \
                    "\">" + self.get_selected()[2] + \
                    "</sub>"+self.get_selected()[1]
                self.ui.Text.setPlainText(format_text)

    def set_fun_word(self):
        if self.get_selected()[2] != "":
            format_text = self.get_selected(
            )[0]+"<w>"+self.get_selected()[2]+"</w>"+self.get_selected()[1]
            self.ui.Text.setPlainText(format_text)

    def set_fun_sentence(self):
        if self.get_selected()[2] != "":
            format_text = self.get_selected(
            )[0]+"<s>"+self.get_selected()[2]+"</s>"+self.get_selected()[1]
            self.ui.Text.setPlainText(format_text)

    def set_fun_paragraphs(self):
        if self.get_selected()[2] != "":
            format_text = self.get_selected(
            )[0]+"<p>"+self.get_selected()[2]+"</p>"+self.get_selected()[1]
            self.ui.Text.setPlainText(format_text)

    def set_fun_phoneme(self):
        if self.get_selected()[2] != "":
            self.phoneme_dialog = Phoneme_Dialog(
                self.ui.Text, self.get_selected())
            self.phoneme_dialog.show()

    def set_fun_sayas(self):
        if self.get_selected()[2] != "":
            self.sayas_dialog = Sayas_Dialog(self.ui.Text, self.get_selected())
            self.sayas_dialog.show()

    def set_fun_style(self):
        if self.get_selected()[2] != "":
            self.style_dialog = Style_Dialog(self.ui.Text, self.get_selected())
            self.style_dialog.show()

    def set_fun_emphasis(self):
        if self.get_selected()[2] != "":
            self.emphasis_dialog = Emphasis_Dialog(self.ui.Text, self.get_selected())
            self.emphasis_dialog.show()
    
    def set_fun_audio(self):
        if self.get_selected()[2] != "":
            audio_src = QInputDialog.getText(self, "音频", "请输入背景音频地址")[0]
            if audio_src != "":
                format_text = self.get_selected()[0]+"<audio src=\""+audio_src + \
                    "\">" + self.get_selected()[2] + \
                    "</audio>"+self.get_selected()[1]
                self.ui.Text.setPlainText(format_text)

    def set_fun_duration(self):
        duration = str(QInputDialog.getInt(self,"持续时间","请输入本段话的持续时间",minValue=1)[0])
        format_text = self.get_selected()[0]+"<mstts:audioduration value=\""+duration+"s\"/>"+self.get_selected()[2]+self.get_selected()[1]
        self.ui.Text.setPlainText(format_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet("light"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
