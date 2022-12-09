import osmnx as ox
import algorithmUtility as au
from collections import defaultdict
import heapq

"""
This class executes the Dijsktra algorithm.
"""
class dijkstra:
    """
    This function initializes the dijkstra class with the given parameters.

    @param graph A graph containing all node values for the location
    @param src A tuple representing the source location latitude and longitude
    @param dest A tuple representing the destination location latitude and longitude
    @param limit A number representing the maximum distance limit percentage
    @param isMaximum A boolean representing if the elevation gain type is maximum
    @param shortestDistance A number representing the shortest path distance

    @exception If the given parameters are of None type
    @exception If the given parameters are empty strings
    """
    def __init__(self,graph,src,dest,limit,isMaximum,shortestDistance) -> None:
        if graph and src and dest and limit and isMaximum and shortestDistance is None:
            raise Exception("None type Parameters in Dijkstra")
        elif (graph and src and dest and limit and isMaximum and shortestDistance) == '':
            raise Exception("Empty Parameters in Dijkstra")
        else:
            self.graph = graph
            self.src = src
            self.dest = dest
            self.srcNode, self.srcDistance = ox.distance.nearest_nodes(self.graph, X = self.src[1], Y=self.src[0], return_dist = True)
            self.destNode, self.destDistance = ox.distance.nearest_nodes(self.graph, X = self.dest[1], Y=self.dest[0], return_dist = True)
            self.utilities = au.algorithmUtility()
            self.shortestDistance = shortestDistance
            self.isMaximum = isMaximum
            self.limit = limit
    
    """
    This function runs this specific Dijkstra algorithm.

    @exception If the calculates source and destionation nodes are not valid

    @return A dictionary of values having path, distance and elevation gain for Dijkstra
    """
    def run(self):
        if (self.srcNode and self.destNode) is None:
            raise Exception("Not Valid Nodes")

        q = [(0.0, 0.0, self.srcNode)]
        visitedNodes = set()
        minimum_distances = {self.srcNode:0}

        parentDict = defaultdict(int)

        while(len(q)!=0):
            currPriority,currDist,currNode = heapq.heappop(q)
            if currNode not in visitedNodes:
                visitedNodes.add(currNode)
                if currNode == self.destNode:
                    path = self.utilities.backtrack(currNode,parentDict)
                    finalGain, finalDrop = self.utilities.calculateFinalElevation(self.graph,path,'elevation-gain'),self.utilities.calculateFinalElevation(self.graph,path,'elevation-drop')
                    pathLengths = ox.utils_graph.get_route_edge_attributes(self.graph, path, 'length')
                    distance = sum(pathLengths)
                    values = dict()
                    latLongPath = list()    

                    for node in path:
                        point = self.graph.nodes[node]
                        latLongPath.append((point['x'], point['y']))
                    
                    print("Here's the path",path)
                    values['path'] = latLongPath
                    values['distance'] = distance
                    values['elevation_gain'] = finalGain
                    return values
                
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
        print("no path")
        