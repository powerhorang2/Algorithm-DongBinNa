n, k = map(int, input().split())
count = 0

while True:
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    print("count: ", count)
    print("n: ", n)
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        print("break")
        break
    # K로 나누기
    count += 1
    n //= k
    print("count: ", count)
    print("n: ", n)

count += (n - 1)
print("end: ", count)