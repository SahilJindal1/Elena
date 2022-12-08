#Backend Unit Tests
import sys
import os
import pytest
sys.path.append(os.path.split(os.path.dirname(__file__))[0])
import algorithms as al
import dijkstra as dj
import astar as at
import shortestPath as sp
import algorithmUtility as au
from map_lib import Map


def test_algorithms_input_validation_succeeds_none():
    source = tuple((None, None))
    destination = tuple((None, None))
    elevation_type = "maximum"
    distance_limit = 125

    with pytest.raises(Exception):
        al.algorithms(source[0], source[1], destination[0], destination[1], elevation_type, distance_limit)

def test_shortest_input_validation_succeeds_none():
    graph = None
    source = tuple((None, None))
    destination = tuple((None, None))

    with pytest.raises(Exception):
        sp.shortestPath(graph, source, destination)

def test_dijsktra_input_validation_succeeds_none():
    graph = None
    source = tuple((None, None))
    destination = tuple((None, None))
    limit = None
    isMaximum = True
    shortest_distance = None

    with pytest.raises(Exception):
        dj.dijkstra(graph, source, destination, limit, isMaximum, shortest_distance)

def test_aStar_input_validation_succeeds_none():
    graph = None
    source = tuple((None, None))
    destination = tuple((None, None))
    limit = None
    isMaximum = True
    shortest_distance = None

    with pytest.raises(Exception):
        at.astar(graph, source, destination, limit, isMaximum, shortest_distance)

def test_calculateDistanceUsingCoords_input_validation():
    source = None
    destination = None

    with pytest.raises(Exception):
        utilty = au.algorithmUtility()
        utilty.calculateDistanceUsingCoords(source, destination)
        
def test_calculateDistanceUsingCoords():
    source = tuple((42.3710233, -72.5175895))
    destination = tuple((42.351556, -72.527381))

    utilty = au.algorithmUtility()
    distance = utilty.calculateDistanceUsingCoords(source, destination)
    
    assert distance == 2309.3278617748715

def test_calculateNodeCosts_input_validation():
    graph = None
    sourceNode = 3271341845
    destinationNode = 3271341826
    type = None

    with pytest.raises(Exception):
        utilty = au.algorithmUtility()
        utilty.calculateNodeCosts(graph, sourceNode, destinationNode, type)

def test_calculateNodeCosts():
    sourceNode = 3271341845
    destinationNode = 3271341826
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)

    utilty = au.algorithmUtility()
    normal_distance = utilty.calculateNodeCosts(graph, sourceNode, destinationNode, "normal")
    gain_distance = utilty.calculateNodeCosts(graph, sourceNode, destinationNode, "gain")
    drop_distance = utilty.calculateNodeCosts(graph, sourceNode, destinationNode, "drop")
    diff_distance = utilty.calculateNodeCosts(graph, sourceNode, destinationNode, "diff")
    other_distance = utilty.calculateNodeCosts(graph, sourceNode, destinationNode, "any-value")

    assert normal_distance == 36.218
    assert gain_distance == 0
    assert drop_distance == 2
    assert diff_distance == -2
    assert other_distance == 2

def test_calculateFinalElevation_input_validation():
    graph = None
    type = None
    path = [3271341845, 3271341826, 66699873, 3271341805]
    
    with pytest.raises(Exception):
        utilty = au.algorithmUtility()
        utilty.calculateFinalElevation(graph, path, type)

def test_calculateFinalElevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    path = [3271341845, 3271341826, 66699873, 3271341805]

    utilty = au.algorithmUtility()
    elevation_gain = utilty.calculateFinalElevation(graph, path, 'elevation-gain')
    elevation_drop = utilty.calculateFinalElevation(graph, path, 'elevation-drop')
    other = utilty.calculateFinalElevation(graph, path, 'any-value')

    assert elevation_gain == 0
    assert elevation_drop == 2
    assert other == 0

def test_shortest_same_location():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    location = tuple((42.35081772765568, -72.52727125397264))

    shortest_path = sp.shortestPath(graph, location, location)
    shortest_path_values = shortest_path.run()

    assert len(shortest_path_values['path']) == 1
    assert shortest_path_values['distance'] == 0
    assert shortest_path_values['elevation_gain'] == 0

