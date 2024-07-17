from collections import deque  # BFS 문제 풀이 위해 필요한 함수

# 입력 자동화
inputs = [
    {
        "n_m": [4, 6],
        "gh": [
            [1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1]
        ]
    }
]

# ----------------------------------------------------------------
# DFS 문제 풀이

printlist = []

# 상하좌우 이동 표시
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# ※핵심※ DFS 동작 함수


def dfs(x, y, n, m, gh, vt, path):
    path.append((x, y))  # 기록 저장
    for i in range(4):  # 현 위치 상하좌우 이동
        nx, ny = x + dx[i], y + dy[i]

        # 이동한 현 위치가 그래프의 범위 내에 있는가, 해당 노드의 값이 1인가 확인
        if 0 <= nx < n and 0 <= ny < m and gh[nx][ny] == 1:

            # 처음 방문 or 이전 방문 수보다 적게 방문 가능 시 해당 노드 닫고 방문 횟수 업데이트
            if vt[nx][ny] == 0 or vt[nx][ny] > vt[x][y] + 1:
                vt[nx][ny] = vt[x][y] + 1

                if nx == n-1 and ny == m-1:  # 도착점 도달, 함수 종료 및 데이터 저장
                    return path

                else:  # 도착점 미도달시, 현 위치에서 다시 DFS 수행.
                    return dfs(nx, ny, n, m, gh, vt, path)

    return path


for input in inputs:
    n, m = input["n_m"]
    gh = input["gh"]
    vt = [[0] * m for _ in range(n)]  # n * m 크기의 2차원 리스트를 생성
    vt[0][0] = 1  # vt는 각 노드를 방문한 횟수 저장.
    path = []

    dfs(0, 0, n, m, gh, vt, path)
    printlist.append(vt[n-1][m-1])

print(printlist)
print(path)

# ----------------------------------------------------------------
# BFS 문제 풀이

printlist = []

# 상하좌우 이동 표시
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# ※핵심※ BFS 동작 함수


def bfs(x, y, n, m, gh, vt):
    q = deque([(x, y)])  # 탐색을 시작할 노드를 큐에 추가
    vt[x][y] = 1  # 시작 노드를 방문표시
    path = [(x, y)]  # 기록 저장

    while q:  # 큐가 빌 때까지 탐색
        x, y = q.popleft()  # 큐에서 노드를 하나 꺼냄
        for i in range(4):  # 해당 노드에서 상하좌우로 이동
            nx, ny = x + dx[i], y + dy[i]

            # 이동한 위치가 그래프의 범위 내에 있고, 해당 노드의 값이 1인지 확인
            if 0 <= nx < n and 0 <= ny < m and gh[nx][ny] == 1:

                # 처음 방문 or 이전 방문 수보다 적게 방문 가능 시 해당 노드 닫고 방문 횟수 업데이트
                if vt[nx][ny] == 0 or vt[nx][ny] > vt[x][y] + 1:
                    q.append((nx, ny))
                    vt[nx][ny] = vt[x][y] + 1
                    path.append((nx, ny))

    # 도착점까지의 최단 거리를 반환
    return path


for input in inputs:
    n, m = input["n_m"]
    gh = input["gh"]
    vt = [[0] * m for _ in range(n)]
    path = bfs(0, 0, n, m, gh, vt)

printlist.append(vt[n-1][m-1])

print(printlist)
print(path)
