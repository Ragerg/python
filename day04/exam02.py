data = set()
print(f'{data} 원소의 개수 : {len(data)}')
for i in range(10):
    data.add(i+1)

data.add(5) # 중복 x
data.add('5') # 자료형까지 본다

print(f'{data} 원소의 개수 : {len(data)}')
data.remove('5')
print(f'remove("5") 후 {data} 원소의 개수 : {len(data)}')
# data.remove('5') ## 요소가 존재하지 않으면 오류발생
data.discard('5') # 요소가 존재하지 않으면 아무일도 일어나지 않는다
print(f'remove("5") 후 {data} 원소의 개수 : {len(data)}')
data.discard(5)
print(f'remove("5") 후 {data} 원소의 개수 : {len(data)}')

copy = data # 얕은 복사
copy = data.copy() # 깊은 복사
print(f'data : {data}')
print(f'copy : {copy}')
copy.add(5)
print(f'data : {data}')
print(f'copy : {copy}')