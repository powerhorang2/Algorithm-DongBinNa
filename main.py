data = input()
x = int(data[1])
y = data[0]

dy = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dx = [1, 2, 3, 4, 5, 6, 7, 8]

moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

real_x = dx.index(x)
real_y = dy.index(y)

result = 0

for move in moves:
    mx = real_x + move[0]
    my = real_y + move[1]

    if mx < 0 or my < 0 or mx > 7 or my > 7:
        continue

    result += 1

print(result)
