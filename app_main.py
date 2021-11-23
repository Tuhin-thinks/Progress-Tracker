import sys
import pyqtgraph as py_graph
from PySide2.QtWidgets import QMainWindow, QApplication, QComboBox, QGridLayout
import numpy as np

from UI import ui_home
from DB import manage_db

fav_colors = (
    '#196ab4', '#f1c232', '#f44336', '#8fce00'
)


class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.curr_time_mode = 'hours'
        self.plot_items = []
        self.ui = ui_home.Ui_MainWindow()
        self.ui.setupUi(self)

        # fetch ui_data from database (call schema using get_ui_data())
        ui_data = manage_db.get_ui_data()
        question_1 = ui_data['question 1']
        question_2 = ui_data['question 2']
        self.ui.label_q1.setText(question_1)
        self.ui.label_q2.setText(question_2)

        # update days passed
        manage_db.update_days_passed()

        subject_names = manage_db.get_subject_names()
        self.ui.choice_subjects.addItems(subject_names)

        # signals and slots
        self.ui.pushButton_toggle_mode.clicked.connect(self.toggle_days_hrs_mode)
        self.ui.pushButton_update.clicked.connect(self.update_to_db)

        # update hrs/days data in time selection mode
        self.toggle_days_hrs_mode()

        # create graph widget
        self.graph_widget: 'py_graph.PlotWidget' = py_graph.PlotWidget()
        self.graph_widget.showGrid(x=True, y=True, alpha=1.0)
        self.graph_widget.setTitle("Progress Report")
        self.graph_widget.setLabel('bottom', 'Hour')
        self.graph_widget.setBackground("#FDE3CF")
        self.gridLayout_3 = QGridLayout(self.ui.graph_inner_frame)
        self.gridLayout_3.addWidget(self.graph_widget)

    def update_to_db(self):
        if self.curr_time_mode == 'days':
            days = int(self.ui.choice_hours.currentText())
            hrs = None
        else:
            hrs = float(self.ui.choice_hours.currentText())
            days = None
        manage_db.update_subject_data(self.ui.choice_subjects.currentText(), hrs, days)
        self.ui.statusbar.showMessage("Updated successfully", 5000)

    def toggle_days_hrs_mode(self):
        for index in range(self.ui.choice_hours.count() - 1, -1, -1):
            self.ui.choice_hours.removeItem(index)
        if self.curr_time_mode == 'days':
            self.ui.choice_hours.addItems((str(i + 0.5) for i in range(1, 13)))
            self.curr_time_mode = 'hours'
        else:
            self.ui.choice_hours.addItems(('1', '2'))  # for days
            self.curr_time_mode = 'days'

    # TODO: complete this function
    def plot_data(self, sub_name: str):
        x = np.linspace(0, self.days_passed)
        y = manage_db.get_subject_data(sub_name)

        self.graph_widget.plot([x], [y], symbol='o')

    # TODO: update hours studied for each day for each subject on subject log
    #       and use this to generate plot.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())
