import abc

class AutonomyState:

    def __init__(self, autonomy):
        self.autonomy = autonomy
        self.current_state = None

    def next_state(self):
        return self.current_state.next_state(self)

    def set_state(self, new_state):
        self.current_state = new_state

class State(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def next_state(self):
        pass


