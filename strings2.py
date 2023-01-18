parrot ="Norwegian Blue"

# print(parrot)
# print(parrot[3])

# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

# print()

# print(parrot[-1])

# print(parrot[-3])
# print(parrot[-4])
# print(parrot[-9])
# print(parrot[-3])
# print(parrot[-6])
# print(parrot[-8])

# print()

# print(parrot[3-14])
# print(parrot[4-14])
# print(parrot[9-14])
# print(parrot[3-14])
# print(parrot[6-14])
# print(parrot[8-14])

print(parrot[0:6]) 
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[0:-1])

print(parrot[:])

print()

print(parrot[0:6:2])# sifirdan 5 e kadar , her iki atla
print(parrot[0:6:3])#sifirdan basla 5 e kadar, 3 atla NW

number="9,223:372;036 854,775;807"
print(number[1::4])# 1 den basla sona kadar 4 atla
print()

seperators=""

for char in number:
    if not char.isnumeric():
        seperators=seperators+char
print(seperators)


values="".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])












