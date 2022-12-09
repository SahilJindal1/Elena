import numpy as np
import math
# import osmnx as ox
# from map_lib import Map

"""
This class contains the utility functions common to executing the algorithms.
"""
class algorithmUtility:
    """
    This function calculates the direct distance between the given source and destination coordinates.

    @param src A tuple representing the source location latitude and longitude
    @param dest A tuple representing the destination location latitude and longitude

    @exception If the given parameters are of None type
    @exception If the given parameters are empty strings

    @return A number representing the distance value between the coordinates
    """
    def calculateDistanceUsingCoords(self, src, dest):
        # R = 6371 kms
        # distance = 2R⋅sin⁻¹(√[sin²((θ₂ - θ₁)/2) + cosθ₁⋅cosθ₂⋅sin²((φ₂ - φ₁)/2)])
        # theta = lat, phi = long

        if (src and dest) is None:
            raise Exception("None type values provided in calculateDistanceUsingCoords function")
        elif (src and dest) == '':
            raise Exception("Empty values provided in calculateDistanceUsingCoords function")

        R = 6371000
        srcLat, srcLong = np.radians(src[0]), np.radians(src[1])
        destLat, destLong = np.radians(dest[0]), np.radians(dest[1])

        val1 = math.pow(np.sin((destLat - srcLat)/2), 2)
        val2 = np.cos(srcLat)*np.cos(destLat)
        val3 = math.pow(np.sin((destLong - srcLong)/2), 2)
        val = math.sqrt(val1 + val2 * val3)

        dist = 2 * R * np.arcsin(val)
        return dist

    """
    This function backtracks the path from current node using the parent dictionary.

    @param currNode A number repsenting a valid node from graph
    @param parent A dictionary containing parents for nodes in the graph

    @exception If the given parameters are of None type
    @exception If the given parameters are empty strings

    @return An array containing the path to currNode
    """
    def backtrack(self, currNode, parent):
        if currNode and parent is None:
            raise Exception("None type parameters in backtrack")
        elif (currNode and parent) == '':
            raise Exception("Empty parameters in backtrack")

        path = [currNode]

        while currNode in parent:
            currNode = parent[currNode]
            path.append(currNode)

        return path[::-1]

    """
    This function calculates the cost between two given nodes from the graph.

    @param graph A graph containing all node values for the location
    @param node1 A number repsenting a valid node from graph
    @param node2 A number repsenting a valid node from graph
    @param type The type of node cost to calculate

    @exception If the given parameters are of None type
    @exception If the given parameters are empty strings

    @return A number representing the cost
    """
    def calculateNodeCosts(self, graph, node1, node2, type):
        if (graph and node1 and node2 and type) is None:
            raise Exception("None type values provided in calculateNodeCosts")
        elif (graph and node1 and node2 and type) == '':
            raise Exception("Empty values provided in calculateNodeCosts")

        if type == 'normal':
            try : 
                return graph.edges[node1, node2 ,0]["length"]
            except : 
                return graph.edges[node1, node2]["weight"]
        elif type == 'gain':
            return max(0, graph.nodes[node2]["elevation"] - graph.nodes[node1]["elevation"])
        elif type == 'drop':
            return max(0, graph.nodes[node1]["elevation"] - graph.nodes[node2]["elevation"])
        elif type == 'diff':
            return graph.nodes[node2]["elevation"] - graph.nodes[node1]["elevation"]
        else:
            return abs(graph.nodes[node1]["elevation"]-graph.nodes[node2]["elevation"])

    """
    This function calculates the total elevation value between two given nodes from the graph.

    @param graph A graph containing all node values for the location
    @param path An array of nodes representing the path
    @param type The type of elevation value to calculate

    @exception If the given parameters are of None type
    @exception If the given parameters are empty strings

    @return A number representing the total elevation type value for path
    """
    def calculateFinalElevation(self, graph, path, type):
        if (graph and path and type) is None:
            raise Exception("None type values provided in calculateFinalElevation")
        elif (graph and path and type) == '':
            raise Exception("Empty values provided in calculateFinalElevation")

        total = 0
        i = 0
        while i < len(path) - 1:
            if type == 'elevation-gain':
                total += max(0, self.calculateNodeCosts(graph, path[i], path[i+1], 'gain'))
            elif type == 'elevation-drop':
                total += max(0, self.calculateNodeCosts(graph, path[i], path[i+1], 'drop'))
            i += 1
        return total

# if __name__=="__main__":
#     source = tuple((42.3710233, -72.5175895))
#     destination = tuple((42.351556, -72.527381))

#     utilty = algorithmUtility()
#     print(utilty.calculateDistanceUsingCoords(source, destination))
#     amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
#     map = Map()
#     graph = map.generate_map(amherstCoordinates, 15000)
#     print(utilty.calculateNodeCosts(graph, 3271341845, 3271341826, "normal"))
#     print(utilty.calculateNodeCosts(graph, 3271341845, 3271341826, "gain"))
#     print(utilty.calculateNodeCosts(graph, 3271341845, 3271341826, "drop"))
#     print(utilty.calculateNodeCosts(graph, 3271341845, 3271341826, "diff"))
#     print(utilty.calculateNodeCosts(graph, 3271341845, 3271341826, "some-value"))

#     path = [3271341845, 3271341826, 66699873, 3271341805]

#     print(utilty.calculateFinalElevation(graph, path, 'elevation-gain'))
#     print(utilty.calculateFinalElevation(graph, path, 'elevation-drop'))


    