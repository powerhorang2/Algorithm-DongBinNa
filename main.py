# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    # 시작 인덱스가 끝 인덱스보다 작거나 같을 때 반복
    while start <= end:
        mid = (start + end) // 2
        # 타겟을 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 타겟이 중간점의 값보다 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 타겟이 중간점의 값보다 큰 경우 오른쪽 확인
        elif array[mid] < target:
            start = mid + 1
    return None


# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
shop = list(map(int, input().split()))
shop.sort()  # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
customer = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in customer:
    # 해당 부품이 존재하는지 확인
    result = binary_search(shop, i, 0, n - 1)
    if result is None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
