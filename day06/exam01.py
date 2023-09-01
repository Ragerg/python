import random
try: # 예외발생
    num = random.randint(0, 3)
    print('추출된 난수 : ', num)
    data = [10, 20]
    print(10/num)
    print(data[2])
# except ZeroDivisionError as e: # 예외처리
#     print('ZeroDivisionError 예외발생!!!', e)
# except IndexError as e: # 예외를 따로 처리할 수 있다
#     print('IndexError 예외발생!!!', e)
except Exception as e: # 어떤 예외가 발생할 지 모를 때 Exception으로 한 번에 받을 수 있다
    print(e)