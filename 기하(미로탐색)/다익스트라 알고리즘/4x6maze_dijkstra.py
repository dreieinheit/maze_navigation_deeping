import heapq


def dijkstra(gh, start, end):
    n, m = len(gh), len(gh[0])
    distances = [[float('inf')] * m for _ in range(n)]
    distances[start[0]][start[1]] = 1
    queue = [(1, start)]
    prev = [[None] * m for _ in range(n)]  # 이전 노드를 저장하는 2차원 배열

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        current_distance, (x, y) = heapq.heappop(queue)

        if (x, y) == end:
            path = []
            while end is not None:
                path.append(end)
                end = prev[end[0]][end[1]]
            path.reverse()
            return current_distance, path

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and gh[nx][ny] == 1:
                next_distance = current_distance + 1

                if next_distance < distances[nx][ny]:
                    distances[nx][ny] = next_distance
                    prev[nx][ny] = (x, y)
                    heapq.heappush(queue, (next_distance, (nx, ny)))

    return -1, []  # 경로가 없는 경우


gh = [
    [1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1]
]
start = (0, 0)
end = (3, 5)

distance, path = dijkstra(gh, start, end)
print("최단 거리:", distance)
print("경로:", path)
