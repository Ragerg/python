data = list(range(1, 10))
print(data)

data2 = (data[0:5])
print(data)
print(data2)
print(data[5:8])
print(data[:3])
print(data[3:]) # print(data[3:len(data)])
print(data[:])

print(data)
data2 = data
print(data2)
data2[0] = 100
print(data)
print(data2)
