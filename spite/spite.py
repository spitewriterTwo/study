# import sys      #导入python的系统类库
# from PyQt5 import QtCore, QtGui, QtWidgets    #导入.py的模块
# from PyQt5.QtGui import QIcon
# import requests
# from multiprocessing import Pool    #引入线程池，加快下载的速度
#
#
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")   #设置窗体对象的名称
#         Form.resize(863, 199)       #窗体的大小
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(30, 30, 81, 31))
#         self.label.setObjectName("label")
#         self.pushButton = QtWidgets.QPushButton(Form)
#         self.pushButton.setGeometry(QtCore.QRect(760, 110, 93, 31))
#         self.pushButton.setObjectName("pushButton")
#         self.lineEdit = QtWidgets.QLineEdit(Form)
#         self.lineEdit.setGeometry(QtCore.QRect(130, 30, 621, 31))
#         self.lineEdit.setObjectName("lineEdit")
#         self.label_2 = QtWidgets.QLabel(Form)
#         self.label_2.setGeometry(QtCore.QRect(30, 110, 81, 31))
#         self.label_2.setObjectName("label_2")
#         self.lineEdit_2 = QtWidgets.QLineEdit(Form)
#         self.lineEdit_2.setGeometry(QtCore.QRect(130, 110, 621, 31))
#         self.lineEdit_2.setObjectName("lineEdit_2")
#
#         self.retranslateUi(Form)    #重新翻译一下
#         #self.pushButton.clicked.connect(Form.start_spite)  写这段之后那么和ui绑定的类就要实现start_spite
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "全能电影解析器"))
#         self.label.setText(_translate("Form", "电影的名字"))
#         self.pushButton.setText(_translate("Form", "启动"))
#         self.label_2.setText(_translate("Form", "电影的链接"))
#         self.pushButton.clicked.connect(self.start_spite)           #在这里定义槽函数
#
#     def start_spite(self):
#         name = self.lineEdit.text();
#         link = self.lineEdit_2.text();
#         data = requests.get(link)
#         with open(name + ".mp4", "wb") as file:
#             file.write(data.content)
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     form = QtWidgets.QWidget()
#     form.setWindowIcon(QIcon("./img/back.jpg"))
#     ui = Ui_Form()
#     ui.setupUi(form)
#     form.show()
#     sys.exit(app.exec())
