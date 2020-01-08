from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class BlackHole(object):
    def __init__(self, **kw):
        super(BlackHole, self).__init__()

class DummyScreen(Screen, BlackHole):
    def __init__(self, **kwargs):
        super(DummyScreen, self).__init__(**kwargs)
