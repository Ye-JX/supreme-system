import sys
from PyQt5 import QtWidgets,QtCore
app=QtWidgets.QApplication(sys.argv)
widget=QtWidgets.QWidget()
widget.resize(360,360)
widget.setWindowTitle("Hello?")
widget.show()
app.exec_()
#sys.exit(app.exec_())