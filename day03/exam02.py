data = {'hong':1111, 'kang':2222, 'han':3333, 'park':4444, 'kang':5555, 100:'max'}
print(data, type(data))

stuInfo = {'name': 'hong', 'age': 28, 'scores':[100, 100, 70]}
print(stuInfo)

data = {}
data = dict()
data = dict(name='hong', age=28, addr='seoul') # key=value 에서 key는 문자열만 가능(''은 안써도 됨)
data = dict([('name', 'hong'), ('age', 28),('addr', 'seoul'), (100, 'max')])
data = dict(zip(['name', 'age', 'addr'],['hong', 28, 'seoul'])) # zip 객체를 딕셔너리 형태로
# print(zip(['name', 'age', 'addr'],['hong', 28, 'seoul'])) # zip 객체가 따로 있음
print(data, type(data))
