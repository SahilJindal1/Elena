import osmnx as ox
import networkx as nx
import algorithmUtility as au

class shortestPath:
    def __init__(self, graph, src, dest) -> None:
        self.graph = graph
        self.src = src
        self.dest = dest
        self.srcNode, self.srcDistance = ox.distance.nearest_nodes(self.graph, X = self.src[1], Y=self.src[0], return_dist = True)
        self.destNode, self.destDistance = ox.distance.nearest_nodes(self.graph, X = self.dest[1], Y=self.dest[0], return_dist = True)
        self.utilities = au.algorithmUtility()

    def run(self):
        path = nx.shortest_path(self.graph, source = self.srcNode, target = self.destNode, weight='length')
        pathLengths = ox.utils_graph.get_route_edge_attributes(self.graph, path, 'length')
        distance = sum(pathLengths)

        self.shortestDistance = distance
        totalElevationGain = self.utilities.calculateFinalElevation(self.graph, path, 'elevation-gain')
        values = dict()
        values['path'] = path
        values['distance'] = distance
        values['elevation_gain'] = totalElevationGain
        return values
