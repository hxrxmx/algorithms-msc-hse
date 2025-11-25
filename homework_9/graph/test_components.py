# test_connected_components.py
from homework_9.graph.components import components


def normalize(comps):
    return sorted([sorted(c) for c in comps])


def test_empty():
    graph = {}
    assert components(graph) == []


def test_no_edges():
    graph = {1: []}
    assert normalize(components(graph)) == [[1]]


def test_isolated():
    graph = {1: [], 2: []}
    comps = normalize(components(graph))
    assert comps == [[1], [2]]


def test_vertex_only_as_neighbor():
    graph = {1: [2]}  # 2 нет среди ключей
    comps = normalize(components(graph))
    assert comps == [[1, 2]]


def test_mixed_component_types():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2],
        4: [],  # изолированная вершина
        5: [6],
        6: [5],
    }
    comps = normalize(components(graph))
    assert comps == [[1, 2, 3], [4], [5, 6]]


def test_loops_n_duplicate_edges():
    graph = {
        1: [1, 2, 2],
        2: [1, 2],
        3: [],
    }
    comps = normalize(components(graph))
    assert comps == [[1, 2], [3]]


def test_asymmetric():
    graph = {
        1: [2, 3],
        2: [],  #
        3: [],  # не ссылаются обратно в 1
        4: [5],
        5: [4],
    }
    comps = normalize(components(graph))
    assert comps == [[1, 2, 3], [4, 5]]
