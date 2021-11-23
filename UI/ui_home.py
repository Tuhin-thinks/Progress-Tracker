# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 541)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_4 = QGridLayout(self.page_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_8 = QFrame(self.page_1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_8)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(15)
        self.choice_hours = QComboBox(self.frame_8)
        self.choice_hours.setObjectName(u"choice_hours")

        self.gridLayout_13.addWidget(self.choice_hours, 3, 1, 1, 1)

        self.label_q2 = QLabel(self.frame_8)
        self.label_q2.setObjectName(u"label_q2")
        self.label_q2.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_q2, 3, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.choice_subjects = QComboBox(self.frame_8)
        self.choice_subjects.setObjectName(u"choice_subjects")

        self.gridLayout_13.addWidget(self.choice_subjects, 2, 1, 1, 1)

        self.label_home_page_header = QLabel(self.frame_8)
        self.label_home_page_header.setObjectName(u"label_home_page_header")
        self.label_home_page_header.setStyleSheet(u"QLabel{\n"
"	border: 2px solid black;\n"
"	border-radius: 2px 5px;\n"
"	padding-top: 2px;\n"
"	padding-bottom: 2px;\n"
"}")
        self.label_home_page_header.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_home_page_header, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.pushButton_toggle_mode = QPushButton(self.frame_8)
        self.pushButton_toggle_mode.setObjectName(u"pushButton_toggle_mode")
        self.pushButton_toggle_mode.setMaximumSize(QSize(80, 16777215))
        self.pushButton_toggle_mode.setStyleSheet(u"#pushButton_toggle_mode{\n"
"	color: gray;\n"
"}\n"
"#pushButton_toggle_mode::hover{\n"
"	color: rgb(85, 87, 83);\n"
"}")

        self.gridLayout_13.addWidget(self.pushButton_toggle_mode, 2, 2, 1, 1)

        self.label_q1 = QLabel(self.frame_8)
        self.label_q1.setObjectName(u"label_q1")
        self.label_q1.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_q1, 2, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.pushButton_update = QPushButton(self.frame_9)
        self.pushButton_update.setObjectName(u"pushButton_update")
        self.pushButton_update.setMaximumSize(QSize(80, 16777215))
        self.pushButton_update.setStyleSheet(u"#pushButton_toggle_mode{\n"
"	color: gray;\n"
"}\n"
"#pushButton_toggle_mode::hover{\n"
"	color: rgb(85, 87, 83);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_update)


        self.gridLayout_13.addWidget(self.frame_9, 4, 0, 1, 3)


        self.gridLayout_4.addWidget(self.frame_8, 0, 0, 1, 1, Qt.AlignTop)

        self.graph_outer_frame = QFrame(self.page_1)
        self.graph_outer_frame.setObjectName(u"graph_outer_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_outer_frame.sizePolicy().hasHeightForWidth())
        self.graph_outer_frame.setSizePolicy(sizePolicy)
        self.graph_outer_frame.setFrameShape(QFrame.Box)
        self.graph_outer_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.graph_outer_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_inne_frame_header = QLabel(self.graph_outer_frame)
        self.label_inne_frame_header.setObjectName(u"label_inne_frame_header")
        self.label_inne_frame_header.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_inne_frame_header, 0, 0, 1, 1)

        self.graph_inner_frame = QFrame(self.graph_outer_frame)
        self.graph_inner_frame.setObjectName(u"graph_inner_frame")
        self.graph_inner_frame.setFrameShape(QFrame.StyledPanel)
        self.graph_inner_frame.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.graph_inner_frame, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.graph_outer_frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_clear_records = QPushButton(self.frame_2)
        self.pushButton_clear_records.setObjectName(u"pushButton_clear_records")

        self.gridLayout_5.addWidget(self.pushButton_clear_records, 3, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.pushButton_export_records = QPushButton(self.frame_3)
        self.pushButton_export_records.setObjectName(u"pushButton_export_records")
        self.pushButton_export_records.setMinimumSize(QSize(0, 45))

        self.gridLayout_7.addWidget(self.pushButton_export_records, 2, 0, 1, 1)

        self.pushButton_add_new_db = QPushButton(self.frame_3)
        self.pushButton_add_new_db.setObjectName(u"pushButton_add_new_db")
        self.pushButton_add_new_db.setMinimumSize(QSize(0, 45))

        self.gridLayout_7.addWidget(self.pushButton_add_new_db, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 3, 1)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(5)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_10.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_new_file_name = QLineEdit(self.frame_6)
        self.lineEdit_new_file_name.setObjectName(u"lineEdit_new_file_name")

        self.gridLayout_10.addWidget(self.lineEdit_new_file_name, 0, 1, 1, 1)

        self.pushButton_export_file = QPushButton(self.frame_6)
        self.pushButton_export_file.setObjectName(u"pushButton_export_file")

        self.gridLayout_10.addWidget(self.pushButton_export_file, 1, 1, 1, 1)


        self.gridLayout_11.addWidget(self.frame_6, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_11.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_11.addItem(self.verticalSpacer_6, 2, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_choose_db_path = QPushButton(self.frame_5)
        self.pushButton_choose_db_path.setObjectName(u"pushButton_choose_db_path")

        self.gridLayout_9.addWidget(self.pushButton_choose_db_path, 0, 1, 1, 1)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.pushButton_confirm_db_path = QPushButton(self.frame_7)
        self.pushButton_confirm_db_path.setObjectName(u"pushButton_confirm_db_path")

        self.gridLayout_12.addWidget(self.pushButton_confirm_db_path, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.label_path_text = QLabel(self.frame_7)
        self.label_path_text.setObjectName(u"label_path_text")
        self.label_path_text.setMaximumSize(QSize(16777215, 50))
        self.label_path_text.setWordWrap(True)

        self.gridLayout_12.addWidget(self.label_path_text, 0, 0, 1, 3)


        self.gridLayout_9.addWidget(self.frame_7, 1, 0, 1, 2)


        self.gridLayout_8.addWidget(self.frame_5, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 0, 1, 4, 1)


        self.gridLayout_6.addWidget(self.frame_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_preferences = QWidget()
        self.page_preferences.setObjectName(u"page_preferences")
        self.label_3 = QLabel(self.page_preferences)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 160, 371, 151))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_preferences)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.frame_button_panel = QFrame(self.centralwidget)
        self.frame_button_panel.setObjectName(u"frame_button_panel")
        self.frame_button_panel.setFrameShape(QFrame.Panel)
        self.frame_button_panel.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.frame_button_panel)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(15)
        self.pushButton_nav_pref = QPushButton(self.frame_button_panel)
        self.pushButton_nav_pref.setObjectName(u"pushButton_nav_pref")
        self.pushButton_nav_pref.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.pushButton_nav_pref, 4, 0, 1, 1)

        self.pushButton_nav_db_setting = QPushButton(self.frame_button_panel)
        self.pushButton_nav_db_setting.setObjectName(u"pushButton_nav_db_setting")
        self.pushButton_nav_db_setting.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.pushButton_nav_db_setting, 3, 0, 1, 1)

        self.pushButton_nav_home = QPushButton(self.frame_button_panel)
        self.pushButton_nav_home.setObjectName(u"pushButton_nav_home")
        self.pushButton_nav_home.setMinimumSize(QSize(0, 45))

        self.gridLayout_3.addWidget(self.pushButton_nav_home, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_button_panel, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 838, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Progress Tracker", None))
        self.label_q2.setText(QCoreApplication.translate("MainWindow", u"question 2", None))
        self.label_home_page_header.setText(QCoreApplication.translate("MainWindow", u"Daily Update", None))
        self.pushButton_toggle_mode.setText(QCoreApplication.translate("MainWindow", u"hrs/days", None))
        self.label_q1.setText(QCoreApplication.translate("MainWindow", u"question 1", None))
#if QT_CONFIG(tooltip)
        self.pushButton_update.setToolTip(QCoreApplication.translate("MainWindow", u"update data to database", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_update.setText(QCoreApplication.translate("MainWindow", u"update", None))
        self.label_inne_frame_header.setText(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.pushButton_clear_records.setText(QCoreApplication.translate("MainWindow", u"clear records", None))
        self.pushButton_export_records.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.pushButton_add_new_db.setText(QCoreApplication.translate("MainWindow", u"Add New DB File", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter new file path", None))
        self.pushButton_export_file.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose path", None))
        self.pushButton_choose_db_path.setText(QCoreApplication.translate("MainWindow", u"Choose", None))
        self.pushButton_confirm_db_path.setText(QCoreApplication.translate("MainWindow", u"confirm", None))
        self.label_path_text.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">This page will be updated very soon!!!</span></p></body></html>", None))
        self.pushButton_nav_pref.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.pushButton_nav_db_setting.setText(QCoreApplication.translate("MainWindow", u"DB-Settings", None))
        self.pushButton_nav_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
    # retranslateUi

