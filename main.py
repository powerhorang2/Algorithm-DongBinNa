n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

d = [-1] * 10001
d[0] = 0

start = min(array)
for money in array:
    d[money] = 1

for i in range(start, m + 1):
    for money in array:
        if d[i - money] > 0 and d[i] > 0:
            d[i] = min(d[i], d[i - money] + 1)
        elif d[i - money] > 0 and d[i] < 0:
            d[i] = d[i - money] + 1

print(d[m])
