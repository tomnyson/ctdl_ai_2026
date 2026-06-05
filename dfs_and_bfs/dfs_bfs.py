from collections import deque


# ─── Graph representation (adjacency list) ───────────────────────────────────

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


# ─── Depth-First Search (DFS) ─────────────────────────────────────────────────

def dfs_recursive(graph, node, visited=None):
    """DFS sử dụng đệ quy."""
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited


def dfs_iterative(graph, start):
    """DFS sử dụng stack (không đệ quy)."""
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Đẩy các đỉnh kề chưa thăm vào stack (đảo ngược để giữ thứ tự)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order


# ─── Breadth-First Search (BFS) ───────────────────────────────────────────────

def bfs(graph, start):
    """BFS sử dụng hàng đợi (queue)."""
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# ─── Demo ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("=== Đồ thị (adjacency list) ===")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")

    print("\n=== DFS (đệ quy) từ 'A' ===")
    dfs_recursive(graph, 'A')
    print()

    print("\n=== DFS (iterative) từ 'A' ===")
    result = dfs_iterative(graph, 'A')
    print(' '.join(result))

    print("\n=== BFS từ 'A' ===")
    result = bfs(graph, 'A')
    print(' '.join(result))
