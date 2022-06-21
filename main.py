n, k = map(int, input().split())    # N과 K를 입력받기
array_a = list(map(int, input().split()))   # 배열 A의 모든 원소를 입력받기
array_b = list(map(int, input().split()))   # 배열 B의 모든 원소를 입력받기

array_a = sorted(array_a)   # 배열 A는 오름차순 정렬 수행
array_b = sorted(array_b, reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if array_a[i] < array_b[i]:
        # 두 원소를 교체
        array_a[i], array_b[i] = array_b[i], array_a[i]
    else:   # A의 원소가 B의 원소보다 크거나 같을 때, 더 이상 교체 할 원소가 없으므로 반복문 탈출
        break

print(sum(array_a)) # 배열 A의 모든 원소의 합을 출력
