list = [{"id": 10, "desc": "wash car"}]

# While loop set to True
# Break when user wants to quit the app
if len(list) == 0:
    print("Todo list is empty!")
else:
    for i in range(len(list)):
        print("[ ]", list[i]["id"], "-", list[i]["desc"])

