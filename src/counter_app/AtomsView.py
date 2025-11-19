from PySide6.QtCore import QObject, Signal, Slot, QUrl
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineScript
from PySide6.QtWebEngineWidgets import QWebEngineView

import web_view_gen.web_rc
from counter_app.view_chanel_data import ViewerState, from_dict, send_view_changed, set_view_request, \
    subscribe_set_view_request

WEB_CHANNEL_SCRIPT = QUrl("qrc:/qtwebchannel/qwebchannel.js")
WEB_VIEW_LINK = QUrl("qrc:/web_view/index.html")


class Bridge(QObject):
    # Web channel signals
    addXyzModel = Signal(str)
    addCifModel = Signal(str)
    resetView = Signal()
    setView = Signal(dict)

    @Slot(str)
    def logFromJs(self, msg):
        print("[JS]", msg)

    @Slot("QVariant")
    def viewChanged(self, data):
        view_state = from_dict(ViewerState, data)
        send_view_changed(viewer_state=view_state)

    @Slot("QVariant")
    def receive(self, data):
        print("Python received:", data, type(data))

    # Request to web chanel handlers
    def set_view(self, viewer_state: ViewerState):
        self.setView.emit(viewer_state.to_dict())


class DebugPage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, source):
        print(f"[JS:{source}:{line}] {msg}")


class AtomsView:
    def __init__(self, atomsViewArea: QWebEngineView):
        self._view_changed_handler = None
        assert web_view_gen.web_rc is not None

        self.atomsViewArea = atomsViewArea

        self.view_changed = Signal(ViewerState)
        self._bridge = Bridge()

        page = DebugPage(atomsViewArea.page().parent())
        self.atomsViewArea.setPage(page)

        channel = QWebChannel(atomsViewArea.page())
        channel.registerObject("bridge", self._bridge)
        self.atomsViewArea.page().setWebChannel(channel)

        self._inject_web_chanel_script()

        self.atomsViewArea.load(WEB_VIEW_LINK)
        self.atomsViewArea.loadFinished.connect(lambda state: print("Loaded web atoms view:", state))

        self._subscribe_events()

    def reset_view(self):
        self._bridge.resetView.emit()

    def _subscribe_events(self):
        subscribe_set_view_request(self._bridge.set_view)

    def _inject_web_chanel_script(self):
        script = QWebEngineScript()
        script.setName("qwebchannel")
        script.setSourceUrl(WEB_CHANNEL_SCRIPT)
        script.setInjectionPoint(QWebEngineScript.InjectionPoint.DocumentCreation)
        script.setWorldId(QWebEngineScript.ScriptWorldId.MainWorld)
        self.atomsViewArea.page().scripts().insert(script)
