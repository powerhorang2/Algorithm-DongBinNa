def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return target
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)


n = int(input())
shop = list(map(int, input().split()))
shop.sort()
m = int(input())
customer = list(map(int, input().split()))

for i in customer:
    if binary_search(shop, i, 0, len(shop) - 1) is None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
