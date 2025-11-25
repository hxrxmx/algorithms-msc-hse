from collections import deque


def components(graph):
    vertices = set(graph.keys())
    for neighs in graph.values():
        for neigh in neighs:
            vertices.add(neigh)

    visited = set()
    components = []

    for start in vertices:
        if start in visited:
            continue

        component = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            v = queue.popleft()
            component.add(v)

            for u in graph.get(v, []):
                if u not in visited:
                    visited.add(u)
                    queue.append(u)

        components.append(component)

    return components
