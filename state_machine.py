from . import robot_states as states

class StateMachine (object):
    def __init__(self):
        self.obstacle_map = [()]
        self.current_state = states.PathingState()

    def on_event(self, event):
        self.current_state = self.current_state.on_event(event)

if __name__ == '__main__':
    robot = StateMachine()
    robot.on_event("next")