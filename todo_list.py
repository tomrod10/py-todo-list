def action(choice):
    if choice == "Add":
        description = input("Write your todo (50 chars max): ")[:50].strip()
        add_todo(description)
        return
    
    todo_num = int(input(f"What number do you want to {choice.casefold()}: "))
    if is_in_list(todo_num) or len(list) == 0:
        print("**Invalid entry. Try again!**")
        return
    elif choice == "Edit":
        edit_todo(todo_num)
    elif choice == "Toggle":
        toggle_todo(todo_num)
    elif choice == "Delete":
        delete_todo(todo_num)

list = []

def is_in_list(num):
    return True if (num > len(list) or len(list) < 1) else False

def get_todo_status(status):
    return "[x]" if status else "[ ]"

def add_todo(description):
    list.append({"id": len(list) + 1, "desc": description, "status": False})

def edit_todo(num):
    edit = input("Write your edited todo: ")
    list[num - 1]["desc"] = edit
    print(f"Todo {num} has been edited")

def toggle_todo(num):
    list[num - 1]["status"] = not list[num - 1]["status"]
    
def delete_todo(num):
    index = num - 1
    del list[index]
    for x in range(index, len(list)):
        list[x]["id"] = x+1

while True:
    if len(list) == 0:
        print("Todo list is empty. Add a todo!")
    else:
        for i in range(len(list)):
            status = get_todo_status(list[i]["status"])
            print(f"{status} {list[i]['id']} - {list[i]['desc']}")
    print("\n")
    
    choice = input("Do you want to (Add/Edit/Toggle/Delete/Exit)? ").capitalize()
    if choice in ("Add", "Edit", "Toggle", "Delete", "Exit"):
        if choice == "Exit":
            print("\nGoodbye!")
            break
        action(choice)
    else:
        print("Invalid option. Try again!")
