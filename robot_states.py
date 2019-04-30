import state_class as State #used by all states
import AStar as alg #PathingState
import connection
import motor_lib as motorDriver

class StartUpState(State):
    def __init__(self):
        #start client connection
        connection()
        #turn on motors/servos
        motorDriver()
        #find balls
        self.set_current_state(PathingState)

    def on_event(self, event):
        if event == 'pathing':
            return PathingState()
        return self

class NavigationState(State):
    global return_trip
    def __init__(self, path):
        if return_trip == True:
            #navigate to dump bin
            #switch state to dumping

        self.path_to_follow = path
        print(self.path_to_follow)


    def on_event(self, event):
        if event == 'next':
            return PathingState()
        return self

class PathingState(State):
    def __init__(self, width=20, height=20, obstacle_map=[(3,3)], start=(1,1), end=(5,5), behind=(0,0)):
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


class MiningState(State):
    def __init__(self):
        #if at dig site:
            #lower arms and begin digging
            #once digging, begin moving conveyor belt
            #once dig time has passed (conveyor is at its end):
                #check for motor stalls
                    #if yes, lift arms and check for motor stall
            #raise arms and turn off wheel motor
            #return_trip = True
            #change state to navigation
        pass


class DumpingState(State):
    def __init__(self):
        #check if we are at the dump bin:
            #if return_trip = True:
                #move to line up conveyor belt with dump bin

        pass
