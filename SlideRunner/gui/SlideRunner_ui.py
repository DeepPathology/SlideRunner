# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SlideRunner_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(905, 797)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setAcceptDrops(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.MainImage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainImage.sizePolicy().hasHeightForWidth())
        self.MainImage.setSizePolicy(sizePolicy)
        self.MainImage.setMinimumSize(QtCore.QSize(400, 400))
        self.MainImage.setLineWidth(0)
        self.MainImage.setAlignment(QtCore.Qt.AlignCenter)
        self.MainImage.setObjectName("MainImage")
        self.verticalLayout.addWidget(self.MainImage)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setMaximum(999)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.verticalLayout.addWidget(self.horizontalScrollBar)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(200, 10))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.OverviewLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OverviewLabel.sizePolicy().hasHeightForWidth())
        self.OverviewLabel.setSizePolicy(sizePolicy)
        self.OverviewLabel.setMinimumSize(QtCore.QSize(200, 200))
        self.OverviewLabel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OverviewLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.OverviewLabel.setObjectName("OverviewLabel")
        self.verticalLayout_2.addWidget(self.OverviewLabel)
        self.filenameLabel = QtWidgets.QLabel(self.centralwidget)
        self.filenameLabel.setObjectName("filenameLabel")
        self.verticalLayout_2.addWidget(self.filenameLabel)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.categoryView = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryView.sizePolicy().hasHeightForWidth())
        self.categoryView.setSizePolicy(sizePolicy)
        self.categoryView.setMinimumSize(QtCore.QSize(200, 100))
        self.categoryView.setMaximumSize(QtCore.QSize(16777215, 120))
        self.categoryView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.categoryView.setObjectName("categoryView")
        self.categoryView.setColumnCount(0)
        self.categoryView.setRowCount(0)
        self.verticalLayout_2.addWidget(self.categoryView)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.statisticView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statisticView.sizePolicy().hasHeightForWidth())
        self.statisticView.setSizePolicy(sizePolicy)
        self.statisticView.setObjectName("statisticView")
        self.verticalLayout_2.addWidget(self.statisticView)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QtCore.QSize(200, 0))
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.threshold_label = QtWidgets.QLabel(self.centralwidget)
        self.threshold_label.setObjectName("threshold_label")
        self.verticalLayout_2.addWidget(self.threshold_label)
        self.threshold = QtWidgets.QSlider(self.centralwidget)
        self.threshold.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold.sizePolicy().hasHeightForWidth())
        self.threshold.setSizePolicy(sizePolicy)
        self.threshold.setProperty("value", 40)
        self.threshold.setOrientation(QtCore.Qt.Horizontal)
        self.threshold.setObjectName("threshold")
        self.verticalLayout_2.addWidget(self.threshold)
        self.opacityLabel = QtWidgets.QLabel(self.centralwidget)
        self.opacityLabel.setObjectName("opacityLabel")
        self.verticalLayout_2.addWidget(self.opacityLabel)
        self.opacitySlider = QtWidgets.QSlider(self.centralwidget)
        self.opacitySlider.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opacitySlider.sizePolicy().hasHeightForWidth())
        self.opacitySlider.setSizePolicy(sizePolicy)
        self.opacitySlider.setProperty("value", 50)
        self.opacitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.opacitySlider.setObjectName("opacitySlider")
        self.verticalLayout_2.addWidget(self.opacitySlider)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 22))
        self.menubar.setObjectName("menubar")
        self.menuDatabase = QtWidgets.QMenu(self.menubar)
        self.menuDatabase.setObjectName("menuDatabase")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAnnotation = QtWidgets.QMenu(self.menubar)
        self.menuAnnotation.setObjectName("menuAnnotation")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.action_Close = QtWidgets.QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.actionOpen_custom = QtWidgets.QAction(MainWindow)
        self.actionOpen_custom.setObjectName("actionOpen_custom")
        self.actionMode = QtWidgets.QAction(MainWindow)
        self.actionMode.setObjectName("actionMode")
        self.actionAdd_annotator = QtWidgets.QAction(MainWindow)
        self.actionAdd_annotator.setEnabled(False)
        self.actionAdd_annotator.setObjectName("actionAdd_annotator")
        self.actionAdd_cell_class = QtWidgets.QAction(MainWindow)
        self.actionAdd_cell_class.setEnabled(False)
        self.actionAdd_cell_class.setObjectName("actionAdd_cell_class")
        self.actionCreate_new = QtWidgets.QAction(MainWindow)
        self.actionCreate_new.setObjectName("actionCreate_new")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuDatabase.addAction(self.actionCreate_new)
        self.menuDatabase.addAction(self.action_Open)
        self.menuDatabase.addAction(self.actionOpen_custom)
        self.menuDatabase.addSeparator()
        self.menuDatabase.addAction(self.actionAdd_annotator)
        self.menuDatabase.addAction(self.actionAdd_cell_class)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.action_Close)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Quit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAnnotation.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SlideRunner"))
        self.MainImage.setText(_translate("MainWindow", "No Slide Open"))
        self.horizontalSlider.setToolTip(_translate("MainWindow", "Zoom Level"))
        self.label_3.setText(_translate("MainWindow", "Overview"))
        self.OverviewLabel.setText(_translate("MainWindow", "TextLabel"))
        self.filenameLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "No database opened."))
        self.threshold_label.setText(_translate("MainWindow", "Threshold"))
        self.opacityLabel.setText(_translate("MainWindow", "Overlay opacity"))
        self.opacitySlider.setToolTip(_translate("MainWindow", "Opacity"))
        self.menuDatabase.setTitle(_translate("MainWindow", "Database"))
        self.menuFile.setTitle(_translate("MainWindow", "Slide"))
        self.menuAnnotation.setTitle(_translate("MainWindow", "Annotation"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.action_Close.setText(_translate("MainWindow", "&Close"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.actionOpen_custom.setText(_translate("MainWindow", "Open custom"))
        self.actionMode.setText(_translate("MainWindow", "Mode"))
        self.actionAdd_annotator.setText(_translate("MainWindow", "Add annotator"))
        self.actionAdd_cell_class.setText(_translate("MainWindow", "Add annotation class"))
        self.actionCreate_new.setText(_translate("MainWindow", "Create new"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

