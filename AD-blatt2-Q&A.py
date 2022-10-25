#LINKED LISTS EXERCISES
#----------------------------------------------------------------------
#Each node contains a next and a data entry. You need to specify the start (as a pointer). We use None to erase the pointer!
#E.g. See below code:
class node:
    pass                        #dummy
start = node()
start.next = node()
start.next.next = node()
start.next.next.next = None
#----------------------------------------------------------------------
""" Exercise 2.1
Create a simple list to hold the items 1,2,3,4, creating the list “from the front” as in Slide 70.
[Notice how the list is only complete when you have finished.]
Use the code from Slide 72 to print out your list. (You may want to write this as a function.)"""
class node:
    pass
start = node()
point = start
point.data = 1
print("point: ",point.data)
point.next = node()
point = point.next
point.data = 2
print("point: ",point.data)
point.next = node()
point = point.next
point.data = 3
print("point: ",point.data)
point.next = node()
point = point.next
point.data = 4
print("point: ",point.data)
point.next = None  # None= so we don't "drop off" at end of our list!!!
print("point: ",point.next)
#----------------------------------------------------------------------
"""Exercise 2.2
Create a simple list to hold the items 1,2,3,4 inserting items at the front of the list as in Slide 74.
[Notice how the list is complete after each item is added.]
Use the code from Slide 72 to print out your list. """
class Node:
    pass
start = None            # initialization
tmp = Node()            # make new node
tmp.next = start        # capture the pointer
tmp.data = 1
start = tmp             # ok, now tmp is free again
                        # and the whole list ends neatly in a ’None’
#----------------------------------------------------------------------
""" Exercise 2.3
Create a simple list to hold the items 1,2,3,4 inserting items at the back of the list as in Slide 75 .
[Notice how the list is complete after each item is added.]
Use the code from Slide 72 to print out your list. """
class Node:
    pass
start = None
def insert(entry):
    #print(entry)
    new = Node()                # there will be a node in any case
    new.data = entry            # and this will be its entry
    if not start:               # all none, just return the new node
        new.next = None         # make sure it is grounded
        return new
    point = start               # it’s not None
    while point.next:           # successor exists
        point = point.next      # we are at last Node before the end
    assert point.next == None   # indeed!
    new.next = point.next
    point.next = new
    return start
                                # note: we are manipulating the list beginning at "start"!!
start = insert("a")
start = insert("b")
start = insert("c")
start = insert("d")
point = start
while point:
    print(point.data)
    point = point.next
#----------------------------------------------------------------------
""" Exercise 2.4
The data slot can contain other kinds of information. Create a list to hold the names of your
modules, storing them in alphabetical order.
Use the code from Slide 72 to print out your list. """
class node:
    pass
start = node()
mylist = []
point = start
point.data = "Algorithms and Data Structures"
mylist.append(point.data)
point.next = node()
point = point.next
point.data = "Accessibility and Usability"
mylist.append(point.data)
point.next = node()
point = point.next
point.data = "Database Systems"
mylist.append(point.data)
point.next = node()
point = point.next
point.data = "Principles and Practices of Large-Scale Programming"
mylist.append(point.data)
point.next = None  # None= so we don't "drop off" at end of our list!!!
for i in sorted(mylist):
    print(i)
#----------------------------------------------------------------------
""" Exercise 2.5
Reflect on the three different ways of constructing a list. What are the advantages and disadvantages
of each? (For example, what happens if you try to print each of the lists after adding just two items?)"""

#----------------------------------------------------------------------
""" Exercise 2.6
Now proceed in the following order with Assignments 2.8-2.13. Optional Assignments 2.14 and 2.15 are on doubly-linked lists (but at least try to understand the ideas behind this data structure from the lecture slides). """
#----------------------------------------------------------------------
""" Exercise 2.7
Write a Python function print_list(start) which takes the start pointer of a linked list and prints out the entries, in order. """

#----------------------------------------------------------------------
""" Exercise 2.8
Write a Python function length() which returns the length of the linked list pointed to by start. """

#----------------------------------------------------------------------
""" Exercise 2.9
Write a Python generator nodes(start) that “walks through” the nodes of a linked list given by start. Hint: use yield. """

#----------------------------------------------------------------------
""" Exercise 2.10
Write a Python function insert_at(entry, location) which inserts entry in front of node number location. location should be an integer, starting with 0 for the first node (as per Python/C/Java convention), proceeding with 1, 2, 3 etc. for the subsequent nodes
Note:
    1. If location is just after the last node (i.e. pointing to None), insert at the end of the list.
    2. If location is larger than the length of the list, i.e. it does not exist, raise an error. """
