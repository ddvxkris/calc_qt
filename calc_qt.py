# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from tkinter import messagebox as ms
try:
    from PyQt6 import QtCore, QtGui, QtWidgets
except ModuleNotFoundError:
    ms.showerror(title="calc_qt", message="Нужен пакет PyQT6 чтобы запустить калькулятор! (терминал -> pip install pyqt6)")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 292)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.action_divide = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_divide.sizePolicy().hasHeightForWidth())
        self.action_divide.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.action_divide.setFont(font)
        self.action_divide.setObjectName("action_divide")
        self.gridLayout.addWidget(self.action_divide, 5, 3, 1, 1)
        self.result = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result.sizePolicy().hasHeightForWidth())
        self.result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.gridLayout.addWidget(self.result, 0, 0, 1, 4)
        self.num6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num6.sizePolicy().hasHeightForWidth())
        self.num6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num6.setFont(font)
        self.num6.setObjectName("num6")
        self.gridLayout.addWidget(self.num6, 3, 2, 1, 1)
        self.num1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num1.sizePolicy().hasHeightForWidth())
        self.num1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num1.setFont(font)
        self.num1.setObjectName("num1")
        self.gridLayout.addWidget(self.num1, 4, 0, 1, 1)
        self.action_multiply = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_multiply.sizePolicy().hasHeightForWidth())
        self.action_multiply.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.action_multiply.setFont(font)
        self.action_multiply.setObjectName("action_multiply")
        self.gridLayout.addWidget(self.action_multiply, 4, 3, 1, 1)
        self.action_minus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_minus.sizePolicy().hasHeightForWidth())
        self.action_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.action_minus.setFont(font)
        self.action_minus.setObjectName("action_minus")
        self.gridLayout.addWidget(self.action_minus, 3, 3, 1, 1)
        self.num3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num3.sizePolicy().hasHeightForWidth())
        self.num3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num3.setFont(font)
        self.num3.setObjectName("num3")
        self.gridLayout.addWidget(self.num3, 4, 2, 1, 1)
        self.numdot = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numdot.sizePolicy().hasHeightForWidth())
        self.numdot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.numdot.setFont(font)
        self.numdot.setObjectName("numdot")
        self.gridLayout.addWidget(self.numdot, 5, 2, 1, 1)
        self.num9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num9.sizePolicy().hasHeightForWidth())
        self.num9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num9.setFont(font)
        self.num9.setObjectName("num9")
        self.gridLayout.addWidget(self.num9, 1, 2, 1, 1)
        self.num4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num4.sizePolicy().hasHeightForWidth())
        self.num4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num4.setFont(font)
        self.num4.setObjectName("num4")
        self.gridLayout.addWidget(self.num4, 3, 0, 1, 1)
        self.num2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num2.sizePolicy().hasHeightForWidth())
        self.num2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num2.setFont(font)
        self.num2.setObjectName("num2")
        self.gridLayout.addWidget(self.num2, 4, 1, 1, 1)
        self.backspace = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backspace.sizePolicy().hasHeightForWidth())
        self.backspace.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.backspace.setFont(font)
        self.backspace.setObjectName("backspace")
        self.gridLayout.addWidget(self.backspace, 5, 0, 1, 1)
        self.num7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num7.sizePolicy().hasHeightForWidth())
        self.num7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num7.setFont(font)
        self.num7.setObjectName("num7")
        self.gridLayout.addWidget(self.num7, 1, 0, 1, 1)
        self.action_plus = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_plus.sizePolicy().hasHeightForWidth())
        self.action_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.action_plus.setFont(font)
        self.action_plus.setObjectName("action_plus")
        self.gridLayout.addWidget(self.action_plus, 1, 3, 1, 1)
        self.num5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num5.sizePolicy().hasHeightForWidth())
        self.num5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num5.setFont(font)
        self.num5.setObjectName("num5")
        self.gridLayout.addWidget(self.num5, 3, 1, 1, 1)
        self.num0 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num0.sizePolicy().hasHeightForWidth())
        self.num0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num0.setFont(font)
        self.num0.setObjectName("num0")
        self.gridLayout.addWidget(self.num0, 5, 1, 1, 1)
        self.special_equals = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.special_equals.sizePolicy().hasHeightForWidth())
        self.special_equals.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.special_equals.setFont(font)
        self.special_equals.setObjectName("special_equals")
        self.gridLayout.addWidget(self.special_equals, 8, 3, 1, 1)
        self.special_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.special_clear.sizePolicy().hasHeightForWidth())
        self.special_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.special_clear.setFont(font)
        self.special_clear.setObjectName("special_clear")
        self.gridLayout.addWidget(self.special_clear, 8, 1, 1, 1)
        self.special_repeat = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.special_repeat.sizePolicy().hasHeightForWidth())
        self.special_repeat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.special_repeat.setFont(font)
        self.special_repeat.setObjectName("special_repeat")
        self.gridLayout.addWidget(self.special_repeat, 8, 2, 1, 1)
        self.num8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num8.sizePolicy().hasHeightForWidth())
        self.num8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.num8.setFont(font)
        self.num8.setObjectName("num8")
        self.gridLayout.addWidget(self.num8, 1, 1, 1, 1)
        self.special_history = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.special_history.sizePolicy().hasHeightForWidth())
        self.special_history.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(20)
        self.special_history.setFont(font)
        self.special_history.setObjectName("special_history")
        self.gridLayout.addWidget(self.special_history, 8, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.functionality()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calc_qt"))
        self.action_divide.setText(_translate("MainWindow", "/"))
        self.result.setText(_translate("MainWindow", "0"))
        self.num6.setText(_translate("MainWindow", "6"))
        self.num1.setText(_translate("MainWindow", "1"))
        self.action_multiply.setText(_translate("MainWindow", "*"))
        self.action_minus.setText(_translate("MainWindow", "-"))
        self.num3.setText(_translate("MainWindow", "3"))
        self.numdot.setText(_translate("MainWindow", "."))
        self.num9.setText(_translate("MainWindow", "9"))
        self.num4.setText(_translate("MainWindow", "4"))
        self.num2.setText(_translate("MainWindow", "2"))
        self.backspace.setText(_translate("MainWindow", "<-"))
        self.num7.setText(_translate("MainWindow", "7"))
        self.action_plus.setText(_translate("MainWindow", "+"))
        self.num5.setText(_translate("MainWindow", "5"))
        self.num0.setText(_translate("MainWindow", "0"))
        self.special_equals.setText(_translate("MainWindow", "="))
        self.special_clear.setText(_translate("MainWindow", "C"))
        self.special_repeat.setText(_translate("MainWindow", "R"))
        self.num8.setText(_translate("MainWindow", "8"))
        self.special_history.setText(_translate("MainWindow", "H"))

    # actual logic starts here


    actions = {"plus": "+", "minus": "-", "multiply": "*", "divide": "/"}
    history: list = []

    def functionality(self):
        self.current_sequence.first = "0"
        self.num0.clicked.connect(lambda: self.add("0"))
        self.num1.clicked.connect(lambda: self.add("1"))
        self.num2.clicked.connect(lambda: self.add("2"))
        self.num3.clicked.connect(lambda: self.add("3"))
        self.num4.clicked.connect(lambda: self.add("4"))
        self.num5.clicked.connect(lambda: self.add("5"))
        self.num6.clicked.connect(lambda: self.add("6"))
        self.num7.clicked.connect(lambda: self.add("7"))
        self.num8.clicked.connect(lambda: self.add("8"))
        self.num9.clicked.connect(lambda: self.add("9"))
        self.numdot.clicked.connect(lambda: self.add("."))
        self.action_plus.clicked.connect(lambda: self.add(self.actions["plus"]))
        self.action_minus.clicked.connect(lambda: self.add(self.actions["minus"]))
        self.action_multiply.clicked.connect(lambda: self.add(self.actions["multiply"]))
        self.action_divide.clicked.connect(lambda: self.add(self.actions["divide"]))
        self.backspace.clicked.connect(self.clear_last)
        self.special_equals.clicked.connect(self.calculate)
        self.special_clear.clicked.connect(self.clear_all)
        self.special_history.clicked.connect(self.history_last_show)
        self.special_repeat.clicked.connect(self.repeat)

    class Sequence:
        first: str = ""
        second: str = ""
        action: str = ""

    current_sequence: Sequence = Sequence()
    current_operand: int = 1

    last_was_action = False

    def add(self, char: str):
        text = self.result.text()
        is_action = self.check_for_action(char)

        if is_action and self.current_operand == 2 and not self.last_was_action:
            print(is_action, self.current_operand, self.last_was_action)
            if self.calculate():
                self.current_sequence.action = char
                self.current_operand = 2
                self.last_was_action = True
                self.result.setText(f"{self.current_sequence.first}{self.current_sequence.action}{self.current_sequence.second}")
            return
        self.last_was_action = is_action
        if not is_action:
            self.append_operand(char)
            if self.current_operand == 1:
                self.current_sequence.action = ""
        else:
            self.current_sequence.action = char
            self.current_operand = 2
        self.result.setText(f"{self.current_sequence.first}{self.current_sequence.action}{self.current_sequence.second}")

    def check_for_action(self, text: str) -> bool:
        for el in self.actions.values():
            if text.__contains__(el):
                return True
        return False

    def append_operand(self, text: str):
        if self.current_operand == 1:
            self.current_sequence.first = self.current_sequence.first + text if self.current_sequence.first != "0" else text
        else:
            self.current_sequence.second = self.current_sequence.second + text if self.current_sequence.second != "0" else text

    def clear_last(self):
        text = self.result.text()
        if len(text) > 1:
            text_list = list(text)
            if self.check_for_action(text_list[-1]):
                self.last_was_action = False
                self.current_operand = 1
                self.current_sequence.action = ""
            text_list[-1] = ""
            text = ""
            for el in text_list:
                if el != "":
                    text += el
            self.result.setText(text)
            if self.current_operand == 1:
                self.current_sequence.first = text
            else:
                self.current_sequence.second = text
        else:
            self.result.setText("0")

    def clear_all(self):
        self.current_sequence.first = "0"
        self.current_sequence.second = ""
        self.current_sequence.action = ""
        self.last_was_action = False
        self.current_operand = 1
        self.result.setText("0")

    def history_last_show(self):
        try:
            self.result.setText(self.history[-1].first + self.history[-1].action + self.history[-1].second)
            self.current_operand = 2
            self.current_sequence = self.history[-1]
            self.history.pop(-1)
        except IndexError:
            ms.showerror(title="calc_ddvx", message="История пуста.")

    def repeat(self):
        try:
            float(self.result.text())
        except (TypeError, ValueError):
            ms.showerror(title="calc_ddvx", message="Проведите действие!")
            return
        sequence = self.Sequence()
        try:
            sequence = self.history[-1]
        except IndexError:
            ms.showerror(title="calc_ddvx", message="История пуста!")
            return
        sequence.first = self.result.text()
        self.current_sequence = sequence
        self.calculate()

    def calculate(self) -> bool:
        try:
            first, second, action = self.current_sequence.first, self.current_sequence.second, self.current_sequence.action
            result = (str(eval(first + action + second)) + " ").replace(".0 ", "").replace(" ", "")
            self.result.setText(result)

            history_sequence = self.Sequence()
            history_sequence.first = first
            history_sequence.second = second
            history_sequence.action = action

            self.history.append(history_sequence)

            self.current_sequence.first = result
            self.current_operand = 1
            self.current_sequence.second = ""
            return True
        except (ValueError, SyntaxError, ZeroDivisionError):
            ms.showerror(title="calc_ddvx", message="Неправильное действие!")
            return False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
