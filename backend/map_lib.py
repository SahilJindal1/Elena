import os 
import osmnx
import pickle
import networkx
import requests
import pandas as pd

class Map:

    def __init__(self) -> None:
        self.url = "https://api.open-elevation.com/api/v1/lookup?locations={}"
        pass

    def generate_map(self,source,dist, mapFilePath='./Map.map'):
        """
        # mapFilePath = path to the map file
        # source = (lat,long)
        # dist = ditance in meters
        """
        
        if(mapFilePath != None):
            if os.path.exists(mapFilePath):
                print("Map Present")
                map = pickle.load(open(mapFilePath, "rb"))
                print("Map Loaded")
                return map
        # getting new map
        print("Creating New Map Graph")
        map = osmnx.graph.graph_from_point(source, dist, network_type="walk")
        map = self.addElevationToMap(map,100)
        pickle.dump(map, open( "Map.map", "wb" ))
        print("New Map Graph Created")
        return map

    def addElevationToMap(self, map, batch=100):
        """
        map: the map graph in which we need to add the elevations
        bath: batch size for open elevation api so that we can add elevations faster. Note there is a limit for open Api Get url.
        """
        point_dict = {}
        for nodeid, data in map.nodes(data=True):
            point_dict[nodeid] = '{:.5f},{:.5f}'.format(data['y'], data['x'])
        nodeLatLongDataframe = pd.Series(point_dict)
        results = []
        for i in range(0, len(nodeLatLongDataframe),batch):
            locationLatLong = '|'.join(nodeLatLongDataframe.iloc[i: i + batch])
            url = self.url.format(locationLatLong)
            responseJSON = requests.get(url).json()
            results.extend(responseJSON['results'])
        elevationDict = {}
        nodeIds = list(point_dict.keys())
        for idx in range(len(nodeIds)):
            elevationDict[nodeIds[idx]] = results[idx]['elevation']
        
        networkx.set_node_attributes(map, name='elevation', values=elevationDict)
        return map

# if __name__=="__main__":
#     newMap = Map()
#     mp = newMap.generate_map(None,(42.37444161675649, -72.51956880913377),30000)