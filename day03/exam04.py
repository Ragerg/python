members = {'홍길동':'1111-2222','박길동':'3333-4444', '윤길동':'5555-6666'}

print(f'홍길동 존재여부 : {"홍길동" in members}') # key값으로 존재여부를 확인
print(f'1111-2222 존재여부 : {"1111-2222" in members}') # value 값으로는 확인 안됨

print(members.keys())
print(members.values())
print(members.items()) # key, value를 tuple로

for data in members:
    # print(data, end=' ') # data는 key를 의미
    print(f'{data} : {members.get(data)}')
print()

for data in members.keys():
    print(data, end=' ')
print()

for data in members.values():
    print(data, end=' ')
print()

for key, value in members.items():
    print(f'{key} : {value}')
print()

keys = ['name', 'age', 'addr']
mem = dict.fromkeys(keys, "") # key 리스트를 통해서 딕셔너리 생성 가능
print(mem)
