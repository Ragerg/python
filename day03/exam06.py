members = {'홍길동':'32거2345', '고길동':'26소2756', '윤길동':'89나2134'}

# 홍길동의 차량번호 검색
print(members.get('홍길동'))

# 차량번호 26소2756의 차주 검색
# 1. 보통
# for key, value in members.items():
#     if value == '26소2756':
#         print(key)
#         break

# 2. key랑 value를 서로 바꾸기
mem = {value:key for key, value in members.items()}
print(mem.get('26소2756'))

# 3.
data = [key for key, value in members.items() if value == '26소2756']
print(data[0])