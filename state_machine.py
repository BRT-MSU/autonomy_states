import robot_states as states

class StateMachine(object):
    states_list = {'startup', 'navigation', 'pathing', 'mining', 'dumping'}

    def __init__(self, controller):
        self.controller = controller
        self.current_state = states.StartUpState()
        self.previous_state = []

    def on_event(self, event):
        return self

    def change_state(self, new_state):
        self.previous_state = self.current_state
        self.current_state = new_state

    def run(self):
        states_list = ['nav', 'mine', 'dump']
        threads = [] #used to keep track of all threads
        startup_state = states.StartUpState()
        startup_state.start()
        threads.append(startup_state)
        startup_state.join() # wait for startup to complete
        threads.remove(startup_state)
        ball_tracking_state = states.BallTrackingState()
        ball_tracking_state.start()
        threads.append(ball_tracking_state)

        while self.controller.isAutonomyActivated:
            # navigation_state = states.NavigationState()
            # navigation_state.start()
            # threads.append(navigation_state)
            # navigation_state.join()
            # threads.remove(navigation_state)
            #
            # mining_state = states.MiningState()
            # mining_state.start()
            # threads.append(mining_state)
            # mining_state.join()
            # threads.remove(mining_state)
            #
            # navigation_state = states.NavigationState()
            # navigation_state.start()
            # threads.append(navigation_state)
            # navigation_state.join()
            # threads.remove(navigation_state)
            #
            # dumping_state = states.DumpingState()
            # dumping_state.start()
            # threads.append(dumping_state)
            # threads.remove(dumping_state)

            for i, state in enumerate(states_list):
                if states_list[i] == 'nav':
                    state = states.NavigationState()
                elif states_list[i] == 'mine':
                    state = states.MiningState()
                elif states_list[i] == 'dump':
                    state = states.DumpingState()

                state.start()
                threads.append(state)
                if states_list[i] == 'dump':
                    pass
                else:
                    state.join()
                threads.remove(state)



        for thread in threads: #safely end all threads
            thread.join()



if __name__ == '__main__':
    robot = StateMachine()
    robot.on_event('startup')

