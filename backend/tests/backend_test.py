#Backend Unit Tests
import sys
import os
import pytest
sys.path.append('../backend')
import algorithms as al
import dijkstra as dj
import astar as at
import shortestPath as sp
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
    source = tuple((42.35081772765568, -72.52727125397264))
    destination = tuple((42.386760374718236, -72.52481790025085))

    shortest_path = sp.shortestPath(graph, source, destination)
    shortest_path_values = shortest_path.run()

    assert len(shortest_path_values['path']) == 103
    assert shortest_path_values['distance'] == 4633.4389999999985
    assert shortest_path_values['elevation_gain'] == 75

def test_aStar_diff_location_max_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    source = tuple((42.35081772765568, -72.52727125397264))
    destination = tuple((42.386760374718236, -72.52481790025085))
    limit = 1.25
    isMaximum = True
    shortest_distance = sp.shortestPath(graph, source, destination).run()['distance']

    a_star = at.astar(graph, source, destination, limit, isMaximum, shortest_distance)
    a_star_values = a_star.run()

    assert len(a_star_values['path']) == 95
    assert a_star_values['distance'] == 5747.205000000002
    assert a_star_values['elevation_gain'] == 87

def test_aStar_diff_location_min_elevation():
    map = Map()
    amherstCoordinates = tuple((42.37444161675649, -72.51956880913377))
    graph = map.generate_map(amherstCoordinates, 15000)
    source = tuple((42.35081772765568, -72.52727125397264))
    destination = tuple((42.386760374718236, -72.52481790025085))
    limit = 1.25
    isMaximum = False
    shortest_distance = sp.shortestPath(graph, source, destination).run()['distance']

    a_star = at.astar(graph, source, destination, limit, isMaximum, shortest_distance)
    a_star_values = a_star.run()

    assert len(a_star_values['path']) == 95
    assert a_star_values['distance'] == 5747.395000000001
    assert a_star_values['elevation_gain'] == 87






    







