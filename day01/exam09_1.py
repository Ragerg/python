import random

num = random.randint(20, 50)
print(f'추출된 난수 : {num}')

print('< 369게임 시작!!!>')
for i in range(1, num+1):
    n1 = i % 10
    n10 = i //10

    print(f'{i:>3}', end=' ') # f'{i:>3}' 3자리 오른쪽 정렬
    if not n1:
        print('뽀' * n10, '숑', end=' ')
    if n1 in [3,6,9]:
        print('짝', end=' ')
    if n10 in [3,6,9]:
        print('짝', end=' ')
    print()