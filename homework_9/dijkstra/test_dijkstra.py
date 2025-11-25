from numpy import inf

from homework_9.dijkstra.dijkstra import dijkstra


def test_single_vertex():
    graph = {1: {}}
    dist = dijkstra(graph, 1)
    assert dist == {1: 0.0}


def test_two_vertices():
    graph = {
        1: {2: 5},
        2: {},
    }
    dist = dijkstra(graph, 1)
    assert dist[1] == 0
    assert dist[2] == 5


def test_vertex_only_as_neighbor():
    graph = {
        1: {2: 3},
    }
    dist = dijkstra(graph, 1)
    assert dist[1] == 0
    assert dist[2] == 3


def test_unreachable_vertex():
    graph = {
        1: {2: 1},
        2: {},
        3: {},
    }
    dist = dijkstra(graph, 1)
    assert dist[1] == 0
    assert dist[2] == 1
    assert dist[3] == inf


def test_multiple_paths_take_shortest():
    graph = {
        1: {2: 1, 3: 5},
        2: {3: 1},
        3: {},
    }
    dist = dijkstra(graph, 1)
    assert dist[1] == 0
    assert dist[2] == 1
    assert dist[3] == 2


def test_zero_weight_edges():
    graph = {
        1: {2: 0},
        2: {3: 0},
        3: {},
    }
    dist = dijkstra(graph, 1)
    assert dist[1] == 0
    assert dist[2] == 0
    assert dist[3] == 0


def test_cycle_graph():
    graph = {
        1: {2: 1, 3: 4},
        2: {3: 2},
        3: {1: 7},
    }
    dist = dijkstra(graph, 2)
    assert dist[2] == 0
    assert dist[3] == 2
    assert dist[1] == 9


def test_complex():
    graph = {
        1: {2: 18, 3: 1, 4: 20},
        2: {},
        3: {4: 10, 6: 5},
        4: {5: 1},
        5: {4: 2, 2: 11},
        6: {4: 7, 5: 2},
    }
    dist = dijkstra(graph, 1)
    assert dist[2] == 18
    assert dist[3] == 1
    assert dist[4] == 10
    assert dist[5] == 8
    assert dist[6] == 6
