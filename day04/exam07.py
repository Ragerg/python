'''
def 함수([인자, 인자, ...]):
    문장
    문장
    ...
    return
'''
def add(a, b):
    return a + b
def sub(a, b):
    return  a - b

def mul(a, b):
    return  a * b

def div(a, b):
    return a / b

print(f'덧셈 : {add(12, 7)}')
print(f'뺄셈 : {sub(12, 7)}')
print(f'곱셈 : {mul(12, 7)}')
print(f'나누기 : {div(12, 7)}')

def calculate(a, b):
    return add(a, b), sub(a, b), mul(a, b), div(a, b) # tuple 형태로 return

print(f'사칙연산 : {calculate(12, 7)}')

# unpacking
a, b, c, d = line = calculate(12, 7)
