# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Huffman.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from collections import Counter
import numpy as np

class Ui_UI_Huffman(object):
    def setupUi(self, UI_Huffman):
        UI_Huffman.setObjectName("UI_Huffman")
        UI_Huffman.resize(900, 720)
        self.TITLE = QtWidgets.QLabel(UI_Huffman)
        self.TITLE.setGeometry(QtCore.QRect(200, 30, 480, 100))
        self.TITLE.setObjectName("TITLE")
        self.Back_to_Start_button = QtWidgets.QPushButton(UI_Huffman)
        self.Back_to_Start_button.setGeometry(QtCore.QRect(740, 550, 150, 90))
        self.Back_to_Start_button.setObjectName("Back_to_Start_button")
        self.Input_Symbol_textedit = QtWidgets.QTextEdit(UI_Huffman)
        self.Input_Symbol_textedit.setGeometry(QtCore.QRect(40, 190, 260, 60))
        self.Input_Symbol_textedit.setObjectName("Input_Symbol_textedit")
        self.Input_Q_hint = QtWidgets.QLabel(UI_Huffman)
        self.Input_Q_hint.setGeometry(QtCore.QRect(50, 130, 220, 50))
        self.Input_Q_hint.setObjectName("Input_Q_hint")
        self.Input_N_textedit = QtWidgets.QTextEdit(UI_Huffman)
        self.Input_N_textedit.setGeometry(QtCore.QRect(360, 190, 100, 61))
        self.Input_N_textedit.setObjectName("Input_N_textedit")
        self.Input_N_hint = QtWidgets.QLabel(UI_Huffman)
        self.Input_N_hint.setGeometry(QtCore.QRect(350, 130, 140, 50))
        self.Input_N_hint.setObjectName("Input_N_hint")
        self.Input_R_textedit = QtWidgets.QTextEdit(UI_Huffman)
        self.Input_R_textedit.setGeometry(QtCore.QRect(610, 190, 100, 61))
        self.Input_R_textedit.setObjectName("Input_R_textedit")
        self.Input_R_hint = QtWidgets.QLabel(UI_Huffman)
        self.Input_R_hint.setGeometry(QtCore.QRect(580, 130, 150, 50))
        self.Input_R_hint.setObjectName("Input_R_hint")
        self.Generate_button = QtWidgets.QPushButton(UI_Huffman)
        self.Generate_button.setGeometry(QtCore.QRect(740, 400, 150, 90))
        self.Generate_button.setObjectName("Generate_button")
        self.Output_textbrowser = QtWidgets.QTextBrowser(UI_Huffman)
        self.Output_textbrowser.setGeometry(QtCore.QRect(40, 310, 671, 381))
        self.Output_textbrowser.setObjectName("Output_textbrowser")
        self.Output_hint = QtWidgets.QLabel(UI_Huffman)
        self.Output_hint.setGeometry(QtCore.QRect(140, 270, 471, 41))
        self.Output_hint.setObjectName("Output_hint")

        self.retranslateUi(UI_Huffman)
        QtCore.QMetaObject.connectSlotsByName(UI_Huffman)

        # 返回按钮点下回到start界面
        self.Back_to_Start_button.clicked.connect(self.backToStart)
        # 生成按钮事件
        self.Generate_button.clicked.connect(self.display)

    #返回界面操作
    def backToStart(self):
        from start import Ui_Form
        self.start_window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.start_window)
        self.start_window.show()
        QtWidgets.QWidget.close(self.Back_to_Start_button.window())



    #按键按下生成操作
    def display(self):
        import Huffman_Coding as H
        #检查Symbols输入
        Input_Symbols = self.Input_Symbol_textedit.toPlainText()
        if len(Input_Symbols) >= 8 and len(Input_Symbols)<=15:
            Input_Symbols = Input_Symbols
        else:
            self.Output_textbrowser.setText("注意输入符号的长度Q的范围！")
            return

        #检查N值输入
        Input_N = self.Input_N_textedit.toPlainText()
        try:
            Input_N = int(Input_N)
            if Input_N >=1 and Input_N <= 3:
                Input_N =Input_N
            else:
                self.Output_textbrowser.setText("请输入正确的N值！")
                return
        except:
            self.Output_textbrowser.setText("请输入正确的N值！")
            return

        #检查R值输入
        Input_R = self.Input_R_textedit.toPlainText()
        try:
            Input_R = int(Input_R)
            if Input_R >=2 and Input_R <= 5:
                Input_R =Input_R
            else:
                self.Output_textbrowser.setText("请输入正确的R值！")
                return
        except:
            self.Output_textbrowser.setText("请输入正确的R值！")
            return
        #Huffman检查Symbol是否可以整除N
        if len(Input_Symbols)%Input_N == 0:
            Input_N = Input_N
        else:
            self.Output_textbrowser.setText("注意输入符号的长度Q是N的整数倍！")
            return
        #输入检查完毕，开始计算Huffman编码以及各项指标
        symbol_probabilities = sort_symbol(Input_Symbols)
        #Huffman码表
        Huffman_table = H.huffman_encode(symbol_probabilities,Input_R,Input_N)
        #Huffman编码后的字符串
        pre_coding_symbol = [Input_Symbols[i:i + Input_N] for i in range(0, len(Input_Symbols), Input_N)]
        Symbols_After_Huffman_Encoding = []

        # 1.对照Huffman码表编码，打印编码后的Symbols
        for i in pre_coding_symbol:
            for symbol, huffman_code in Huffman_table.items():
                if i == symbol:
                    Symbols_After_Huffman_Encoding.append(huffman_code)

        # 2.计算并打印平均码长
        Aver_len_H = H.aver_code_length(symbol_probabilities, Input_R, Input_N)

        #3.计算并打印信息熵以及编码效率
        Info_Entropy_H = H.Entropy(symbol_probabilities, Input_N)
        #print('N重信源编码后的信息熵:', Info_Entropy_H)
        Ave_l_lbr_H = Aver_len_H * np.log2(Input_R)
        Encoding_Efficiency_H = Info_Entropy_H / Ave_l_lbr_H
        #print('编码效率:', Encoding_Efficiency_H)
        # 将文本设置到输出框中
        output_text = f"{'哈夫曼编码表如下：'}\n{Huffman_table}\n\n{'经过Huffman编码后的信息:'}\n{Symbols_After_Huffman_Encoding}" \
                      f"\n\n{'平均码长:'}\n{Aver_len_H}\n\n{'N重信源编码后的信息熵:'}\n{Info_Entropy_H}\n\n{'编码效率:'}\n{Encoding_Efficiency_H}"
        self.Output_textbrowser.setText(output_text)
        # self.Output_textbrowser.setText(Input_Symbols)

    def retranslateUi(self, UI_Huffman):
        _translate = QtCore.QCoreApplication.translate
        UI_Huffman.setWindowTitle(_translate("UI_Huffman", "UI_Huffman"))
        self.TITLE.setText(_translate("UI_Huffman", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Huffman编码</span></p><p align=\"center\"><span style=\" font-size:16pt;\">任意Q符号N重序列信源的最优R进制编码</span></p><p><br/></p></body></html>"))
        self.Back_to_Start_button.setText(_translate("UI_Huffman", "返回到初始界面"))
        self.Input_Symbol_textedit.setHtml(_translate("UI_Huffman", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Input_Q_hint.setText(_translate("UI_Huffman", "<html><head/><body><p>在这里输入符号</p><p>注意符号长度:8 &lt;= Q &lt;= 15</p></body></html>"))
        self.Input_N_hint.setText(_translate("UI_Huffman", "<html><head/><body><p>输入N</p><p>注意：1&lt;= N &lt;=3</p></body></html>"))
        self.Input_R_hint.setText(_translate("UI_Huffman", "<html><head/><body><p>输入进制R</p><p>注意：2&lt;= R &lt;=5</p></body></html>"))
        self.Generate_button.setText(_translate("UI_Huffman", "Generate"))
        self.Output_hint.setText(_translate("UI_Huffman", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">运行结果</span></p></body></html>"))

    # #symbol概率计算函数
def sort_symbol(Symbols):
    symbol_counts = Counter(Symbols)
    # 计算总字母数
    total_symbols = len(Symbols)
    # 计算每个字母的概率
    symbol_probabilities = [[symbol, count / total_symbols] for symbol, count in symbol_counts.items()]
    # 从大到小排序
    symbol_probabilities = sorted(symbol_probabilities, key=lambda x: x[1], reverse=True)
    return symbol_probabilities

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    #import pics_ui_rc # 导入添加的资源（根据实际情况填写文件名）
    app = QApplication(sys.argv)
    UI_Huffman = QMainWindow()
    ui = Ui_UI_Huffman()
    ui.setupUi(UI_Huffman)
    UI_Huffman.show()
    sys.exit(app.exec_())