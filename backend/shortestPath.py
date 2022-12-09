import osmnx as ox
import networkx as nx
import algorithmUtility as au

"""
This class executes the Shortest path algorithm.
"""
class shortestPath:
    """
    This function initializes the shortestPath class with the given parameters.

    @param graph A graph containing all node values for the location
    @param src A tuple representing the source location latitude and longitude
    @param dest A tuple representing the destination location latitude and longitude
    
    @exception If the given parameters are of None type
    @exception If the given parameters are empty strings
    """
    def __init__(self, graph, src, dest) -> None:
        if (graph and src and dest) is None:
            raise Exception("None type Parameters in shortest Path")
        elif (graph and src and dest) == '':
            raise Exception("Empty Parameters in shortest Path")
        else:
            self.graph = graph
            self.src = src
            self.dest = dest
            self.srcNode, self.srcDistance = ox.distance.nearest_nodes(self.graph, X = self.src[1], Y=self.src[0], return_dist = True)
            self.destNode, self.destDistance = ox.distance.nearest_nodes(self.graph, X = self.dest[1], Y=self.dest[0], return_dist = True)
            self.utilities = au.algorithmUtility()

    """
    This function runs this specific shortest path algorithm.

    @exception If the calculates source and destionation nodes are not valid

    @return A dictionary of values having path, distance and elevation gain for shortest path
    """
    def run(self):
        if (self.srcNode and self.destNode) is None:
            raise Exception("Not Valid Nodes")
        path = nx.shortest_path(self.graph, source = self.srcNode, target = self.destNode, weight='length')
        pathLengths = ox.utils_graph.get_route_edge_attributes(self.graph, path, 'length')
        distance = sum(pathLengths)

        self.shortestDistance = distance
        totalElevationGain = self.utilities.calculateFinalElevation(self.graph, path, 'elevation-gain')
        values = dict()
        latLongPath = list()

        for node in path:
            point = self.graph.nodes[node]
            latLongPath.append((point['x'], point['y']))
        
        values['path'] = latLongPath
        values['distance'] = distance
        values['elevation_gain'] = totalElevationGain
        return values
