# 초기 캐릭터의 위치 characterX, characterY
# 아이템의 위치 itemX, itemY
# rectangle: [[왼쪽 아래 꼭짓점, 오른쪽 위 꼭짓점]]
from collections import deque

def bfs(graph, cx, cy, tx, ty, visited):
    queue = deque([[cx, cy]])
    visited[cx][cy] = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        if x == tx and y == ty:
            break
        for i in range(4):
            if graph[x+dx[i]][y+dy[i]] == 2 and visited[x+dx[i]][y+dy[i]] == 0:
                queue.append([x+dx[i], y+dy[i]])
                visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1
                # print(visited[x+dx[i]][y+dy[i]])
        
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 빈칸: 0 면:1 선:2
    graph = [[0 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]
    
    # 영역 채우기
    # 라인이 겹치는 경우를 위해 두 배로 계산
    for rec in rectangle:
        x1, y1, x2, y2 = rec[0]*2, rec[1]*2, rec[2]*2, rec[3]*2   
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                graph[x][y] = 1
        
    # 테두리 찾기
    # 상하좌우 뿐만 아니라 대각선까지 모두 체크
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, 1, -1, -1]
    for x in range(102):
        if 1 not in graph[x]:
            continue
        for y in range(102):
            if graph[x][y] == 1:
                line = False
                for i in range(8):
                    if graph[x+dx[i]][y+dy[i]] == 0:
                        line = True
                        break
                if line:
                    graph[x][y] = 2
    
    # 그래프 확인
    # for i in graph[:21]:
    #     print(i[:21])
    
    # bfs 호출
    bfs(graph, characterX*2, characterY*2, itemX*2, itemY*2, visited)
    answer = visited[itemX*2][itemY*2] // 2 
    return answer