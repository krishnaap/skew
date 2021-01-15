#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 20:47:43 2021

@author: krishna
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 20, 113, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 170, 501, 331))
        self.graphicsView.setInputMethodHints(QtCore.Qt.ImhNone)
        self.graphicsView.setObjectName("graphicsView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(290, 60, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(130, 60, 110, 23))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        self.menuSkewT_Plotter = QtWidgets.QMenu(self.menubar)
        self.menuSkewT_Plotter.setObjectName("menuSkewT_Plotter")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPlotting = QtWidgets.QAction(MainWindow)
        self.actionPlotting.setObjectName("actionPlotting")
        self.menubar.addAction(self.menuSkewT_Plotter.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select date</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Plot"))
        self.lineEdit.setText(_translate("MainWindow", "type station name"))
        self.label.setText(_translate("MainWindow", "Type station name"))
        self.label_2.setText(_translate("MainWindow", "Select the date"))
        self.menuSkewT_Plotter.setTitle(_translate("MainWindow", "SkewT Plotter"))
        self.actionPlotting.setText(_translate("MainWindow", "Plotting"))
        self.actionPlotting.setToolTip(_translate("MainWindow", "Plot the figure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
