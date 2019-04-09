from . import state_class as State #used by all states
from . import myAlgorithm as alg #PathingState


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

class NavigationState(State):
    def __init__(self, path):
        self.path_to_follow = path
        print(self.path_to_follow)

    def on_event(self, event):
        if event == "next":
            return PathingState()
        return self