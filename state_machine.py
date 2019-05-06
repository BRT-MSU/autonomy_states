import robot_states as states

class StateMachine(object):

    def __init__(self, controller):
        self.controller = controller
        self.current_state = None
        self.previous_states = []
        self.threads = [] #used to keep track of all threads

    def change_state(self, new_state):
        self.previous_state = self.current_state
        self.current_state = new_state

    def run_state(state):
        self.threads.append(state)
        state.start()
        state.join()
        self.threads.remove(state)

    def run(self):
        startup_state = states.StartUpState()
        startup_state.start()
        threads.append(startup_state)
        startup_state.join() # wait for startup to complete
        threads.remove(startup_state)
        
        ball_tracking_state = states.BallTrackingState() # run tracking constantly
        ball_tracking_state.start()
        threads.append(ball_tracking_state)

        first_trip = True

        while self.controller.isAutonomyActivated:
            self.run_state(states.NavigationState(self.controller), to_dig=True, first_trip)
            first_trip = False
            self.run_state(states.MiningState(self.controller))
            self.run_state(states.NavigationState(self.controller)) 
            self.run_state(states.DumpingState(self.controller))
         

        for thread in self.threads: #safely end all threads
            thread.join()

if __name__ == '__main__':
    robot = StateMachine(None)

