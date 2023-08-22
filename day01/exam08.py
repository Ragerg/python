'''
    *
    **
    ***
    ****
    *****
'''
for i in range(5):
    print('*' * (i+1))
print()

for i in range(9):
    if i < 5:
        print('*' * (i+1))
    else:
        print('*' * (9-i))
print()

for i in range(9):
    # 파이썬 조건연산자 : 참문장 if 조건식 else 거짓문장
    cnt = (i+1) if i < 5 else (9-i)
    print('*' * cnt)
print()

for i in range(5):
    print(' ' * i, end='')
    print('*' * (5-i))
print()