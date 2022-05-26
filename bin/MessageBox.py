from PyQt5.QtWidgets import QMessageBox


class MessageBox:
    def __init__(self, title, text, msg):
        self.box = QMessageBox()
        self.box.setText(text)
        self.box.setInformativeText(msg)
        self.box.setWindowTitle(title)

    def showerror(self):
        self.box.setIcon(QMessageBox.Critical)
        self.box.exec_()

    def showinfo(self):
        self.box.setIcon(QMessageBox.Information)
        self.box.exec_()

    def showwarning(self):
        self.box.setIcon(QMessageBox.Warning)
        self.box.exec_()
