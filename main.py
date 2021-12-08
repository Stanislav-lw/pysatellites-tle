import sys

from datetime import datetime

from PySide2 import QtWidgets, QtCore

from ui_mainwidget import Ui_MainWidget
from mapwidget import MapWidget

from pyorbital.orbital import Orbital
from spacetrack import SpaceTrackClient


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)
        self.ui.idsLineEdit.setPlaceholderText('id or id_1, id_2, ..., id_n')
        self.mwt = MapWidget()
        self.ui.mwtLayout.addWidget(self.mwt, 0, 0)
        self.ui.updatePushButton.clicked.connect(self.update_satellite_list)
        self.ui.savePushButton.clicked.connect(self.save_satellite_tle)
        setting = QtCore.QSettings('sat_down.ini', QtCore.QSettings.IniFormat)
        self.ui.idsLineEdit.setText(setting.value('ids'))
        self.ui.usernameLineEdit.setText(setting.value('username'))
        self.ui.passwordLineEdit.setText(setting.value('password'))
        self.satellite_tles = {}

    def closeEvent(self, e):
        setting = QtCore.QSettings('sat_down.ini', QtCore.QSettings.IniFormat)
        setting.setValue('ids', self.ui.idsLineEdit.text())
        setting.setValue('username', self.ui.usernameLineEdit.text())
        setting.setValue('password', self.ui.passwordLineEdit.text())
        e.accept()

    def update_satellite_list(self):
        self.mwt.clear()
        self.satellite_tles.clear()
        self.ui.noradListWidget.clear()
        if self.ui.idsLineEdit.text():
            st = SpaceTrackClient(identity=self.ui.usernameLineEdit.text(),
                                  password=self.ui.passwordLineEdit.text())
            id_list = self.ui.idsLineEdit.text().split(',')
            current_datetime = datetime.utcnow()
            for sat_id in id_list:
                tle = st.tle_latest(norad_cat_id=sat_id, orderby='epoch desc', limit=1, format='tle')
                if tle:
                    try:
                        self.ui.noradListWidget.addItem(sat_id.strip())
                        self.satellite_tles[sat_id.strip()] = tle
                        orb = Orbital('S', line1=tle[0:69], line2=tle[70:139])
                        lon, lat, alt = orb.get_lonlatalt(current_datetime)
                        self.mwt.draw_point(lon, lat, sat_id.strip())
                    except NotImplementedError as ex:
                        error_dialog = QtWidgets.QErrorMessage(self)
                        error_dialog.showMessage('Norad id: {0} - {1}!'.format(sat_id, ex))

    def save_satellite_tle(self):
        selected_items = self.ui.noradListWidget.selectedItems()
        for item in selected_items:
            if item.text() in self.satellite_tles:
                file = open(item.text() + '.tle', 'w')
                file.write(self.satellite_tles.get(item.text()))
                file.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MainWidget()
    widget.show()

    sys.exit(app.exec_())
