from collections import deque

def bfs(n, start, computers, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        network = []       # 현재 노드와 연결된 노드들 중 방문되지 않은 노드들
        for i in range(n):
            if v != i and computers[v][i] == 1 and not visited[i]:
                network.append(i)
        for i in network:
            queue.append(i)
            visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            bfs(n, v, computers, visited)
            answer += 1
    return answer