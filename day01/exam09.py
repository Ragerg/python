import random

num01, num02 = map(int, input('두 개의 정수를 입력 : ').split())
r = random.randrange(num01, num02+1)
print(r)

for i in range(r):
    j = i+1
    cnt3 = str(j).count('3')
    cnt6 = str(j).count('6')
    cnt9 = str(j).count('9')
    cnt = cnt3 + cnt6 + cnt9

    if j % 10 == 0:
        print('뽀' * (j // 10) + '숑' + '짝' * cnt, end=' ')
    elif cnt > 0:
        print('짝' * cnt, end=' ')
    else:
        print(j, end= ' ')
