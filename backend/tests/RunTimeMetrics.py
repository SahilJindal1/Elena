import time
import sys
import os
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
import osmnx as ox
from map_lib import Map
import astar as ast
import shortestPath as sh
import dijkstra as dj
from collections import defaultdict
import matplotlib.pyplot as plt

class RunTime:

    def __init__(self, startLatitude, startLongitude, endLatitude, endLongitude, elevationType, distanceLimit) -> None:
        
        if (startLatitude and startLongitude and endLatitude and endLongitude and elevationType and distanceLimit) is None:
            raise Exception("None type Parameters in Algorithms")
        elif (startLatitude and startLongitude and endLatitude and endLongitude and elevationType and distanceLimit) == '':
            raise Exception("Empty Parameters in Algorithms")
        else:
            amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
            self.map = Map()
            self.graph = self.map.generate_map(amherstCoordinates, 15000)
            self.src = tuple((startLatitude, startLongitude))
            self.dest = tuple((endLatitude, endLongitude))
            self.limit = distanceLimit / 100
            self.isMaximum = (elevationType == 'maximum')
            # X = long, Y = lat
            self.srcNode, self.srcDistance = ox.distance.nearest_nodes(self.graph, X = self.src[1], Y=self.src[0], return_dist = True)
            self.destNode, self.destDistance = ox.distance.nearest_nodes(self.graph, X = self.dest[1], Y=self.dest[0], return_dist = True)
            print(self.graph.nodes[self.srcNode], self.graph.nodes[self.destNode])

    def timeTaken(self,timeDict,distList):


        if (self.srcNode and self.destNode) is None:
            raise Exception("Not Valid Nodes")

        start = time.time()
        shortestPathAlgorithm = sh.shortestPath(self.graph, self.src, self.dest)
        min_path = shortestPathAlgorithm.run()
        end = time.time()

        shortestDistance = min_path['distance']
        print("Shortest Path Algorithm took", (end-start)* 10**3,"ms")
        timeDict["shortest"].append((end-start) * 10**3)

        distList.append(shortestDistance)

        start = time.time()
        dijkstraAlgorithm = dj.dijkstra(self.graph, self.src, self.dest, self.limit, self.isMaximum, shortestDistance)
        dijkstraAlgorithm.run()
        end = time.time()

        print("Dijkstra Algorithm took", (end-start)* 10**3,"ms")
        timeDict["dijkstra"].append((end-start) * 10**3)


        start = time.time()
        astarAlgorithm = ast.astar(self.graph, self.src, self.dest, self.limit, self.isMaximum, shortestDistance)
        astarAlgorithm.run()
        end = time.time()

        print("A-star Algorithm took", (end-start)* 10**3,"ms")
        timeDict["astar"].append((end-start) * 10**3)


        return timeDict,distList

        
        
if __name__ == "__main__":
    timeDict = defaultdict(list)
    distList = []
    startCoord = [[42.38991592520288,-72.52825001376017],[42.39516055978262, -72.53122330162097],[42.371124392650906, -72.51695988627795],[42.36707244865424,-72.51187238346712],[42.403842502702375, -72.52771191696442],[42.38949984067455, -72.53351077463662]]
    endCoord  = [[42.390461766901325, -72.51921324394927],[42.38991592520288,-72.52825001376017],[42.349730603336376, -72.52837808812986],[42.373217640705526,-72.53175871511382],[42.34703289024968, -72.5275742867851],[42.3733365327973, -72.53173725744197]]

    if(len(startCoord)!=len(endCoord)):
        raise Exception("Start and destination coordinate lenght do not match")
    
    # To get the avaerage time run this loop for 10 iterations
    for i in range(len(startCoord)):
        startLat = startCoord[i][0]
        startLong = startCoord[i][1]

        endLat = endCoord[i][0]
        endLong = endCoord[i][1]

        runTimeObj = RunTime(startLat,startLong,endLat,endLong,"maximum",150)
        timeDict, distList = runTimeObj.timeTaken(timeDict,distList)

    print("Average Time to run the Shortest Path Algorithm ",(sum(timeDict["shortest"])/(len(timeDict["shortest"]))))
    print("Average Time to run the Dijkstra Algorithm ",(sum(timeDict["dijkstra"])/(len(timeDict["dijkstra"]))))
    print("Average Time to run the A-Star Algorithm ",(sum(timeDict["astar"])/(len(timeDict["astar"]))))

    origDistList = distList.copy()
    distList.sort()
    
    keydict = dict(zip(timeDict["shortest"], distList))
    timeDict["shortest"].sort(key=keydict.get)

    plt.plot(distList,timeDict["shortest"],color = 'blue')
    plt.ylabel("Run Time in ms")
    plt.xlabel("Distance between start and end coordinates")
    plt.show()

    plt.plot(distList,timeDict["dijkstra"],color = 'black')
    plt.ylabel("Run Time in ms")
    plt.xlabel("Distance between start and end coordinates")
    plt.show()

    plt.plot(distList,timeDict["astar"],color = 'green')
    plt.ylabel("Run Time in ms")
    plt.xlabel("Distance between start and end coordinates")
    plt.show()
    