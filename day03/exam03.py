members = {'홍길동':'010-1111-2222', '박길동':'010-3333-4444'}
print(members)
members.setdefault('윤길동', '010-5555-6666') # 추가
members.setdefault('이길동') # value값이 없으면 None이 들어간다
print(members)
members.setdefault('이길동', '010-7777-8888') # 수정안됨 : setdefault는 새로운 데이터를 삽입할 때만 사용된다
print(members)
members.update(이길동='010-7777-8888') # 기존데이터 수정 (key값이 존재하면)
members.update(한길동='010-9999-0000') # 새로운 데이터 추가도 가능 (key값이 없으면) / key값이 문자열만 가능하다
members.update({2023082501:'010-2345-6789'}) # 키값이 문자열이 아닌경우 -> 1. 딕셔너리 형태로 삽입이 가능
members.update([[2023082502, '010-1234-5678'], ['고길동','010-4567-8901']]) # 2. 2차원 리스트 형태로 삽입 가능
members.update(zip(['park', '윤길동'], ['8282', None])) # 3. zip객체 형태로 삽입 가능
print(members)

value = members.pop('이길동')
print(f'pop("이길동") : {value}')
# members.pop('구길동') # key가 없으면 에러
value = members.pop('구길동', "없음") # key가 없으면 return하려는 값을 "없음"으로 지정
print(f'pop("구길동") : {value}')
print(members)

members.popitem() # 맨 마지막 항목 제거 후 반환
print(members)

value = members.get('홍길동')
print(f'홍길동 : {value}')
print(f'이길동 : {members.get("이길동", "존재하지 않음")}')
