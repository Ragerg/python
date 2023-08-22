data = [10, 20, 30 ,40, 'hello'] # 같은 자료형들의 집합이 아니어도 됨
print(type(data), data)
data = list()
print(type(data), data)

data = (10, 20, 30, 40)
print(type(data), data)
data = tuple()
print(type(data), data)

# data = 10 ## <class 'int'>
data = 10, 20 # data = (10, 20) <class 'tuple'>
print(type(data), data)

# range(시작=기본값 0, 종료, step=기본값 1)
data = range(10) # range(0, 10) 0~9 10개의 숫자를 생성하라
print(type(data), data)
data = list(data)
print(data)

data = range(5, 15)
print(list(data))

data = list(range(1, 10, 2))
print(data)

data = list(range(20, 4, -3))
print(data)

# list 에 쓰는 연산자
# in 그 데이터가 있는지 없는지 판단할 때 쓰는 연산자, 시퀀스 자료형에 다 쓸 수 있다
# [ : ] 슬라이스 / 임의로 잘라내기
print(16 in data, 17 in data)
print('e' in 'Hello')
print(10 in range(10))