from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import cartopy.crs as ccrs
import matplotlib

matplotlib.use("Qt5Agg")


class MapWidget(FigureCanvas):
    def __init__(self):
        self.figure = Figure()
        FigureCanvas.__init__(self, self.figure)
        self.ax = self.figure.add_subplot(frameon=False, projection=ccrs.PlateCarree())
        self.draw_map()

    def draw_map(self):
        self.ax.stock_img()
        self.figure.tight_layout()

    def draw_point(self, lon, lat, text):
        self.ax.scatter(lon, lat, s=3, color='red', transform=ccrs.Geodetic())
        self.ax.text(lon + 2, lat - 1, text, horizontalalignment='left', transform=ccrs.Geodetic())
        self.draw()

    def clear(self):
        self.ax.cla()
        self.draw_map()
        self.draw()
