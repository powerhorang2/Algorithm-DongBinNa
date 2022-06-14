n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0

firstCount = int(m / (k + 1)) * k + m % (k + 1)  # 큰 수가 더해지는 횟수
secondCount = m - firstCount    # 작은 수가 더해지는 횟수

result = first * firstCount + second * secondCount

print(result)
