#Backend Unit Tests
import sys
import pytest
sys.path.append('../backend')
import algorithms as al
import dijkstra as dj
import astar as at


def test_algorithms_input_validation_suceeds_none():
    source = tuple((None, None))
    destination = tuple((None, None))
    elevation_type = "maximum"
    distance_limit = 125

    with pytest.raises(Exception):
        al.algorithms(source[0], source[1], destination[0], destination[1], elevation_type, distance_limit)

def test_dijsktra_input_validation_suceeds_none():
    graph = None
    source = tuple((None, None))
    destination = tuple((None, None))
    limit = None
    isMaximum = True
    shortest_distance = None

    with pytest.raises(Exception):
        dj.dijkstra(graph, source, destination, limit, isMaximum, shortest_distance)

def test_aStar_input_validation_suceeds_none():
    graph = None
    source = tuple((None, None))
    destination = tuple((None, None))
    limit = None
    isMaximum = True
    shortest_distance = None

    with pytest.raises(Exception):
        at.astar(graph, source, destination, limit, isMaximum, shortest_distance)



