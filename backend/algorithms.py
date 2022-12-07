import osmnx as ox
import networkx as nx
import numpy as np
import astar as ast
import shortestPath as sh

from map_lib import Map

class algorithms:
    def __init__(self, startLatitude, startLongitude, endLatitude, endLongitude, elevationType, distanceLimit) -> None:
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

    def run(self):
        algorithmValues = {}
        shortestPathAlgorithm = sh.shortestPath(self.graph, self.src, self.dest)
        algorithmValues['shortest_path'] = shortestPathAlgorithm.run()
        shortestDistance = algorithmValues['shortest_path']['distance']

        astarAlgorithm = ast.astar(self.graph, self.src, self.dest, self.limit, self.isMaximum, shortestDistance)
        algorithmValues['a_star'] = astarAlgorithm.run()
        return algorithmValues

# if __name__=="__main__":
#     src = tuple((42.35081772765568, -72.52727125397264))
#     dest = tuple((42.386760374718236, -72.52481790025085))
#     alg = algorithms(src[0], src[1], dest[0], dest[1], 'maximum', 125)
#     values = alg.run()
#     print(values)

