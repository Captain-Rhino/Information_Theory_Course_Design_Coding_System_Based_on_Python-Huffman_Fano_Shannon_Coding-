# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Fano.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI_Fano(object):
    def setupUi(self, UI_Fano):
        UI_Fano.setObjectName("UI_Fano")
        UI_Fano.resize(900, 720)
        self.TITLE = QtWidgets.QLabel(UI_Fano)
        self.TITLE.setGeometry(QtCore.QRect(200, 30, 480, 100))
        self.TITLE.setObjectName("TITLE")
        self.Back_to_Start_button = QtWidgets.QPushButton(UI_Fano)
        self.Back_to_Start_button.setGeometry(QtCore.QRect(740, 550, 150, 90))
        self.Back_to_Start_button.setObjectName("Back_to_Start_button")
        self.Input_Symbol_textedit = QtWidgets.QTextEdit(UI_Fano)
        self.Input_Symbol_textedit.setGeometry(QtCore.QRect(40, 190, 671, 60))
        self.Input_Symbol_textedit.setObjectName("Input_Symbol_textedit")
        self.Input_Q_hint = QtWidgets.QLabel(UI_Fano)
        self.Input_Q_hint.setGeometry(QtCore.QRect(50, 130, 191, 50))
        self.Input_Q_hint.setObjectName("Input_Q_hint")
        self.Generate_button = QtWidgets.QPushButton(UI_Fano)
        self.Generate_button.setGeometry(QtCore.QRect(740, 400, 150, 90))
        self.Generate_button.setObjectName("Generate_button")
        self.Output_textbrowser = QtWidgets.QTextBrowser(UI_Fano)
        self.Output_textbrowser.setGeometry(QtCore.QRect(40, 310, 671, 381))
        self.Output_textbrowser.setObjectName("Output_textbrowser")
        self.Output_hint = QtWidgets.QLabel(UI_Fano)
        self.Output_hint.setGeometry(QtCore.QRect(140, 270, 471, 41))
        self.Output_hint.setObjectName("Output_hint")

        self.retranslateUi(UI_Fano)
        QtCore.QMetaObject.connectSlotsByName(UI_Fano)

    def retranslateUi(self, UI_Fano):
        _translate = QtCore.QCoreApplication.translate
        UI_Fano.setWindowTitle(_translate("UI_Fano", "UI_Fano"))
        self.TITLE.setText(_translate("UI_Fano", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Fano编码</span></p><p align=\"center\"><span style=\" font-size:16pt;\">任意Q符号信源的二进制编码</span></p><p><br/></p></body></html>"))
        self.Back_to_Start_button.setText(_translate("UI_Fano", "返回到初始界面"))
        self.Input_Symbol_textedit.setHtml(_translate("UI_Fano", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Input_Q_hint.setText(_translate("UI_Fano", "<html><head/><body><p>在这里输入符号</p><p>注意符号长度:Q &gt;= 10</p></body></html>"))
        self.Generate_button.setText(_translate("UI_Fano", "Generate"))
        self.Output_hint.setText(_translate("UI_Fano", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">运行结果</span></p></body></html>"))

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    #import pics_ui_rc # 导入添加的资源（根据实际情况填写文件名）
    app = QApplication(sys.argv)
    UI_Fano = QMainWindow()
    ui = Ui_UI_Fano()
    ui.setupUi(UI_Fano)
    UI_Fano.show()
    sys.exit(app.exec_())