import random
try:
    num = random.randint(0, 2)
    result = 10/num
except Exception as e:
    print('예외발생! : ', e)
    pass
else: # 예외가 발생하지 않았을 때 수행하는 문장
    print(f'10/{num} = {result}')
finally:
    print('프로그램 종료...')