def test_dijkstra_same_location_max_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    location = tuple((42.35081772765568, -72.52727125397264))
    limit = 1.25
    isMaximum = True
    shortest_distance = sp.shortestPath(graph, location, location).run()['distance']

    dijkstra = dj.dijkstra(graph, location, location, limit, isMaximum, shortest_distance)
    dijkstra_values = dijkstra.run()

    assert len(dijkstra_values['path']) == 1
    assert dijkstra_values['distance'] == 0
    assert dijkstra_values['elevation_gain'] == 0

def test_dijkstra_same_location_min_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    location = tuple((42.35081772765568, -72.52727125397264))
    limit = 1.25
    isMaximum = False
    shortest_distance = sp.shortestPath(graph, location, location).run()['distance']

    dijkstra = dj.dijkstra(graph, location, location, limit, isMaximum, shortest_distance)
    dijkstra_values = dijkstra.run()

    assert len(dijkstra_values['path']) == 1
    assert dijkstra_values['distance'] == 0
    assert dijkstra_values['elevation_gain'] == 0

def test_aStar_same_location_max_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    location = tuple((42.35081772765568, -72.52727125397264))
    limit = 1.25
    isMaximum = True
    shortest_distance = sp.shortestPath(graph, location, location).run()['distance']

    a_star = at.astar(graph, location, location, limit, isMaximum, shortest_distance)
    a_star_values = a_star.run()

    assert len(a_star_values['path']) == 1
    assert a_star_values['distance'] == 0
    assert a_star_values['elevation_gain'] == 0

def test_aStar_same_location_min_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    location = tuple((42.35081772765568, -72.52727125397264))
    limit = 1.25
    isMaximum = False
    shortest_distance = sp.shortestPath(graph, location, location).run()['distance']

    a_star = at.astar(graph, location, location, limit, isMaximum, shortest_distance)
    a_star_values = a_star.run()

    assert len(a_star_values['path']) == 1
    assert a_star_values['distance'] == 0
    assert a_star_values['elevation_gain'] == 0

def test_shortest_diff_location():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    source = tuple((42.3710233, -72.5175895))
    destination = tuple((42.351556, -72.527381))

    shortest_path = sp.shortestPath(graph, source, destination)
    shortest_path_values = shortest_path.run()

    assert len(shortest_path_values['path']) == 35
    assert shortest_path_values['distance'] == 2687.1060000000007
    assert shortest_path_values['elevation_gain'] == 15

def test_aStar_diff_location_max_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    source = tuple((42.3710233, -72.5175895))
    destination = tuple((42.351556, -72.527381))
    limit = 1.25
    isMaximum = True
    shortest_distance = sp.shortestPath(graph, source, destination).run()['distance']

    a_star = at.astar(graph, source, destination, limit, isMaximum, shortest_distance)
    a_star_values = a_star.run()

    assert len(a_star_values['path']) == 33
    assert a_star_values['distance'] == 2857.2499999999995
    assert a_star_values['elevation_gain'] == 11

def test_aStar_diff_location_min_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    source = tuple((42.3710233, -72.5175895))
    destination = tuple((42.351556, -72.527381))
    limit = 1.25
    isMaximum = False
    shortest_distance = sp.shortestPath(graph, source, destination).run()['distance']

    a_star = at.astar(graph, source, destination, limit, isMaximum, shortest_distance)
    a_star_values = a_star.run()

    assert len(a_star_values['path']) == 33
    assert a_star_values['distance'] == 2857.2499999999995
    assert a_star_values['elevation_gain'] == 11

def test_dijkstra_diff_location_max_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    source = tuple((42.3710233, -72.5175895))
    destination = tuple((42.351556, -72.527381))
    limit = 1.25
    isMaximum = True
    shortest_distance = sp.shortestPath(graph, source, destination).run()['distance']

    dijkstra = dj.dijkstra(graph, source, destination, limit, isMaximum, shortest_distance)
    a_star_values = dijkstra.run()

    assert len(a_star_values['path']) == 68
    assert a_star_values['distance'] == 3244.9270000000006
    assert a_star_values['elevation_gain'] == 41

def test_dijkstra_diff_location_min_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    source = tuple((42.3710233, -72.5175895))
    destination = tuple((42.351556, -72.527381))
    limit = 1.25
    isMaximum = False
    shortest_distance = sp.shortestPath(graph, source, destination).run()['distance']

    dijkstra = dj.dijkstra(graph, source, destination, limit, isMaximum, shortest_distance)
    a_star_values = dijkstra.run()

    assert len(a_star_values['path']) == 68
    assert a_star_values['distance'] == 3244.9270000000006
    assert a_star_values['elevation_gain'] == 41
    







