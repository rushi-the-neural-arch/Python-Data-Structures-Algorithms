''''''''

# We create a class called "NODE". In the constructor of this class, 
# we give the argument of self and data. 
# Every node is going to consist of data and next. 
# We define self.data equal to data that is passed into the constructor of the object of class Node 
# We set self.next equal to None.
# This is something that we’ll set again as we make use of the node, 
# but for now, we just set it to None. That’s pretty much all we need for the Node class as of now.

''''''''

class Node(object):

    def __init__(self,data):
        self.data = data
        self.nextNode = None


''''''''

# Here, we define a LinkedList class, and in the constructor, we again pass self. 
# we define the head pointer, which will point to the first node in the linked list. 
# Initially, we just set it equal to None.

''''''''

class LinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = None


    '''''''''''''''

        InsertAtStart Function

    '''''''''''''''

    # Now, we want to insert an element at the beginnig
    def insertAtStart(self,data):
        self.size = self.size + 1       # Increment the size of LinkedList
        newNode = Node(data)            # Pass the data, eg "12" as an object to the 
                                        # Node class, so it will make a new Node

        if not self.head:         # If head is NONE
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
    # So, Time Complexity for Insertion At Beginning is O(1) ! Great




    ''''''''''''''''
        # InsertAfterNode Function

    '''''''''''''''



    #Now, we want to insert after a specific NODE
    def insertAfterNode(self,previousNode,data):
        self.size = self.size + 1
        newNode = Node(data)


        if previousNode is None:
            print("Previous Node doesn't exist")
            return
    
        newNode.nextNode = previousNode.nextNode
        previousNode.nextNode = newNode

    ''''''''
        # In the code above, we create a new method called insert_after_node.
        # It takes self since it is a class method. It also takes prev_node which is the previous node
        # after which we have to insert the new node and data which we’ll use to make the new_node.
    ''''''''



    ''''''''''''''''''''

        #InsertAtEnd Function

    ''''''''''''''''''''


    
    def insertAtEnd(self,data):

        self.size = self.size + 1    # Common Steps as usual, increase the size of LinkedList
        newNode = Node(data)         # & create a new Node by creating an object of Node Class

        #For the insertAtEnd method, we also need to cater for the case 
        # if the linked list is empty.

        if self.head is None:
            self.head = newNode
            return

        #Let’s see what we can do if the linked list is not empty. 
        # We have newNode that we create, and we want to append it to the linked list. 
        # We can start from the head pointer and then move through each of the nodes in the 
        # linked list until we get to the end, i.e. None. Once we arrive at the 
        # location that we want to insert the newNode at, we insert as shown below:
    
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    ''''''''
        #We define actualNode which is initially equal to the head. 
        # This implies we’re at the start of the linked list.
        # We have named the variable we defined as actualNode because that’s what it will 
        # eventually point to. It will start at the beginning of the linked list and 
        # move through the linked list as long as the actualNode.nextNode doesn’t point to None. 
        # We keep moving from node to node  until we get to the actualNode where a
        # ctualNode.next will point to None and will terminate the while loop.
        # After the while loop concludes, actualNode points to the last node. 
        # we input our newNode into the linked list by setting the next of actualNode
        # to new_node which has its own next pointing to None.   
    ''''''''   


    ''''''''''''

        # REMOVE Function

    ''''''''''''''



    def remove(self,data):

        if self.head is None:
            return 

        self.size = self.size - 1

        currentNode = self.head
        previousNode = None
        
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None: # So the data we want to remove is the "Head" Node
            self.head = currentNode.nextNode # Simply update the "Head" to the next node
                                            # so the current node(head) will be removes\d

        else: # So now finally remove the intermediary currentNode
            previousNode.nextNode = currentNode.nextNode 



    # O(1) time complexity
    def size1(self):
        return self.size

    # O(N) time complexity
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        
        return size

    # O(N) Time Complexity



    ''''''''''''''''''''
        # Traverse List Function

    ''''''''''''''''''



      
    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print("%s " % actualNode.data)
            actualNode = actualNode.nextNode

    ''''''

    # print_list is a class method, so it will take self as an argument and 
    # print out the entries of a linked list. We will start from the head pointer 
    # and print out the data component of the node and then move to the next node. 
    # We’ll keep a check on the next node to make sure it is not None. 
    # If it’s not, we move to the next node. This way, we keep printing out data 
    # until we’ve hit the null terminating component of the linked list.

    ''''''


    def print_list(self):

        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.nextNode

linkedlist = LinkedList()

linkedlist.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")
e4 = Node("Fri")
e5 = Node("Sat")

linkedlist.head.nextNode = e2
e2.nextNode = e3
e3.nextNode = e4
e4.nextNode = e5

e_between = "Wed"
#e_between = linkedlist.insertAfterNode(linkedlist.head,"Wed")

e_between = linkedlist.insertAfterNode(linkedlist.head.nextNode,e_between)
e_end = linkedlist.insertAtEnd("Sun")

print(linkedlist.print_list())

print(" .........THE END................ ")


#remove1 = linkedlist.remove(e_end)

#print(linkedlist.print_list())



# If you have only 1 element in the LinkedList then use "InsertAtEnd" function



