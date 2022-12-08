import numpy as np
import math
# import osmnx as ox
# from map_lib import Map

class algorithmUtility:
    def calculateDistanceUsingCoords(self, src, dest):
        # R = 6371 kms
        # distance = 2R⋅sin⁻¹(√[sin²((θ₂ - θ₁)/2) + cosθ₁⋅cosθ₂⋅sin²((φ₂ - φ₁)/2)])
        # theta = lat, phi = long

        if (src and dest) is None:
            raise Exception("None type values not provided in calculateDistanceUsingCoords function")

        R = 6371000
        srcLat, srcLong = np.radians(src[0]), np.radians(src[1])
        destLat, destLong = np.radians(dest[0]), np.radians(dest[1])

        val1 = math.pow(np.sin((destLat - srcLat)/2), 2)
        val2 = np.cos(srcLat)*np.cos(destLat)
        val3 = math.pow(np.sin((destLong - srcLong)/2), 2)
        val = math.sqrt(val1 + val2 * val3)

        dist = 2 * R * np.arcsin(val)
        return dist

    def calculateNodeCosts(self, graph, node1, node2, type):
        if (graph and node1 and node2 and type) is None:
            raise Exception("None type values not provided in calculateNodeCosts")

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

    def calculateFinalElevation(self, graph, path, type):
        if (graph and path and type) is None:
            raise Exception("None type values not provided in calculateFinalElevation")

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


    