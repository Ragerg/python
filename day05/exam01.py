# def myPrint(*values, end='>>', sep='\t'):
#     for value in values:
#         print(value, end=end)
#
# myPrint(10, end='\n')
# myPrint(10, 'A')
# myPrint((10, 20, 30, 40), [100, 200, 300, 400])

def calc(commend, *args):
    s = 0 if commend == 'add' else 1
    for value in args:
        if commend == 'add':
            s += value
        elif commend == 'mul':
            s *= value
    return s


print(calc('add', 12, 7))
print(calc('add', 12, 6, 9))
print(calc('mul', 12, 7))
print(calc('mul', 1, 2, 3, 4, 5))

## 고민해보자
# print(calc('add', 12, [6, 9, 10]))
