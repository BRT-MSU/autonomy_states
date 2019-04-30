class State:
    def __init__(self):
        self.current_state = None
        self.next_state = None
        self.previous_state = None
        self.running = False

    def set_current_state(self, state):
        self.current_state = state

    def set_next_state(self, state, state_check):
        if state_check:
            self.next_state = state
        else:
            print("cannot switch from " + self.current_state
                  + " to " + state)

    def set_previous_state(self, state):
        self.previous_state = state

    def get_current_state(self):
        return self.current_state

    def get_next_state(self):
        return self.next_state

    def get_previous_state(self):
        return self.previous_state

    def run_state(self):
        self.running = True
        while self.running:
            print("ur a bitch")