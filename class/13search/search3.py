def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    front_visited = {start}
    back_visited = {goal}
    front_queue = [(start, [start])]
    back_queue = [(goal, [goal])]

    while front_queue and back_queue:
        if front_queue:
            front_vertex, front_path = front_queue.pop(0)
            for neighbor in graph[front_vertex]:
                if neighbor not in front_visited:
                    front_visited.add(neighbor)
                    front_queue.append((neighbor, front_path + [neighbor]))
                    if neighbor in back_visited:
                        back_path = next(p for v, p in back_queue if v == neighbor)
                        return front_path + back_path[::-1][1:]

        if back_queue:
            back_vertex, back_path = back_queue.pop(0)
            for neighbor in graph[back_vertex]:
                if neighbor not in back_visited:
                    back_visited.add(neighbor)
                    back_queue.append((neighbor, back_path + [neighbor]))
                    if neighbor in front_visited:
                        front_path = next(p for v, p in front_queue if v == neighbor)
                        return front_path + back_path[::-1][1:]

    return None

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    front_visited = {start}
    back_visited = {goal}
    front_queue = [(start, [start])]
    back_queue = [(goal, [goal])]

    while front_queue and back_queue:
        if front_queue:
            front_vertex, front_path = front_queue.pop(0)
            for neighbor in graph[front_vertex]:
                if neighbor not in front_visited:
                    front_visited.add(neighbor)
                    front_queue.append((neighbor, front_path + [neighbor]))
                    if neighbor in back_visited:
                        back_path = next(p for v, p in back_queue if v == neighbor)
                        return front_path + back_path[::-1][1:]

        if back_queue:
            back_vertex, back_path = back_queue.pop(0)
            for neighbor in graph[back_vertex]:
                if neighbor not in back_visited:
                    back_visited.add(neighbor)
                    back_queue.append((neighbor, back_path + [neighbor]))
                    if neighbor in front_visited:
                        front_path = next(p for v, p in front_queue if v == neighbor)
                        return front_path + back_path[::-1][1:]

    return None
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bidirectional_search(graph, 'A', 'F'))
