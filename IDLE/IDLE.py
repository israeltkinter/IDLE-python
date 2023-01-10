from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import subprocess
import sys
import os
import keyboard
import color


class Ui_MainWindow(object):
    def __init__(self, path, text_changed):
        self.path_window = path
        self.text_changed = text_changed

    def setupUi1(self, Form):
        Form.setObjectName("Form")
        Form.resize(301, 154)
        Form.setMaximumSize(QtCore.QSize(301, 154))
        self.labelf = QtWidgets.QLabel(Form)
        self.labelf.setGeometry(QtCore.QRect(20, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelf.setFont(font)
        self.labelf.setObjectName("label")
        self.label_2f = QtWidgets.QLabel(Form)
        self.label_2f.setGeometry(QtCore.QRect(20, 110, 51, 16))
        self.label_3f = QtWidgets.QLabel(Form)
        self.label_3f.setGeometry(QtCore.QRect(20, 75, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2f.setFont(font)
        self.label_2f.setObjectName("label_2")
        self.label_3f.setFont(font)
        self.label_3f.setObjectName("label_2")
        self.lineEditf = QtWidgets.QLineEdit(Form)
        self.lineEditf.setGeometry(QtCore.QRect(80, 40, 113, 20))
        self.lineEditf.setObjectName("lineEdit")
        self.lineEdit_2f = QtWidgets.QLineEdit(Form)
        self.lineEdit_2f.setGeometry(QtCore.QRect(80, 110, 113, 20))
        self.lineEdit_2f.setObjectName("lineEdit_2")
        self.pushButtonf = QtWidgets.QPushButton(Form, clicked=self.find_word)
        self.pushButtonf.setGeometry(QtCore.QRect(220, 40, 75, 23))
        self.pushButtonf.setObjectName("pushButton")
        self.pushButton_2f = QtWidgets.QPushButton(Form, clicked=self.replace)
        self.pushButton_2f.setGeometry(QtCore.QRect(220, 110, 75, 23))
        self.pushButton_2f.setObjectName("pushButton_2")
        self.pushButtonf3 = QtWidgets.QPushButton(Form, clicked=self.find_next)
        self.pushButtonf3.setGeometry(QtCore.QRect(220, 75, 75, 23))
        self.pushButtonf3.setObjectName("pushButton")

        self.retranslateUi1(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi1(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Find"))
        self.labelf.setText(_translate("Form", "Find:"))
        self.label_2f.setText(_translate("Form", "Replace:"))
        self.label_3f.setText(_translate("Form", "Next:"))
        self.pushButtonf.setText(_translate("Form", "find"))
        self.pushButton_2f.setText(_translate("Form", "replace"))
        self.pushButtonf3.setText(_translate("Form", "find next"))


    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1148, 781)
        self.MainWindow.setMaximumSize(1148,781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 761, 731))
        self.textEdit.textChanged.connect(self.set_text_changed1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.add_indent)
        self.textEdit.textChanged.connect(self.add_Apostrophes)
        self.textEdit.textChanged.connect(self.add_Parenthesis)



        self.label = QtWidgets.QTextEdit(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 0, 381, 731))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgba(0, 0, 0, 255);\n"
"color:rgba(84, 168, 84, 255);")
        self.label.setReadOnly(True)
        self.label.setObjectName("label")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp_2 = QtWidgets.QMenu(self.menubar)
        self.menuHelp_2.setObjectName("menuHelp_2")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(self.new)
        self.actionNew.setShortcut("Ctrl+A")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.open)
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save)
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(self.save_as)
        self.actionSave_As.setShortcut("Ctrl+Alt+S")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")


        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.triggered.connect(lambda :self.textEdit.undo())
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRedo.triggered.connect(lambda :self.textEdit.redo())
        self.actionRedo.setShortcut("Ctrl+Y")

        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCut.triggered.connect(lambda :self.textEdit.cut())
        self.actionCut.setShortcut("Ctrl+X")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCopy.triggered.connect(lambda :self.textEdit.copy())
        self.actionCopy.setShortcut("Ctrl+C")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPaste.triggered.connect(lambda :self.textEdit.paste())
        self.actionPaste.setShortcut("Ctrl+V")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionSelect_All.triggered.connect(lambda :self.textEdit.selectAll())
        self.actionSelect_All.setShortcut("Ctrl+A")
        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionFind.triggered.connect(self.open_window)
        self.actionFind.setShortcut("Ctrl+F")
        self.actionFind_Again = QtWidgets.QAction(MainWindow)
        self.actionFind_Again.setObjectName("actionFind_Again")
        self.actionFind_Again.triggered.connect(self.find_next)
        self.actionFind_Again.setShortcut("Ctrl+G")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit_2.triggered.connect(self.closeEvent)
        self.actionExit_2.setShortcut("Ctrl+Q")
        self.actionExit_3 = QtWidgets.QAction(MainWindow)
        self.actionExit_3.setObjectName("actionExit_3")
        self.actionExit_3.triggered.connect(lambda :sys.exit(1))
        self.actionExit_3.setShortcut("Ctrl+Alt+Q")
        self.actionConfigure = QtWidgets.QAction(MainWindow)
        self.actionConfigure.setObjectName("actionConfigure")
        self.actionConfigure.triggered.connect(self.run)
        self.actionConfigure.setShortcut("F5")
        self.actionPysehll = QtWidgets.QAction(MainWindow)
        self.actionPysehll.setObjectName("actionPysehll")
        self.actionPysehll.triggered.connect(self.run_pyshell)
        self.actionPysehll.setShortcut("Ctrl+Alt+O")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionautomatic_save = QtWidgets.QAction(MainWindow,  checkable=True)
        self.actionautomatic_save.setObjectName("actionautomatic_save")
        self.actionautomatic_save.triggered.connect(self.automatic_save)

        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuFile.addAction(self.actionExit_3)
        self.menuNew.addAction(self.actionUndo)
        self.menuNew.addAction(self.actionRedo)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionCut)
        self.menuNew.addAction(self.actionCopy)
        self.menuNew.addAction(self.actionPaste)
        self.menuNew.addAction(self.actionSelect_All)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionFind)
        self.menuNew.addAction(self.actionFind_Again)
        self.menuOptions.addAction(self.actionConfigure)
        self.menuOptions.addAction(self.actionPysehll)

        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionautomatic_save)
        self.menuHelp_2.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuHelp_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow.closeEvent = self.closeEvent
        self.add_color()











    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowFlags(self.window.windowFlags() & QtCore.Qt.CustomizeWindowHint)
        self.window.setWindowFlags(self.window.windowFlags() & ~QtCore.Qt.WindowMinMaxButtonsHint)
        self.ui = self.setupUi1(self.window)
        self.window.show()



    def set_file_path(self, path):
        self.path_window = path


    def set_text_changed1(self):
        self.text_changed = True
        if self.path_window != "":
            self.MainWindow.setWindowTitle(f"IDLE Python - *{self.path_window}")
        else:
            self.MainWindow.setWindowTitle(f"IDLE Python - *untitled")

    def set_text_changed0(self):
        self.text_changed = False
        if self.path_window != "":
            self.MainWindow.setWindowTitle(f"IDLE Python - {self.path_window}")
        else:
            self.MainWindow.setWindowTitle(f"IDLE Python - untitled")

    def new(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow("",False)
        self.ui2.setupUi(self.window2)
        self.window2.show()


    def open(self):
        options1 = "Python File (*.py) \n All Files (*.*)"
        self.path3 = QFileDialog.getOpenFileName(caption='Open python file', filter=options1)
        try:
            with open(self.path3[0], "r", encoding="UTF-8") as file:
                read = file.read()
                self.textEdit.setText(read)
                self.set_file_path(self.path3[0])
                self.MainWindow.setWindowTitle(f"IDLE Python - {self.path_window}")
                self.set_text_changed0()
        except (FileNotFoundError, UnicodeDecodeError):
            msg1 = QMessageBox.critical(self.MainWindow,
                                         "ERROR",
                                         "An error occurred opening the file \n Check if the file is found and if the file is a Python file",
                                         QMessageBox.Ok)


    def save(self):
        options1 = "Python File (*.py) \n All Files (*.*)"
        if self.path_window == "":
            self.path = QFileDialog.getSaveFileName(caption="Python File", filter=options1)
            try:
                with open(self.path[0], "w", encoding="UTF-8") as file:
                    file.write(self.textEdit.toPlainText())
                    self.set_file_path(self.path[0])
                    self.MainWindow.setWindowTitle(f"IDLE Python - {self.path_window}")
                    self.set_text_changed0()
            except FileNotFoundError:
                pass
        else:
            with open(self.path_window, "w", encoding="UTF-8") as file:
                file.write(self.textEdit.toPlainText())
                self.set_text_changed0()



    def save_as(self):
        options1 = "Python File (*.py) \n All Files (*.*)"
        self.path2 = QFileDialog.getSaveFileName(caption="Python File", filter=options1)
        try:
            with open(self.path2[0], "w", encoding="UTF-8") as file:
                file.write(self.textEdit.toPlainText())
                self.set_file_path(self.path2[0])
                self.set_text_changed0()
                self.MainWindow.setWindowTitle(f"IDLE Python - {self.path_window}")
        except FileNotFoundError:
            pass

    def automatic_save(self):
        if self.path_window == "" and self.actionautomatic_save.isChecked():
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Critical)
            msg2.setText("Autosave cannot be enabled due to the following\n reason No file selected")
            font = QtGui.QFont()
            font.setPointSize(10)
            msg2.setFont(font)

            # setting Message box window title
            msg2.setWindowTitle("Error")

            # declaring buttons on Message Box
            msg2.setStandardButtons(QMessageBox.Ok)

            # start the app
            retval = msg2.exec_()
            self.actionautomatic_save.setChecked(False)
        elif self.actionautomatic_save.isChecked():
            self.textEdit.textChanged.connect(self.save)
        elif self.actionautomatic_save.isChecked() == False:
            self.textEdit.textChanged.disconnect(self.save)


    def mbox(self):
        if self.text_changed or (self.textEdit.toPlainText().strip() == "" and self.path_window == ""):
            msg2 = QMessageBox.question(self.MainWindow,
                                         "RUN",
                                         "Do you want to save the changes\n to the file before running it?",
                                         QMessageBox.Ok | QMessageBox.Cancel)
            if msg2 == QMessageBox.Ok:
                self.save()
                if self.path_window == "":
                    close = QMessageBox.critical(self.MainWindow,
                                                 "ERROR",
                                                 "not selected a file",
                                                 QMessageBox.Ok)
            else:
                if self.path_window == "":
                    close = QMessageBox.critical(self.MainWindow,
                                                 "ERROR",
                                                 "not selected a file",
                                                 QMessageBox.Ok)

    def closeEvent(self, event):
        if self.text_changed:
            close = QMessageBox.question(self.MainWindow,
                                         "QUIT",
                                         "Do you want to save the changes\n to the file before closed file?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if close == QMessageBox.Yes:
                self.save()
                try:
                    event.accept()
                except AttributeError:
                    self.MainWindow.destroy()
            elif close == QMessageBox.No:
                try:
                    event.accept()
                except AttributeError:
                    self.MainWindow.destroy()
            elif close == QMessageBox.Cancel:
                try:
                    event.ignore()
                except AttributeError:
                    pass
        else:
            try:
                event.accept()
            except AttributeError:
                self.MainWindow.destroy()




    def find_word(self):
        self.textEdit.moveCursor(QtGui.QTextCursor.Start)
        self.find = self.textEdit.find(self.lineEditf.text())





    def find_next(self):
        self.textEdit.moveCursor(QtGui.QTextCursor.NextWord)
        try:
            self.find = self.textEdit.find(self.lineEditf.text())
        except AttributeError:
            pass

    def replace(self):
        if self.find:
            self.textEdit.insertPlainText(self.lineEdit_2f.text())



    def run(self):
        self.mbox()
        if self.path_window != "":
            process = subprocess.Popen(f'python "{self.path_window}"', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            error2 = error.decode(encoding="iso8859_8")
            output2 = output.decode(encoding='iso8859_8')
            output3 = str(output2)
            error3 = str(error2)

            self.label.setText("")
            self.label.insertPlainText(output3)
            self.label.insertPlainText(error3 if error != b'' else "\n")
            if error != b'':
                self.label.setStyleSheet("background-color:rgba(0, 0, 0, 255);\ncolor:rgba(238, 75, 43,255);")
            else:
                self.label.setStyleSheet("background-color:rgba(0, 0, 0, 255);\ncolor:rgba(84, 168, 84, 255);")


    def run_pyshell(self):
        try:
            os.startfile("python.exe")
        except FileNotFoundError:
            pass



    def add_indent(self):
        count = self.textEdit.toPlainText().count(":")
        insert = "    "
        if self.textEdit.toPlainText().endswith("\n"):
            self.textEdit.insertPlainText(insert * count)


    def add_Apostrophes(self):
        if self.textEdit.toPlainText().endswith(' "'):
            self.textEdit.insertPlainText('"')
            keyboard.press("left")
        elif self.textEdit.toPlainText().endswith(" '"):
            self.textEdit.insertPlainText("'")
            keyboard.press("left")


    def add_Parenthesis(self):
        if self.textEdit.toPlainText().endswith("("):
            self.textEdit.insertPlainText(")")
            keyboard.press("left")
        elif self.textEdit.toPlainText().endswith("["):
            self.textEdit.insertPlainText("]")
            keyboard.press("left")
        elif self.textEdit.toPlainText().endswith("{"):
            self.textEdit.insertPlainText("}")
            keyboard.press("left")


    def add_color(self):
        words = color.PythonWords(self.textEdit)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IDLE Python  - untitled"))
        self.label.setText(_translate("MainWindow", f"python {sys.version} on {sys.platform}"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "Edit"))
        self.menuOptions.setTitle(_translate("MainWindow", "Run"))
        self.menuHelp.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp_2.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFind_Again.setText(_translate("MainWindow", "Find Next"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionExit_3.setText(_translate("MainWindow", "Exit All"))
        self.actionConfigure.setText(_translate("MainWindow", "Run Module"))
        self.actionPysehll.setText(_translate("MainWindow", "Python shell"))
        self.actionAbout.setText(_translate("MainWindow", "Configure"))
        self.actionautomatic_save.setText(_translate("MainWindow", "Automatic Save"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))


# זה למקרה ויש שגיאה ב self.textEdit.textChanged.connect שהישום לא יקרוס
# אז עשיתי תחליף לשגיאה את הפונקצייה הזאת והוא עדין מדפיס את השגיאה הזאת אבל הישום לא קורס

def excepthook(*args):
    STDERR = sys.stderr
    print >> STDERR, 'caught'
    print >> STDERR, args

sys.excepthook = excepthook


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("", False)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


