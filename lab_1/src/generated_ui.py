# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(872, 724)
        self.gridLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 761, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.KSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.KSlider.setOrientation(QtCore.Qt.Horizontal)
        self.KSlider.setObjectName("KSlider")
        self.gridLayout.addWidget(self.KSlider, 4, 4, 1, 1)
        self.RdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.RdoubleSpinBox.setMaximum(259.99)
        self.RdoubleSpinBox.setObjectName("RdoubleSpinBox")
        self.gridLayout.addWidget(self.RdoubleSpinBox, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 3, 1, 1)
        self.hlsLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.hlsLabel.setAutoFillBackground(False)
        self.hlsLabel.setObjectName("hlsLabel")
        self.gridLayout.addWidget(self.hlsLabel, 5, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.blueSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.blueSlider.setMaximum(255)
        self.blueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueSlider.setObjectName("blueSlider")
        self.gridLayout.addWidget(self.blueSlider, 3, 1, 1, 1)
        self.rgbLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.rgbLabel.setAutoFillBackground(False)
        self.rgbLabel.setStyleSheet("")
        self.rgbLabel.setObjectName("rgbLabel")
        self.gridLayout.addWidget(self.rgbLabel, 5, 1, 1, 1)
        self.HdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.HdoubleSpinBox.setMaximum(359.99)
        self.HdoubleSpinBox.setObjectName("HdoubleSpinBox")
        self.gridLayout.addWidget(self.HdoubleSpinBox, 1, 8, 1, 1)
        self.YdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.YdoubleSpinBox.setObjectName("YdoubleSpinBox")
        self.gridLayout.addWidget(self.YdoubleSpinBox, 3, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)
        self.HSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.HSlider.setMaximum(359)
        self.HSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HSlider.setObjectName("HSlider")
        self.gridLayout.addWidget(self.HSlider, 1, 7, 1, 1)
        self.YSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.YSlider.setOrientation(QtCore.Qt.Horizontal)
        self.YSlider.setObjectName("YSlider")
        self.gridLayout.addWidget(self.YSlider, 3, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)
        self.greenSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.greenSlider.setMaximum(255)
        self.greenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenSlider.setObjectName("greenSlider")
        self.gridLayout.addWidget(self.greenSlider, 2, 1, 1, 1)
        self.color = QtWidgets.QLabel(self.gridLayoutWidget)
        self.color.setAutoFillBackground(True)
        self.color.setText("")
        self.color.setObjectName("color")
        self.gridLayout.addWidget(self.color, 6, 0, 1, 8)
        self.BdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.BdoubleSpinBox.setMaximum(259.99)
        self.BdoubleSpinBox.setObjectName("BdoubleSpinBox_2")
        self.gridLayout.addWidget(self.BdoubleSpinBox, 3, 2, 1, 1)
        self.LdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.LdoubleSpinBox.setObjectName("LdoubleSpinBox")
        self.gridLayout.addWidget(self.LdoubleSpinBox, 3, 8, 1, 1)
        self.SSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.SSlider.setOrientation(QtCore.Qt.Horizontal)
        self.SSlider.setObjectName("SSlider")
        self.gridLayout.addWidget(self.SSlider, 2, 7, 1, 1) # 3, 7, 1, 1
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 6, 1, 1)
        self.CSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.CSlider.setOrientation(QtCore.Qt.Horizontal)
        self.CSlider.setObjectName("CSilde")
        self.gridLayout.addWidget(self.CSlider, 1, 4, 1, 1)
        self.LSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.LSlider.setOrientation(QtCore.Qt.Horizontal)
        self.LSlider.setObjectName("LSlider")
        self.gridLayout.addWidget(self.LSlider, 3, 7, 1, 1)
        self.SdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.SdoubleSpinBox.setObjectName("SdoubleSpinBox")
        self.gridLayout.addWidget(self.SdoubleSpinBox, 2, 8, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 6, 1, 1)
        self.cmykLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.cmykLabel.setAutoFillBackground(False)
        self.cmykLabel.setObjectName("cmykLabel")
        self.gridLayout.addWidget(self.cmykLabel, 5, 4, 1, 1)
        self.CdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.CdoubleSpinBox.setObjectName("CdoubleSpinBox")
        self.gridLayout.addWidget(self.CdoubleSpinBox, 1, 5, 1, 1)
        self.GdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.GdoubleSpinBox.setMaximum(259.99)
        self.GdoubleSpinBox.setObjectName("GdoubleSpinBox")
        self.gridLayout.addWidget(self.GdoubleSpinBox, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.MSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.MSlider.setOrientation(QtCore.Qt.Horizontal)
        self.MSlider.setObjectName("MSlider")
        self.gridLayout.addWidget(self.MSlider, 2, 4, 1, 1)
        self.MdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.MdoubleSpinBox.setObjectName("MdoubleSpinBox")
        self.gridLayout.addWidget(self.MdoubleSpinBox, 2, 5, 1, 1)
        self.redSlider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.redSlider.setAutoFillBackground(False)
        self.redSlider.setMaximum(255)
        self.redSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redSlider.setObjectName("redSlider")
        self.gridLayout.addWidget(self.redSlider, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.KdoubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.KdoubleSpinBox.setObjectName("KdoubleSpinBox")
        self.gridLayout.addWidget(self.KdoubleSpinBox, 4, 5, 1, 1)
        self.colorButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.colorButton.setObjectName("colorButton")
        self.gridLayout.addWidget(self.colorButton, 6, 8, 1, 1)
        MainWindow.setCentralWidget(self.gridLayoutWidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ColorConverter"))
        self.label_6.setText(_translate("MainWindow", "K"))
        self.hlsLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "B"))
        self.rgbLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "M"))
        self.label_3.setText(_translate("MainWindow", "R"))
        self.label_10.setText(_translate("MainWindow", "L"))
        self.label_7.setText(_translate("MainWindow", "Y"))
        self.label_8.setText(_translate("MainWindow", "H"))
        self.label_9.setText(_translate("MainWindow", "S"))
        self.cmykLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "G"))
        self.label_4.setText(_translate("MainWindow", "C"))
        self.colorButton.setText(_translate("MainWindow", "Выбрать цвет "))