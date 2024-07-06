from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bidirectional_search(self, start, goal):
        if start not in self.graph or goal not in self.graph:
            return None

        if start == goal:
            return [start]

        # Initialize frontiers for both searches
        frontier_start = deque([start])
        frontier_goal = deque([goal])

        # Initialize visited nodes and parents
        visited_start = {start: None}
        visited_goal = {goal: None}

        while frontier_start and frontier_goal:
            # Expand from the start side
            if frontier_start:
                current_start = frontier_start.popleft()
                for neighbor in self.graph[current_start]:
                    if neighbor not in visited_start:
                        visited_start[neighbor] = current_start
                        frontier_start.append(neighbor)
                        # If we find a connection
                        if neighbor in visited_goal:
                            return self._construct_path(neighbor, visited_start, visited_goal)

            # Expand from the goal side
            if frontier_goal:
                current_goal = frontier_goal.popleft()
                for neighbor in self.graph[current_goal]:
                    if neighbor not in visited_goal:
                        visited_goal[neighbor] = current_goal
                        frontier_goal.append(neighbor)
                        # If we find a connection
                        if neighbor in visited_start:
                            return self._construct_path(neighbor, visited_start, visited_goal)

        return None

    def _construct_path(self, meeting_node, visited_start, visited_goal):
        # Construct path from start to meeting node
        path = []
        node = meeting_node
        while node is not None:
            path.append(node)
            node = visited_start[node]
        path = path[::-1]  # reverse the start to meeting path

        # Construct path from meeting node to goal
        node = visited_goal[meeting_node]
        while node is not None:
            path.append(node)
            node = visited_goal[node]

        return path

# Example usage
if __name__ == "__main__":
    graph = Graph()
    edges = [
        ('A','B'), ('A','C'),
        ('B','D'), ('B','E'),
        ('C','F'),
        ('E','F')
    ]

    for u, v in edges:
        graph.add_edge(u, v)

    start_node = 'A'
    goal_node = 'F'
    path = graph.bidirectional_search(start_node, goal_node)

    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found between {start_node} and {goal_node}")
