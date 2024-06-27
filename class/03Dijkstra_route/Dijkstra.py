import heapq

def dijkstra(graph, start):
    # 儲存每個節點的最短距離
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # 儲存未處理的節點
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # 如果當前距離大於已知的最短距離，則跳過
        if current_distance > distances[current_vertex]:
            continue
        
        # 更新鄰居的距離
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # 只有當發現更短的距離時才進行更新
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 測試Dijkstra演算法
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print(f"從節點 {start_vertex} 到其他節點的最短距離:")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")
