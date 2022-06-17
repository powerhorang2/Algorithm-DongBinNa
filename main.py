n, m = map(int, input().split())
a, b, direction = map(int, input().split())

visited = [[0] * m for _ in range(n)]
visited[a][b] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
steps = [0, 1, 2, 3]

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))


def turn_direction():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:

    turn_direction()
    nx = a + dx[direction]
    ny = b + dy[direction]

    if array[ny][nx] == 0 and visited[nx][ny] == 0:
        visited[a][b] = 1
        a, b = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = a - dx[direction]
        ny = b - dy[direction]
        if array[nx][ny] == 1:
            break
        else:
            a = nx
            b = ny
            turn_time = 0

print(count)
