# 定義圖形結構
# A+-B+-D
#  |  +-E+
#  +-C---+-F
#
#
#
#
#
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# 深度優先搜尋
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))

# 廣度優先搜尋
def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex])

# 測試深度優先搜尋和廣度優先搜尋
print("深度優先搜尋:")
dfs(graph, 'A')
print("\n廣度優先搜尋:")
bfs(graph, 'A')
