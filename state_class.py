class State (object):
    def __init__(self):
        print("__init__ State")

    def on_event(self, event):
        print("on_event State: " + event)