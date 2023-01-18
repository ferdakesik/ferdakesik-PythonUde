letters="abcdefghijklmnopqrstuvwxyz"
#        01234567890123456789012345

backwards=letters[25:0:-1]
print(backwards)

#create a slice that produces the characters qpo
print(letters[16:13:-1])

#slice the string to produce edcba

print(letters[4::-1])

#slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])

print(letters[-1:])
print(letters[-4:])