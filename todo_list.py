"""
Requirements:
-Each todo list item will have a max input of 50 chars
-Each todo list item will have a "Completed" box
    -i.e. [x] for completed and [ ] for incompleted
-Each todo item will have number associated

-Ask user to "Do you want to (Add/Edit/Delete/Toggle) todo? "
-Strip spaces
-User input should not be case-sensitive

Add:
-If todo list length is 15 prevent user from adding
    -Print "You have too many todos! Consider finishing some first!"
-Add todo to end of list
-Status should be incomplete

Edit:
-Ask user "What todo # do you want to edit? "
-Turn input into int
-Find the todo in the list with index (input # - 1)
-Ask user to input todo info
-Once todo has been edited print "Todo # has been edited"

Delete:
-Ask user "What todo # do you want to delete? "
-Turn input into int
-Find the todo in the list with index (input # - 1)
-Delete todo
-Print "Todo # has been deleted"

Toggle:
-Ask user "What todo # do you want to toggle? "
-Toggle todo status box
-Print "Todo # has been toggled"

Displaying list:
-Loop over list
"""