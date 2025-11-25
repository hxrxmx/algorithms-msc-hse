import heapq

from numpy import inf


# сделаем для ориентированного, так как в задании тип не указан,
# а ориентирован - частный случай первого в контексте этого алгоритма
def dijkstra(
    graph,
    start,
):
    vertices = set(graph.keys())
    for neighs in graph.values():
        vertices.update(neighs.keys())

    dist = {v: inf for v in vertices}
    dist[start] = 0.0

    heap = [(0.0, start)]

    while heap:
        distance, vertex = heapq.heappop(heap)

        if distance > dist[vertex]:
            continue

        for u, w in graph.get(vertex, {}).items():
            new_distance = distance + w
            if new_distance < dist[u]:
                dist[u] = new_distance
                heapq.heappush(heap, (new_distance, u))

    return dist
