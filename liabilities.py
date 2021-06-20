from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import QSize


class LiabilitiesDialog(QDialog):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.setWindowTitle("Liabilities")
        self.setMinimumSize(QSize(981, 619))
        self.setWindowIcon(QtGui.QIcon("./assets/liabilities.png"))

        self.label = QtWidgets.QLabel(self)
        self.update = QtWidgets.QPushButton(self)
        self.text_4 = QtWidgets.QLabel(self)
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.text_3 = QtWidgets.QLabel(self)
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.text_2 = QtWidgets.QLabel(self)
        self.text_1 = QtWidgets.QLabel(self)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.label_8 = QtWidgets.QLabel(self)
        self.label_7 = QtWidgets.QLabel(self)
        self.int_3 = QtWidgets.QLabel(self)
        self.int_2 = QtWidgets.QLabel(self)
        self.int_1 = QtWidgets.QLabel(self)
        self.label_6 = QtWidgets.QLabel(self)
        self.value2_2 = QtWidgets.QLabel(self)
        self.value1_3 = QtWidgets.QLabel(self)
        self.value1_2 = QtWidgets.QLabel(self)
        self.label_5 = QtWidgets.QLabel(self)
        self.pay1 = QtWidgets.QPushButton(self)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_3 = QtWidgets.QLabel(self)
        self.qty3 = QtWidgets.QLabel(self)
        self.qty2 = QtWidgets.QLabel(self)
        self.qty1 = QtWidgets.QLabel(self)
        self.value3 = QtWidgets.QLabel(self)
        self.value2 = QtWidgets.QLabel(self)
        self.value1 = QtWidgets.QLabel(self)
        self.item3 = QtWidgets.QLabel(self)
        self.item2 = QtWidgets.QLabel(self)
        self.item1 = QtWidgets.QLabel(self)
        self.label_2 = QtWidgets.QLabel(self)

        self.setupUi()

    def setupUi(self):
        self.label.setGeometry(QtCore.QRect(420, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2.setGeometry(QtCore.QRect(70, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.item1.setGeometry(QtCore.QRect(70, 120, 141, 21))
        self.item1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.item1.setObjectName("item1")
        self.item2.setGeometry(QtCore.QRect(70, 160, 171, 21))
        self.item2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.item2.setObjectName("item2")
        self.item3.setGeometry(QtCore.QRect(70, 200, 111, 21))
        self.item3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.item3.setObjectName("item3")
        self.value1.setGeometry(QtCore.QRect(230, 120, 101, 20))
        self.value1.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value1.setObjectName("value1")
        self.value2.setGeometry(QtCore.QRect(400, 160, 131, 16))
        self.value2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value2.setObjectName("value2")
        self.value3.setGeometry(QtCore.QRect(400, 200, 121, 20))
        self.value3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value3.setObjectName("value3")
        self.qty1.setGeometry(QtCore.QRect(590, 120, 81, 21))
        self.qty1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qty1.setObjectName("qty1")
        self.qty2.setGeometry(QtCore.QRect(590, 160, 81, 21))
        self.qty2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qty2.setObjectName("qty2")
        self.qty3.setGeometry(QtCore.QRect(590, 200, 81, 21))
        self.qty3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.qty3.setObjectName("qty3")
        self.label_3.setGeometry(QtCore.QRect(230, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4.setGeometry(QtCore.QRect(580, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pay1.setGeometry(QtCore.QRect(680, 490, 121, 31))
        self.pay1.setObjectName("pay1")
        self.label_5.setGeometry(QtCore.QRect(390, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.value1_2.setGeometry(QtCore.QRect(230, 160, 101, 20))
        self.value1_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value1_2.setObjectName("value1_2")
        self.value1_3.setGeometry(QtCore.QRect(230, 200, 101, 20))
        self.value1_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value1_3.setObjectName("value1_3")
        self.value2_2.setGeometry(QtCore.QRect(400, 120, 131, 16))
        self.value2_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.value2_2.setObjectName("value2_2")
        self.label_6.setGeometry(QtCore.QRect(770, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.int_1.setGeometry(QtCore.QRect(780, 120, 81, 21))
        self.int_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.int_1.setObjectName("int_1")
        self.int_2.setGeometry(QtCore.QRect(780, 160, 81, 21))
        self.int_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.int_2.setObjectName("int_2")
        self.int_3.setGeometry(QtCore.QRect(780, 200, 81, 21))
        self.int_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.int_3.setObjectName("int_3")
        self.label_7.setGeometry(QtCore.QRect(90, 320, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8.setGeometry(QtCore.QRect(590, 320, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lineEdit.setGeometry(QtCore.QRect(670, 370, 201, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.text_1.setGeometry(QtCore.QRect(590, 370, 81, 21))
        self.text_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.text_1.setObjectName("text_1")
        self.text_2.setGeometry(QtCore.QRect(590, 420, 81, 21))
        self.text_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.text_2.setObjectName("text_2")
        self.lineEdit_2.setGeometry(QtCore.QRect(670, 420, 201, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 370, 201, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.text_3.setGeometry(QtCore.QRect(100, 370, 81, 21))
        self.text_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.text_3.setObjectName("text_3")
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 420, 201, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.text_4.setGeometry(QtCore.QRect(40, 420, 141, 21))
        self.text_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.text_4.setObjectName("text_4")
        self.update.setGeometry(QtCore.QRect(200, 480, 121, 31))
        self.update.setObjectName("update")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Dialog", "My Liabilities"))
        self.label_2.setText(_translate("Dialog", "Item"))
        self.item1.setText(_translate("Dialog", "Student Loan"))
        self.item2.setText(_translate("Dialog", "Car Loan"))
        self.item3.setText(_translate("Dialog", "Mortgage"))
        self.value1.setText(_translate("Dialog", "$10K"))
        self.value2.setText(_translate("Dialog", "$200/month"))
        self.value3.setText(_translate("Dialog", "$4000/month"))
        self.qty1.setText(_translate("Dialog", "30 years"))
        self.qty2.setText(_translate("Dialog", "5 years"))
        self.qty3.setText(_translate("Dialog", "30 years"))
        self.label_3.setText(_translate("Dialog", "Principal"))
        self.label_4.setText(_translate("Dialog", "Repayment Period"))
        self.pay1.setText(_translate("Dialog", "Pay"))
        self.label_5.setText(_translate("Dialog", "Monthly Payment"))
        self.value1_2.setText(_translate("Dialog", "$10K"))
        self.value1_3.setText(_translate("Dialog", "$400K"))
        self.value2_2.setText(_translate("Dialog", "$200/month"))
        self.label_6.setText(_translate("Dialog", "Interest Rate"))
        self.int_1.setText(_translate("Dialog", "2%"))
        self.int_2.setText(_translate("Dialog", "2.5%"))
        self.int_3.setText(_translate("Dialog", "3%"))
        self.label_7.setText(_translate("Dialog", "Update my repayment schedule"))
        self.label_8.setText(_translate("Dialog", "Repay Liability in Advance"))
        self.text_1.setText(_translate("Dialog", "Liability"))
        self.text_2.setText(_translate("Dialog", "Amount"))
        self.text_3.setText(_translate("Dialog", "Liability"))
        self.text_4.setText(_translate("Dialog", "Monthly Payment"))
        self.update.setText(_translate("Dialog", "Update"))
