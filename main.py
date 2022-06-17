input_data = input()
row = int(input_data[1])
# 문자를 유니코드 정수로 변환하고 문자 'a'의 유니코드 정수를 빼면 a 부터 0 이되는데 거기에 1을 더하는 테크닉 - 그럼 문자 a 는 정수 1이 된다.
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

result = 0

for step in steps:
    # 이동 후 위치 파악
    next_row = row + step[0]
    next_column = column + step[1]

    # 이동 후 나이트의 위치가 8 X 8 정원안이면 카운트 증가
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1

print(result)
