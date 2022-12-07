import osmnx as ox

import algorithmUtility as au

class astar:
    def __init__(self, graph, src, dest, limit, isMaximum, shortestDistance) -> None:
        self.graph = graph
        self.src = src
        self.dest = dest
        self.limit = limit
        self.isMaximum = isMaximum
        # X = long, Y = lat
        self.srcNode, self.srcDistance = ox.distance.nearest_nodes(self.graph, X = self.src[1], Y=self.src[0], return_dist = True)
        self.destNode, self.destDistance = ox.distance.nearest_nodes(self.graph, X = self.dest[1], Y=self.dest[0], return_dist = True)
        self.shortestDistance = shortestDistance
        self.utilities = au.algorithmUtility()

    def calculateNodeHeuristics(self):
        destination = self.graph.nodes[self.destNode]
        destCoords = destination['y'], destination['x']
        heuristics =  dict()

        for n, data in self.graph.nodes(data=True):
            currCoords = data['y'], data['x']
            heuristics[n] = self.utilities.calculateDistanceUsingCoords(destCoords, currCoords)

        return heuristics

    def backtrack(self, currNode, parent):
        path = [currNode]

        while currNode in parent:
            currNode = parent[currNode]
            path.append(currNode)

        return path[::-1]

    def run(self):
        open, closed = set(), set()
        g, normalDistance, f, parent = dict(), dict(), dict(), dict()
        h = self.calculateNodeHeuristics()
        for n in self.graph.nodes():
            g[n] = float('inf')
            normalDistance[n] = float('inf')

        open.add(self.srcNode)
        g[self.srcNode] = 0
        normalDistance[self.srcNode] = 0
        f[self.srcNode] = h[self.srcNode] 
        while len(open) > 0 :
            currNode = min(open, key=lambda x: f[x]) 
            if currNode == self.destNode:
                path = self.backtrack(currNode, parent)
                totalElevationGain = self.utilities.calculateFinalElevation(self.graph, path, 'elevation-gain')
                pathLengths = ox.utils_graph.get_route_edge_attributes(self.graph, path, 'length')
                distance = sum(pathLengths)
                values = dict()
   
                latLongPath = list()
                for node in path:
                    point = self.graph.nodes[node]
                    latLongPath.append((point['x'], point['y']))
            
                values['path'] = latLongPath
                values['distance'] = distance
                values['elevation_gain'] = totalElevationGain
                return values
            
            open.remove(currNode)
            closed.add(currNode)

            for n in self.graph.neighbors(currNode):
                if n in closed: 
                    continue 
                else:
                    if self.isMaximum:
                        # have to maximize the elevation => but I will take minimum of values => 
                        # so the least value should be the most elevated
                        # hence drop value negative would mean, its elevated
                        curr_g = g[currNode] + self.utilities.calculateNodeCosts(self.graph, currNode, n, "drop")  
                    else:  
                        # have to minimize the elvation => but I will take minimum of values => 
                        # so the least value should be the least elevated
                        # hence gain value positive would mean, its elevated
                        curr_g = g[currNode] + self.utilities.calculateNodeCosts(self.graph, currNode, n, "gain")

                    currDistance = normalDistance[currNode] + self.utilities.calculateNodeCosts(self.graph, currNode, n, "normal")

                    if n in open:
                        if curr_g >= g[n] or currDistance > self.limit * self.shortestDistance:
                            continue
                    else:
                        if currDistance <= self.limit * self.shortestDistance:
                            open.add(n)

                    g[n] = curr_g
                    normalDistance[n] = currDistance
                    f[n] = g[n] + h[n]
                    parent[n] =  currNode 