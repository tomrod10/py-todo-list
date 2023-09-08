list = []

def add_todo(description):
    list.append({"id": len(list) + 1, "desc": description})

# While loop set to True
# Break when user wants to quit the app
while True:
    if len(list) == 0:
        print("Todo list is empty!")
    else:
        for i in range(len(list)):
            print("[ ]", list[i]["id"], "-", list[i]["desc"])
    
    choice = input("Do you want to (Add/Edit/Toggle/Delete/Exit)? ").capitalize()
    if choice in ("Add", "Edit", "Toggle", "Delete", "Exit"):
        if choice == "Add":
            description = input("Write your todo (50 chars max): ")[:50].strip()
            add_todo(description)
        elif choice == "Exit":
            print("\n Goodbye!")
            break
    else:
        print("Invalid option. Try again!")
