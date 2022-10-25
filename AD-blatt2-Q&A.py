Exercise 2.1
Create a simple list to hold the items 1,2,3,4, creating the list “from the front” as in Slide 70.
[Notice how the list is only complete when you have finished.]
Use the code from Slide 72 to print out your list. (You may want to write this as a function.)

Exercise 2.2
Create a simple list to hold the items 1,2,3,4 inserting items at the front of the list as in Slide 74.
[Notice how the list is complete after each item is added.]
Use the code from Slide 72 to print out your list.

Exercise 2.3
Create a simple list to hold the items 1,2,3,4 inserting items at the back of the list as in Slide 75 .
[Notice how the list is complete after each item is added.]
Use the code from Slide 72 to print out your list.

Exercise 2.4
The data slot can contain other kinds of information. Create a list to hold the names of your
modules, storing them in alphabetical order.
Use the code from Slide 72 to print out your list.

Exercise 2.5
Reflect on the three different ways of constructing a list. What are the advantages and disadvantages
of each? (For example, what happens if you try to print each of the lists after adding just two items?)
Now attempt Assignment 2.7 below. Save your function in a file called “list_print.py”. Return
to your file “week-x-examples.py”.
Check that the print list function works on all your example lists.

Exercise 2.6
Now proceed in the following order with Assignments 2.8-2.13. Optional Assignments 2.14 and 2.15
are on doubly-linked lists (but at least try to understand the ideas behind this data structure from
the lecture slides).

Exercise 2.7
Write a Python function print_list(start) which takes the start pointer of a linked list and
prints out the entries, in order.

Exercise 2.8
Write a Python function length() which returns the length of the linked list pointed to by start.

Exercise 2.9
Write a Python generator nodes(start) that “walks through” the nodes of a linked list given by
start.
Hint: use yield.

Exercise 2.10
Write a Python function insert_at(entry, location) which inserts entry in front of node number
location. location should be an integer, starting with 0 for the first node (as per Python/C/Java
convention), proceeding with 1, 2, 3 etc. for the subsequent nodes
Note:
1. If location is just after the last node (i.e. pointing to None), insert at the end of the list.
2. If location is larger than the length of the list, i.e. it does not exist, raise an error.
