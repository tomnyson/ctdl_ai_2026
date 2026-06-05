import heapq


# ─── Đồ thị có trọng số (vô hướng) ──────────────────────────────────────────
# Danh sách cạnh: (u, v, weight)
EDGES = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('B', 'E', 7),
    ('C', 'E', 3),
    ('C', 'F', 8),
    ('D', 'F', 11),
    ('E', 'D', 4),
    ('E', 'F', 6),
]

NODES = ['A', 'B', 'C', 'D', 'E', 'F']


def build_adj(edges, nodes):
    """Xây dựng danh sách kề từ danh sách cạnh."""
    adj = {n: [] for n in nodes}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    return adj


# ════════════════════════════════════════════════════════════
#  DIJKSTRA — Đường đi ngắn nhất từ một đỉnh nguồn
# ════════════════════════════════════════════════════════════

def dijkstra(nodes, edges, src):
    """
    Thuật toán Dijkstra tìm đường đi ngắn nhất từ đỉnh src đến tất cả đỉnh.

    Trả về:
        dist (dict): khoảng cách nhỏ nhất từ src đến mỗi đỉnh
        prev (dict): đỉnh trước đó trên đường đi ngắn nhất
    """
    adj = build_adj(edges, nodes)

    dist = {n: float('inf') for n in nodes}
    prev = {n: None for n in nodes}
    dist[src] = 0

    # Min-heap: (distance, node)
    heap = [(0, src)]
    settled = set()

    print(f"\n{'='*50}")
    print(f"  DIJKSTRA từ đỉnh '{src}'")
    print(f"{'='*50}")
    print(f"{'Bước':<6} {'Settle':<8} {'Xét cạnh':<16} {'Cập nhật dist'}")
    print('-' * 50)

    step = 0
    while heap:
        d, u = heapq.heappop(heap)

        if u in settled:
            continue
        settled.add(u)
        step += 1
        print(f"{step:<6} {u:<8}", end='')

        first = True
        for v, w in adj[u]:
            if v in settled:
                continue
            new_d = dist[u] + w
            edge_str = f"{u}→{v}(w={w})"
            update_str = ''
            if new_d < dist[v]:
                dist[v] = new_d
                prev[v] = u
                heapq.heappush(heap, (new_d, v))
                update_str = f"dist[{v}]={new_d}"
            if first:
                print(f"{edge_str:<16} {update_str}")
                first = False
            else:
                print(f"{'':14} {edge_str:<16} {update_str}")

        if first:
            print()  # không có cạnh nào

    print('-' * 50)
    print("\n📊 Kết quả khoảng cách ngắn nhất:")
    for n in nodes:
        path = get_path(prev, src, n)
        d_str = str(dist[n]) if dist[n] != float('inf') else '∞'
        print(f"  {src} → {n}: dist={d_str:<5}  đường đi: {' → '.join(path)}")

    return dist, prev


def get_path(prev, src, dst):
    """Truy vết đường đi từ src đến dst."""
    path = []
    cur = dst
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    if path[0] != src:
        return ['(không có đường)']
    return path


# ════════════════════════════════════════════════════════════
#  KRUSKAL — Cây khung nhỏ nhất (MST)
# ════════════════════════════════════════════════════════════

class UnionFind:
    """Cấu trúc Union-Find (Disjoint Set) với path compression + union by rank."""

    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank   = {n: 0  for n in nodes}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # cùng thành phần → tạo chu trình
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


def kruskal(nodes, edges):
    """
    Thuật toán Kruskal tìm cây khung nhỏ nhất (MST).

    Trả về:
        mst_edges (list): danh sách cạnh thuộc MST
        total_weight (int): tổng trọng số MST
    """
    sorted_edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(nodes)
    mst_edges = []
    total = 0

    print(f"\n{'='*50}")
    print(f"  KRUSKAL — Cây khung nhỏ nhất (MST)")
    print(f"{'='*50}")
    print(f"Cạnh đã sắp xếp: {[(u,v,w) for u,v,w in sorted_edges]}\n")
    print(f"{'Bước':<6} {'Cạnh':<12} {'Trọng số':<12} {'Kết quả'}")
    print('-' * 50)

    for step, (u, v, w) in enumerate(sorted_edges, 1):
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total += w
            result = '✅ Thêm vào MST'
        else:
            result = '❌ Tạo chu trình — bỏ'
        print(f"{step:<6} {u}—{v:<9} {w:<12} {result}")

        if len(mst_edges) == len(nodes) - 1:
            break

    print('-' * 50)
    print(f"\n🌲 MST gồm {len(mst_edges)} cạnh:")
    for u, v, w in mst_edges:
        print(f"  {u} ── {v}   (w={w})")
    print(f"\n  Tổng trọng số MST = {total}")

    return mst_edges, total


# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("╔══════════════════════════════════════════════════╗")
    print("║   Dijkstra & Kruskal — Demo                      ║")
    print("╚══════════════════════════════════════════════════╝")
    print(f"\nĐồ thị: {len(NODES)} đỉnh, {len(EDGES)} cạnh")
    print(f"Đỉnh : {NODES}")
    print(f"Cạnh : {EDGES}")

    # Dijkstra từ 'A'
    dist, prev = dijkstra(NODES, EDGES, src='A')

    # Kruskal
    mst, weight = kruskal(NODES, EDGES)
