import osmnx as ox
import algorithmUtility as au
from collections import defaultdict
import heapq
import networkx as nx

class dijkstra:

    def __init__(self,graph,src,dest,limit,isMaximum,shortestDistance) -> None:
        self.graph = graph
        self.src = src
        self.dest = dest
        self.srcNode, self.srcDistance = ox.distance.nearest_nodes(self.graph, X = self.src[1], Y=self.src[0], return_dist = True)
        self.destNode, self.destDistance = ox.distance.nearest_nodes(self.graph, X = self.dest[1], Y=self.dest[0], return_dist = True)
        self.utilities = au.algorithmUtility()
        self.shortestDistance = shortestDistance
        self.isMaximum = isMaximum
        self.limit = limit
    
    def backtrack(self, currNode, parent):
        path = [currNode]

        while currNode in parent:
            currNode = parent[currNode]
            path.append(currNode)

        return path[::-1]

    def run(self):

        q = [(0.0, 0.0, self.srcNode)]
        visitedNodes = set()
        minimum_distances = {self.srcNode:0}

        parentDict = defaultdict(int)

        while(len(q)!=0):
            currPriority,currDist,currNode = heapq.heappop(q)
            if currNode not in visitedNodes:
                visitedNodes.add(currNode)
                if currNode == self.destNode:
                    return currPriority,currDist,parentDict
                
                for neighbor in self.graph.neighbors(currNode):
                    if neighbor in visitedNodes:
                        continue
                    previous = minimum_distances.get(neighbor, None)
                    currDiff = self.utilities.calculateNodeCosts(self.graph,currNode, neighbor, "normal")

                    if self.limit <=1.5:
                        nextDiff = (currDiff - self.utilities.calculateNodeCosts(self.graph,currNode,neighbor,"diff"))*currDiff
                    else:
                        if(self.isMaximum):
                            nextDiff = currDiff + self.utilities.calculateNodeCosts(self.graph,currNode,neighbor,"drop")
                        else:
                            nextDiff = currDiff + self.utilities.calculateNodeCosts(self.graph,currNode,neighbor,"gain")
                        nextDiff += currPriority
                         
                    nextDist = currDist + currDiff

                    if nextDist<=(self.shortestDistance*self.limit) and (previous is None or nextDiff<previous):
                        parentDict[neighbor] = currNode
                        minimum_distances[neighbor] = nextDiff
                        heapq.heappush(q,(nextDiff,nextDist,neighbor))
        
        if not currDist:
            return

        path = self.backtrack(currNode,parentDict)
        finalGain, finalDrop = self.utilities.calculateFinalElevation(self.graph,path,'elevation-gain'),self.utilities.calculateFinalElevation(self.graph,path,'elevation-drop')
        pathLengths = ox.utils_graph.get_route_edge_attributes(self.graph, path, 'length')
        distance = sum(pathLengths)
        values = dict()
        latLongPath = list()    

        print("Here's the path", path)

        for node in path:
            point = self.graph.nodes[node]
            latLongPath.append((point['x'], point['y']))
        
        values['path'] = latLongPath
        values['distance'] = distance
        values['elevation_gain'] = finalGain
        return values