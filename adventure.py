available_exits = ["norths","south","east","west"]

chosen_exist = ""

while chosen_exist not in available_exits:
    chosen_exist = input("please choose a direction: ")
    if chosen_exist.casefold == "quit":
        print("game over")
        break
print("aren't you glad you got out of there")

