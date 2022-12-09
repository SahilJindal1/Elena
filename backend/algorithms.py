import osmnx as ox
import networkx as nx
import numpy as np
import astar as ast
import shortestPath as sh
import dijkstra as dj

from map_lib import Map

"""
This class calls all the three algorithms to get their path, distance and elevation values.
"""
class algorithms:
    """
    This function initializes the algorithms class with the given parameters.

    @param startLatitude A decimal representing source location latitude
    @param startLongitude A decimal representing source location longitude
    @param endLatitude A decimal representing destination location latitude
    @param endLongitude A decimal representing destination location longitude
    @param elevationType A string representing the elevation type
    @param distanceLimit A number representing the maximum distance limit percentage

    @exception If the given parameters are of None type
    @exception If the given parameters are empty strings
    """
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

    """
    This function runs all the algorithms.

    @exception If the calculates source and destionation nodes are not valid

    @return A dictionary of values having path, distance and elevation gain for shortest-path, dijkstra and a*
    """
    def run(self):
        if (self.srcNode and self.destNode) is None:
            raise Exception("Not Valid Nodes")

        algorithmValues = {}
        shortestPathAlgorithm = sh.shortestPath(self.graph, self.src, self.dest)
        algorithmValues['shortest_path'] = shortestPathAlgorithm.run()
        shortestDistance = algorithmValues['shortest_path']['distance']

        dijkstraAlgorithm = dj.dijkstra(self.graph, self.src, self.dest, self.limit, self.isMaximum, shortestDistance)
        algorithmValues['dijkstra'] = dijkstraAlgorithm.run()

        astarAlgorithm = ast.astar(self.graph, self.src, self.dest, self.limit, self.isMaximum, shortestDistance)
        algorithmValues['a_star'] = astarAlgorithm.run()

        if algorithmValues['a_star'] is None:
            if algorithmValues['dijkstra'] is not None:
                algorithmValues['a_star'] = algorithmValues['dijkstra']
            else:
                algorithmValues['a_star'] = algorithmValues['shortest_path']

        if algorithmValues['dijkstra'] is None:
            if algorithmValues['a_star'] is not None:
                algorithmValues['dijkstra'] = algorithmValues['a_star']
            else:
                algorithmValues['dijkstra'] = algorithmValues['shortest_path']

        return algorithmValues

# if __name__=="__main__":
#     src = tuple((42.3710233, -72.5175895))
#     dest = tuple((42.351556, -72.527381))
#     alg = algorithms(src[0], src[1], dest[0], dest[1], 'minimum', 125)
#     values = alg.run()

#     print(len(values['shortest_path']['path']), values['shortest_path']['distance'], values['shortest_path']['elevation_gain'])
#     print(len(values['dijkstra']['path']), values['dijkstra']['distance'], values['dijkstra']['elevation_gain'])
#     print(len(values['a_star']['path']), values['a_star']['distance'], values['a_star']['elevation_gain'])

