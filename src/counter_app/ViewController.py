from contextlib import ExitStack
from math import radians
from typing import TYPE_CHECKING

from PySide6.QtCore import QSignalBlocker

from counter_app.view_chanel_data import ViewerState, Vec3, Quat, set_view_request

if TYPE_CHECKING:
    from counter_app.main import MainWindow

class ViewController:
    def __init__(self, parent: "MainWindow"):
        self.parent = parent

        self.tx = parent.tx_box
        self.ty = parent.ty_box
        self.tz = parent.tz_box
        self.zoom = parent.zoom_box
        self.qx = parent.qx_box
        self.qy = parent.qy_box
        self.qz = parent.qz_box
        self.qw = parent.qw_box

        self.tx.valueChanged.connect(self.set_view)
        self.ty.valueChanged.connect(self.set_view)
        self.tz.valueChanged.connect(self.set_view)
        self.zoom.valueChanged.connect(self.set_view)
        self.qx.valueChanged.connect(self.set_view)
        self.qy.valueChanged.connect(self.set_view)
        self.qz.valueChanged.connect(self.set_view)
        self.qw.valueChanged.connect(self.set_view)

    def show_view(self, viewer_state: ViewerState):
        with ExitStack() as stack:
            for w in (self.tx, self.ty, self.tz, self.zoom, self.qx, self.qy, self.qz, self.qw):
                stack.enter_context(QSignalBlocker(w))

            self.tx.setValue(viewer_state.t.x)
            self.ty.setValue(viewer_state.t.y)
            self.tz.setValue(viewer_state.t.z)
            self.zoom.setValue(viewer_state.posZ)
            self.qx.setValue(viewer_state.q.x)
            self.qy.setValue(viewer_state.q.y)
            self.qz.setValue(viewer_state.q.z)
            self.qw.setValue(viewer_state.q.w)

    def set_view(self):
        viewer_state = ViewerState(
            t=Vec3(x = self.tx.value(),
                   y = self.ty.value(),
                   z = self.tz.value()),
            posZ=self.zoom.value(),
            q=Quat(x = radians(self.qx.value()),
                   y = radians(self.qy.value()),
                   z = radians(self.qz.value()),
                   w = self.qw.value())
        )
        set_view_request(viewer_state)
