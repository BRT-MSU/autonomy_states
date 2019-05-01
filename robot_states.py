import state_class as State #used by all states
import AStar as alg #PathingState
import motor_lib as motorDriver

class BallTrackingState(State):
    def __init__(self, controller):
        super().init(controller)
        self.values_to_return
        pass

    def run(self):
        pass

    def join(self):
        super().join()
        return self.values_to_return

class StartUpState(State):
    def __init__(self, controller):
        super().init(controller)
        #extend camera servos
        #locate balls
            #determine orientation - arena A or B
        #raise digging wheel arms
        #initialize arduino
        #face front of robot away from mining area
        pass

    def on_event(self, event):
        if event == 'pathing':
            return PathingState()
        return self

    def run(self):
        pass


class NavigationState(State):
    global return_trip
    global first_Trip

    def __init__(self, controller):
        super().init(controller)
        if first_Trip == True:
            pass
        else:
            self.path_to_follow = path
            print(self.path_to_follow)

    def on_event(self, event):
        if event == 'next':
            return PathingState()
        return self

    def run(self):
        pass


class PathingState(State):
    def __init__(self, controller, width=20, height=20, obstacle_map=[(3,3)], start=(1,1), end=(5,5), behind=(0,0)):
        super().init(controller)
        """
        width and height in matrix size (width(cm) / spacing(cm))
        obstacle_map is location of obstacles in matrix coordinates
        behind is matrix location behind robot
        """
        self.graph = alg.AStarGraph(obstacles=obstacle_map,width=width,height=height)
        self.result, self.cost = alg.AStarSearch(navPoints=[start,end], behind=behind, graph=self.graph)
        print("init pathingstate")

    def on_event(self, event):
        return NavigationState(self.result) #feed the resulting path to the navigation state

    def run(self):
        pass

class MiningState(State):
    def __init__(self, controller):
        super().init(controller)

    def run(self):
        state_active = True
        while state_active:
            pass
            #if at dig site:
                #lower arms and begin digging
                #once digging, begin moving conveyor belt
                #once dig time has passed (conveyor is at its end):
                    #check for motor stalls
                        #if yes, lift arms and check for motor stall
                #raise arms and turn off wheel motor
                #return_trip = True
                #change state to navigation



class DumpingState(State):
    def __init__(self, controller):
        super().init(controller)

    def run(self):
        state_active = True
        while state_active:
            pass
            # if return_trip = True:
            # check if we are at the dump bin
            # move to line up conveyor belt with dump bin
            # move conveyor belt to empty it
            # once conveyor belt is empty:
            # return_trip = False
            # change state back to navigation

