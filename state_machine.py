import robot_states as states

class StateMachine(object):
    states_list = {'startup', 'navigation', 'pathing', 'mining', 'dumping'}

    def __init__(self):
        self.current_state = states.StartUpState()
        self.previous_state = None

    def on_event(self, event):
        if event == 'startup':
            self.current_state = states.StartUpState()
            return self.current_state
        elif event == 'navigation':
            self.current_state = states.NavigationState()
            return self.current_state
        elif event == 'pathing':
            self.current_state = states.PathingState()
            return self.current_state
        elif event == 'mining':
            self.current_state = states.MiningState()
            return self.current_state
        elif event == 'dumping':
            self.current_state = states.DumpingState()
            return self.current_state
        return self

    def check_state(self, new_state):
        #if next state is a valid transition from curr:
            #return True
        return False

    def change_state(self, new_state):
        self.previous_state = self.current_state
        self.current_state = new_state

if __name__ == '__main__':
    robot = StateMachine()
    robot.on_event('startup')

