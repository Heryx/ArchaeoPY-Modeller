# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created: Fri Nov 07 16:45:23 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1324, 822)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.Button_Grid = QtGui.QGridLayout()
        self.Button_Grid.setObjectName(_fromUtf8("Button_Grid"))
        self.pushButton_clear = QtGui.QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.Button_Grid.addWidget(self.pushButton_clear, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.Button_Grid.addItem(spacerItem, 0, 3, 1, 1)
        self.toolbar_grid = QtGui.QGridLayout()
        self.toolbar_grid.setObjectName(_fromUtf8("toolbar_grid"))
        self.Button_Grid.addLayout(self.toolbar_grid, 0, 0, 1, 1)
        self.pushButton_plot = QtGui.QPushButton(self.centralwidget)
        self.pushButton_plot.setObjectName(_fromUtf8("pushButton_plot"))
        self.Button_Grid.addWidget(self.pushButton_plot, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.Button_Grid, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 2, 0, 1, 1)
        self.mpl = MplWidget(self.centralwidget)
        self.mpl.setMinimumSize(QtCore.QSize(1024, 400))
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.gridLayout_6.addWidget(self.mpl, 0, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_feature = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_feature.sizePolicy().hasHeightForWidth())
        self.groupBox_feature.setSizePolicy(sizePolicy)
        self.groupBox_feature.setMinimumSize(QtCore.QSize(320, 290))
        self.groupBox_feature.setObjectName(_fromUtf8("groupBox_feature"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox_feature)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 24, 306, 251))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_width = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_width.setObjectName(_fromUtf8("label_width"))
        self.gridLayout_3.addWidget(self.label_width, 4, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_conductivity = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_conductivity.setObjectName(_fromUtf8("label_conductivity"))
        self.gridLayout_3.addWidget(self.label_conductivity, 0, 0, 1, 1)
        self.label_length = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_length.setObjectName(_fromUtf8("label_length"))
        self.gridLayout_3.addWidget(self.label_length, 3, 0, 1, 1)
        self.comboBox_conductivity = QtGui.QComboBox(self.gridLayoutWidget_2)
        self.comboBox_conductivity.setEditable(True)
        self.comboBox_conductivity.setObjectName(_fromUtf8("comboBox_conductivity"))
        self.comboBox_conductivity.addItem(_fromUtf8(""))
        self.comboBox_conductivity.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_conductivity, 0, 1, 1, 1)
        self.label_depth = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_depth.setObjectName(_fromUtf8("label_depth"))
        self.gridLayout_3.addWidget(self.label_depth, 2, 0, 1, 1)
        self.doubleSpinBox_magsus = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_magsus.setObjectName(_fromUtf8("doubleSpinBox_magsus"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_magsus, 1, 1, 1, 1)
        self.label_magsus = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_magsus.setObjectName(_fromUtf8("label_magsus"))
        self.gridLayout_3.addWidget(self.label_magsus, 1, 0, 1, 1)
        self.doubleSpinBox_depth = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_depth.setObjectName(_fromUtf8("doubleSpinBox_depth"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_depth, 2, 1, 1, 1)
        self.doubleSpinBox_width = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_width.setObjectName(_fromUtf8("doubleSpinBox_width"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_width, 4, 1, 1, 1)
        self.doubleSpinBox_length = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_length.setObjectName(_fromUtf8("doubleSpinBox_length"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_length, 3, 1, 1, 1)
        self.label_strike = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_strike.setObjectName(_fromUtf8("label_strike"))
        self.gridLayout_3.addWidget(self.label_strike, 5, 0, 1, 1)
        self.doubleSpinBox_strike = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_strike.setObjectName(_fromUtf8("doubleSpinBox_strike"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_strike, 5, 1, 1, 1)
        self.doubleSpinBox_depthextent = QtGui.QDoubleSpinBox(self.gridLayoutWidget_2)
        self.doubleSpinBox_depthextent.setObjectName(_fromUtf8("doubleSpinBox_depthextent"))
        self.gridLayout_3.addWidget(self.doubleSpinBox_depthextent, 6, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_feature, 0, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 6, 1, 1)
        self.groupBox_instrument = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_instrument.sizePolicy().hasHeightForWidth())
        self.groupBox_instrument.setSizePolicy(sizePolicy)
        self.groupBox_instrument.setMinimumSize(QtCore.QSize(310, 250))
        self.groupBox_instrument.setObjectName(_fromUtf8("groupBox_instrument"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.groupBox_instrument)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 294, 251))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_array = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_array.setObjectName(_fromUtf8("label_array"))
        self.gridLayout_4.addWidget(self.label_array, 0, 0, 1, 1)
        self.label_lowersensor = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_lowersensor.setObjectName(_fromUtf8("label_lowersensor"))
        self.gridLayout_4.addWidget(self.label_lowersensor, 4, 0, 1, 1)
        self.label_a1 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_a1.setObjectName(_fromUtf8("label_a1"))
        self.gridLayout_4.addWidget(self.label_a1, 2, 0, 1, 1)
        self.doubleSpinBox_lowersensor = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_lowersensor.setObjectName(_fromUtf8("doubleSpinBox_lowersensor"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_lowersensor, 4, 1, 1, 1)
        self.label_uppersensor = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_uppersensor.setObjectName(_fromUtf8("label_uppersensor"))
        self.gridLayout_4.addWidget(self.label_uppersensor, 5, 0, 1, 1)
        self.label_a = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_a.setObjectName(_fromUtf8("label_a"))
        self.gridLayout_4.addWidget(self.label_a, 1, 0, 1, 1)
        self.doubleSpinBox_uppersensor = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_uppersensor.setObjectName(_fromUtf8("doubleSpinBox_uppersensor"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_uppersensor, 5, 1, 1, 1)
        self.doubleSpinBox_a1 = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_a1.setObjectName(_fromUtf8("doubleSpinBox_a1"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_a1, 2, 1, 1, 1)
        self.label_a2 = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_a2.setObjectName(_fromUtf8("label_a2"))
        self.gridLayout_4.addWidget(self.label_a2, 3, 0, 1, 1)
        self.comboBox_array = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_array.setObjectName(_fromUtf8("comboBox_array"))
        self.gridLayout_4.addWidget(self.comboBox_array, 0, 1, 1, 1)
        self.doubleSpinBox_a = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_a.setObjectName(_fromUtf8("doubleSpinBox_a"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_a, 1, 1, 1, 1)
        self.doubleSpinBox_a2 = QtGui.QDoubleSpinBox(self.gridLayoutWidget_3)
        self.doubleSpinBox_a2.setObjectName(_fromUtf8("doubleSpinBox_a2"))
        self.gridLayout_4.addWidget(self.doubleSpinBox_a2, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_instrument, 0, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem3, 0, 4, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 0, 2, 1, 1)
        self.groupBox_survey = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_survey.sizePolicy().hasHeightForWidth())
        self.groupBox_survey.setSizePolicy(sizePolicy)
        self.groupBox_survey.setMinimumSize(QtCore.QSize(350, 210))
        self.groupBox_survey.setObjectName(_fromUtf8("groupBox_survey"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox_survey)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 20, 321, 141))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.doubleSpinBox_fieldinclination = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_fieldinclination.setObjectName(_fromUtf8("doubleSpinBox_fieldinclination"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_fieldinclination, 2, 1, 1, 1)
        self.label_traverselength = QtGui.QLabel(self.gridLayoutWidget)
        self.label_traverselength.setObjectName(_fromUtf8("label_traverselength"))
        self.gridLayout_2.addWidget(self.label_traverselength, 0, 0, 1, 1)
        self.label_fieldinclination = QtGui.QLabel(self.gridLayoutWidget)
        self.label_fieldinclination.setObjectName(_fromUtf8("label_fieldinclination"))
        self.gridLayout_2.addWidget(self.label_fieldinclination, 2, 0, 1, 1)
        self.label_traverseint = QtGui.QLabel(self.gridLayoutWidget)
        self.label_traverseint.setObjectName(_fromUtf8("label_traverseint"))
        self.gridLayout_2.addWidget(self.label_traverseint, 1, 0, 1, 1)
        self.doubleSpinBox_traverselength = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_traverselength.setObjectName(_fromUtf8("doubleSpinBox_traverselength"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_traverselength, 0, 1, 1, 1)
        self.doubleSpinBox_traverseint = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_traverseint.setObjectName(_fromUtf8("doubleSpinBox_traverseint"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_traverseint, 1, 2, 1, 1)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout_2.addWidget(self.doubleSpinBox, 0, 2, 1, 1)
        self.doubleSpinBox_samplingint = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_samplingint.setObjectName(_fromUtf8("doubleSpinBox_samplingint"))
        self.gridLayout_2.addWidget(self.doubleSpinBox_samplingint, 1, 1, 1, 1)
        self.groupBox_method = QtGui.QGroupBox(self.groupBox_survey)
        self.groupBox_method.setGeometry(QtCore.QRect(0, 180, 351, 121))
        self.groupBox_method.setObjectName(_fromUtf8("groupBox_method"))
        self.gridLayoutWidget_4 = QtGui.QWidget(self.groupBox_method)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 355, 95))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioButton_res = QtGui.QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_res.setObjectName(_fromUtf8("radioButton_res"))
        self.gridLayout.addWidget(self.radioButton_res, 0, 0, 1, 1)
        self.radioButton_mag = QtGui.QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_mag.setObjectName(_fromUtf8("radioButton_mag"))
        self.gridLayout.addWidget(self.radioButton_mag, 0, 1, 1, 1)
        self.radioButton_2d = QtGui.QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_2d.setObjectName(_fromUtf8("radioButton_2d"))
        self.buttonGroup_2D3D = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup_2D3D.setObjectName(_fromUtf8("buttonGroup_2D3D"))
        self.buttonGroup_2D3D.addButton(self.radioButton_2d)
        self.gridLayout.addWidget(self.radioButton_2d, 1, 0, 1, 1)
        self.radioButton_3d = QtGui.QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_3d.setObjectName(_fromUtf8("radioButton_3d"))
        self.buttonGroup_2D3D.addButton(self.radioButton_3d)
        self.gridLayout.addWidget(self.radioButton_3d, 1, 1, 1, 1)
        self.radioButton_pseudo = QtGui.QRadioButton(self.gridLayoutWidget_4)
        self.radioButton_pseudo.setObjectName(_fromUtf8("radioButton_pseudo"))
        self.buttonGroup_2D3D.addButton(self.radioButton_pseudo)
        self.gridLayout.addWidget(self.radioButton_pseudo, 2, 0, 1, 2)
        self.gridLayout_5.addWidget(self.groupBox_survey, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 3, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1324, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menu_About = QtGui.QMenu(self.menubar)
        self.menu_About.setObjectName(_fromUtf8("menu_About"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Save_Data = QtGui.QAction(MainWindow)
        self.action_Save_Data.setObjectName(_fromUtf8("action_Save_Data"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.menu_File.addAction(self.action_Save_Data)
        self.menu_File.addAction(self.action_Quit)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menubar.addAction(self.menu_About.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_plot.setText(_translate("MainWindow", "Plot", None))
        self.groupBox_feature.setTitle(_translate("MainWindow", "Feature Parameters", None))
        self.label_width.setText(_translate("MainWindow", "Width (y-extent)", None))
        self.label_8.setText(_translate("MainWindow", "Depth Extent (z-extent)", None))
        self.label_conductivity.setText(_translate("MainWindow", "Resistivity (rho)", None))
        self.label_length.setText(_translate("MainWindow", "Length (x-extent)", None))
        self.comboBox_conductivity.setItemText(0, _translate("MainWindow", "Insulating", None))
        self.comboBox_conductivity.setItemText(1, _translate("MainWindow", "Conducting", None))
        self.label_depth.setText(_translate("MainWindow", "Depth (Z)", None))
        self.label_magsus.setText(_translate("MainWindow", "Magnetic Susceptibility", None))
        self.label_strike.setText(_translate("MainWindow", "Strike (degrees)", None))
        self.groupBox_instrument.setTitle(_translate("MainWindow", "Instrument Parameters", None))
        self.label_array.setText(_translate("MainWindow", "Array", None))
        self.label_lowersensor.setText(_translate("MainWindow", "Lower Sensor Height (m)", None))
        self.label_a1.setText(_translate("MainWindow", "Electrode Separation (a1)", None))
        self.label_uppersensor.setText(_translate("MainWindow", "Upper Sensor Height (m)", None))
        self.label_a.setText(_translate("MainWindow", "Electrode Separation (a)", None))
        self.label_a2.setText(_translate("MainWindow", "Separation of Sides (a2)", None))
        self.groupBox_survey.setTitle(_translate("MainWindow", "Survey Parameters", None))
        self.label_traverselength.setText(_translate("MainWindow", " Length (x, y)", None))
        self.label_fieldinclination.setText(_translate("MainWindow", "Field Inclination", None))
        self.label_traverseint.setText(_translate("MainWindow", "Interval (x, y)", None))
        self.groupBox_method.setTitle(_translate("MainWindow", "Survey Type", None))
        self.radioButton_res.setText(_translate("MainWindow", "Resistivity", None))
        self.radioButton_mag.setText(_translate("MainWindow", "Magnetometry", None))
        self.radioButton_2d.setText(_translate("MainWindow", "2D", None))
        self.radioButton_3d.setText(_translate("MainWindow", "3D", None))
        self.radioButton_pseudo.setText(_translate("MainWindow", "Pseudosections", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        self.menu_About.setTitle(_translate("MainWindow", "&About", None))
        self.action_Save_Data.setText(_translate("MainWindow", "&Save Data", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))

from mplwidget import MplWidget
