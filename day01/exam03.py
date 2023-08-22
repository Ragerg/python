# 논리값(True, False)

print(True, False)
print(10 > 3)
print(10 == 3)
print(10 != 3)
print("Hello" == "Hello")
print("Hello" == "hello")
print(1 == 1.0) # 값비교라 True
print(1 is 1.0) # id에 있는 메모리값을 비교하여 False
print(id('Hello'))
print(id('Hello'))
print(id('Hello'))
print(id(1))
print(id(1.0))

print(type(bool(int(str(10))))), print(bool(int(str(10))))
print(bool(1), bool(0), bool(1.5), bool('false')) # 0이 아니면 True
msg = "hello" and "안녕" # and는 뒤에 있는 것 까지 보니까 안녕
msg = "hello" or "안녕" # or은 뒤에 있는 것 안보니까 hello
print(msg)

# 시퀀스 자료형
# list [10,20,30]
# tuple (10,20,30)
# 문자열 'hello' "hello' '''hello''' """hello"""
# range 연속적인 숫자를 생성하게 하는 객체

print('hello')
print('''hello''')
print("""hello
여러 줄도 가능
라인 또 변경""")
