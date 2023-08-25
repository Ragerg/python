str = 'Hello, World'
print(str, str.upper(), str.lower()) # 원본 데이터가 바뀌는 것은 아님
strList = str.split(',')
print(strList)
str2 = '/'.join(strList)
print(str2)
print(f'[{strList[1].lstrip()}]')

str = ' !    Hello World       '
print((f'str : [{str}]'))
print(f'lstrip() : [{str.lstrip(" !")}]')
print(f'rstrip() : [{str.rstrip()}]')
print(f'strip() : [{str.strip("! ")}]')

str = 'hello'
print(f'str : [{str}]')
print(f'str : [{str.center(11)}]') # 가운데 정렬
print(f'str : [{str.center(10)}]')
print(f'str : [{str.ljust(10)}]') # 왼쪽 정렬
print(f'str : [{str.rjust(10)}]') # 오른쪽 정렬
print(f'str : [{str.zfill(10)}]') # 오른쪽 정렬, 공백에 0

str = "Hello World!!"
print(f'"o"의 위치 : {str.index("o")}') # 처음 있는 "o" 위치
print(f'"o"의 위치 : {str.index("o", 6)}') # 시작위치 6에서 부터 "o" 위치
# print(f'"p"의 위치 : {str.index("p")}') # 문자열이 없는 경우 예외발생
print(f'"p"의 위치 : {str.find("p")}') # 문자열이 없는 경우 -1 반환
print(f'"o"의 위치 : {str.rfind("o")}')
print(f'"l"의 개수 : {str.rfind("l")}')
print(f'"l" => "rr" : {str.replace("l","rr")}')
