from PySide6.QtCore import QObject, Signal, Slot, QUrl
from PySide6.QtWebChannel import QWebChannel
import web_view_gen.web_rc


class Bridge(QObject):
    modelUpdated = Signal(str)
    resetViewRequested = Signal()
    backgroundUpdated = Signal(str)

    @Slot(str)
    def logFromJs(self, msg):
        print("[JS]", msg)

class AtomsView:
    def __init__(self, atomsViewArea: "WebEngineWidget"):
        self.atomsViewArea = atomsViewArea
        self._bridge = Bridge()
        channel = QWebChannel(atomsViewArea.page())
        channel.registerObject("bridge", self._bridge)
        atomsViewArea.page().setWebChannel(channel)

        link = QUrl("qrc:/web_view/index.html").toString()
        print(f"Link to web view: {link}")
        self.atomsViewArea.load(
            QUrl("qrc:/web_view/index.html")
        )
