from dataclasses import is_dataclass, fields, dataclass, asdict
from typing import Callable

from blinker import Signal


def from_dict(cls, data):
    kwargs = {}
    for f in fields(cls):
        if is_dataclass(f.type):
            kwargs[f.name] = from_dict(f.type, data[f.name])
        else:
            kwargs[f.name] = data[f.name]
    return cls(**kwargs)

@dataclass
class Vec3:
    x: float
    y: float
    z: float

@dataclass
class Quat:
    x: float
    y: float
    z: float
    w: float

@dataclass
class ViewerState:
    posZ: float
    q: Quat
    t: Vec3

    def to_dict(self):
        return asdict(self)


_view_changed_event = Signal()
_set_view_request = Signal()

def subscribe_view_changed(handler: Callable[[ViewerState], None]):
    def _adapter(sender, viewer_state: ViewerState, **kwargs):
        handler(viewer_state)  # drop sender, **kwargs

    _view_changed_event.connect(_adapter, weak=False)

def send_view_changed(viewer_state: ViewerState):
    _view_changed_event.send(viewer_state=viewer_state)

def subscribe_set_view_request(handler: Callable[[ViewerState], None]):
    def _adapter(sender, viewer_state: ViewerState, **kwargs):
        handler(viewer_state)

    _set_view_request.connect(_adapter, weak=False)

def set_view_request(viewer_state: ViewerState):
    _set_view_request.send(viewer_state=viewer_state)
