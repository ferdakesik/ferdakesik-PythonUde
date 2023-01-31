
employee_file=open("employess.txt","r")

print(employee_file.readable())

print(employee_file.read())
print(employee_file.readlines())
employee_file.close()