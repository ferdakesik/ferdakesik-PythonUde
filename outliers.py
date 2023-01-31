data=[2,3,5,6,7,888,999,77,88,4,21,34,35]

del data[0:2]
print(data)

del data[4:]
print(data)


min_valid=100
max_valid=200

for index , value in enumerate(data):
    if (value<min_valid) or (value>max_valid):
        del data[index]
print(data)