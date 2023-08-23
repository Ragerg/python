'''
    <list 내장함수>
    append  : 데이터 추가(맨 마지막에)
    insert  : 데이터 추가(특정 위치에)
    pop     : 데이터 삭제(맨 마지막을)
    remove  : 데이터 삭제(특정 데이터를)
    index   : 특정값의 위치 검색
    count   : 특정겂의 빈도수
    reverse : 위치 뒤집기
    sort    : 정렬
    clear   : 리스트 요소 전부 삭제

'''

data = []
print(data, id(data))
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
# delData = data.pop()
delData = data.pop(0) # pop에 인덱스 사용 가능
print('삭제된 값 : ', delData)

data = list()
data.insert(0,10)
data.insert(0,20)
data.insert(0,30)
print(data, id(data))
delData = data.pop()
print('삭제된 값 : ', delData)


data = [10, 20, 30, 40, 30]
idx = data.index(30)
cnt = data.count(30)
print('위치 : ', idx)
print('개수 : ', idx)
print('before : ', data)
data.remove(30)
print('after : ', data)

for i in range(len(data)):
    print(data[i], end=' ')
print()

for d in data:
    print(d, end=' ')
print()

# ite = iter(data)
# print(next(ite))

for d in iter(data):
    print(d, end=' ')
print()

for index, d in enumerate(data, start=100):
    print(f'[{index}] : {d}')

for i in range(1, len(data)+1):
    print(data[-i], end=' ')
print()

data.reverse() # 원본을 수정하여 data 값이 바뀜
for d in iter(data):
    print(d, end=' ')
print()
data.reverse()

# data2 = reversed(data) # 원본 수정 안함
# print('data : ', data)
# print('data2 : ', next(data2))
for d in reversed(data):
    print(d, end=' ')
print()

# data.sort()
# print(data)
print(sorted(data, reverse=True)) # reverse=True 내림차순, reverse=False 오름차순(default)
print(data)

data = [10, 20, 30]
# for i in range(len(data)):
#      data.pop(0)
# data.clear()
del data[:]
print(data)

