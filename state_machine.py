import robot_states as states

class StateMachine(object):
    states_list = {'startup', 'navigation', 'pathing', 'mining', 'dumping'}

    def __init__(self, controller):
        self.controller = controller
        self.current_state = states.StartUpState()
        self.previous_state = []

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

    def change_state(self, new_state):
        self.previous_state = self.current_state
        self.current_state = new_state

    def run(self):
        threads = [] #used to keep track of all threads
        startup_state = states.StartUpState()
        startup_state.start()
        threads.append(startup_state)
        startup_state.join() # wait for startup to complete
        threads.remove(startup_state)
        ball_tracking_state = states.BallTrackingState()
        ball_tracking_state.start()
        threads.append(ball_tracking_state)

        while self.controller.autonomy_activated: #TODO: look at actual variable name
            navigation_state = states.NavigationState()
            navigation_state.start()
            threads.append(navigation_state)
            navigation_state.join()
            threads.remove(navigation_state)

            mining_state = states.MiningState()
            mining_state.start()
            threads.append(mining_state)
            mining_state.join()
            threads.remove(mining_state)

            navigation_state = states.NavigationState()
            navigation_state.start()
            threads.append(navigation_state)
            navigation_state.join()
            threads.remove(navigation_state)

            dumping_state = states.DumpingState()
            dumping_state.start()
            threads.append(dumping_state)
            threads.remove(dumping_state)



        for thread in threads: #safely end all threads
            thread.join()



if __name__ == '__main__':
    robot = StateMachine()
    robot.on_event('startup')

