def action(choice):
    if choice == "Add":
        description = input("Write your todo (50 chars max): ")[:50].strip()
        add_todo(description)
    elif choice == "Edit":
        todo_num = int(input("What todo number do you want to edit? "))
        edit_todo(todo_num)
    elif choice == "Toggle":
        todo_num = int(input("What todo number do you want to toggle? "))
        toggle_todo(todo_num)

list = []

def is_in_list(num):
    return True if (num > len(list) or len(list) < 1) else False

def add_todo(description):
    list.append({"id": len(list) + 1, "desc": description, "status": False})

def edit_todo(num):
    if is_in_list(num) or len(list) == 0:
        print("**Invalid entry. Try again!**")
        return
    edit = input("Write your edited todo: ")
    list[num - 1]["desc"] = edit
    print("Todo", num, "has been edited")

def toggle_todo(num):
    if is_in_list(num) or len(list) == 0:
        print("**Invalid entry. Try again!**")
        return
    list[num - 1]["status"] = not list[num - 1]["status"]
    print("Todo", num, "has been toggled")
    

while True:
    if len(list) == 0:
        print("Todo list is empty. Add a todo!")
    else:
        for i in range(len(list)):
            status = "[x]" if list[i]["status"] else "[ ]"
            print(status, list[i]["id"], "-", list[i]["desc"])
    print("\n")
    
    choice = input("Do you want to (Add/Edit/Toggle/Delete/Exit)? ").capitalize()
    if choice in ("Add", "Edit", "Toggle", "Delete", "Exit"):
        if choice == "Exit":
            print("\nGoodbye!")
            break
        action(choice)
    else:
        print("Invalid option. Try again!")
