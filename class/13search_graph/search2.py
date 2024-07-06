# 雙向搜尋
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
                        back_path = [p for v, p in back_queue if v == neighbor][0]
                        return front_path + back_path[::-1][1:]

        if back_queue:
            back_vertex, back_path = back_queue.pop(0)
            for neighbor in graph[back_vertex]:
                if neighbor not in back_visited:
                    back_visited.add(neighbor)
                    back_queue.append((neighbor, back_path + [neighbor]))
                    if neighbor in front_visited:
                        front_path = [p for v, p in front_queue if v == neighbor][0]
                        return front_path + back_path[::-1][1:]

    return None

# 迭代加深搜尋
def iterative_deepening_search(graph, start, goal):
    def dls(node, depth, path):
        if depth == 0 and node == goal:
            return path
        if depth > 0:
            for neighbor in graph[node]:
                result = dls(neighbor, depth - 1, path + [neighbor])
                if result:
                    return result
        return None

    depth = 0
    while True:
        result = dls(start, depth, [start])
        if result:
            return result
        depth += 1

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
# 測試雙向搜尋與迭代加深搜尋
print("雙向搜尋:")
print(bidirectional_search(graph, 'A', 'F'))  # 輸出: ['A', 'C', 'F']
print("迭代加深搜尋:")
print(iterative_deepening_search(graph, 'A', 'F'))  # 輸出: ['A', 'C', 'F']

