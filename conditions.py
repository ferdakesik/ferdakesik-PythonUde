age=int(input("how old are you"))

# #if age >=16 and age <= 65:
# if 16<=age<=65:
#     print("have a good day at work")
# else:
#     print("enjoy your free time")

print("_"*80)

if age<16 or age >65:
    print("enjoy your free time")
else:
    print("you are younger than 16")

print()

if age in range (16,66):
    print("enjoy your free time")
else:
    print("you are younger than 16")

