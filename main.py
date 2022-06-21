array = ['기린5', '사자3', '고래1', '호랑이0', '고양이2', '펭귄6']


def setting(data):
    return data[-1]


array.sort(key=setting)
print(array)
