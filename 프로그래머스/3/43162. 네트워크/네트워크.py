def build_graph(n, computers):
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
    return graph

def solution(n, computers):
    graph = build_graph(n, computers)
    visited = [False] * n
    count = 0

    def dfs(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)

    for node in range(n):
        if not visited[node]:
            dfs(node)
            count += 1

    return count