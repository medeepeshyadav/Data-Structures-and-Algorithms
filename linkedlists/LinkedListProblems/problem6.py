#Problem: insert an element in a sorted linked list

# a code to implement singly linked list

class Node:
    def __init__(self, data):
        """Function to initialize node"""
        self.data = data    #defining data field of node
        self.next = None    #defining next as NULL

class SLinkedList:

    def __init__(self):
        """Initializing LinkedList"""
        self.head = None
        self.length = 0

    def insert_at_beg(self, newdata):
        """Insertion at beginning"""
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode
        self.length +=1

    def insert_at_end(self, newdata):
        """Inserts data at the end of the list same as Append"""
        newNode = Node(newdata)         #make node object with data
        
        #if list is empty, that is Head is None
        if self.head == None:           #if head is None
            newNode.next = self.head
            self.head = newNode         #make newNode as HEAD
            self.length+=1

        #else traverse to the very last node and set its next as newNode
        else:
            current = self.head            #initialize last as head
            while current.next != None:    #check last.next is None, if its None break the loop
                current = current.next        #update last to next
            
            current.next = newNode             #when last.next == None, set last.next as newNode
            self.length +=1

    def insert_at(self,pos,newdata):
        """Insert data at given position"""

        if pos > self.length or pos < 0:        #if pos is > listLength or < 0 : please insert valid pos
            print("Please insert valid position!")
        else:
            if pos == 0:                        #if pos = 0; call insert_at_beg()
                self.insert_at_beg(newdata)
            elif pos == (self.length):          #if pos = listLength; call insert_at_end()
                self.insert_at_end(newdata)

            else:                               #else
                newNode = Node(newdata)         #create a new node
                count = 0                       #initialize count
                current = self.head             #start counting from HEAD
                while count < pos-1:            #keep counting till pos-1
                    count +=1
                    current = current.next

                #at count == pos-1
                newNode.next = current.next     #make current_node's next as newNode's next
                current.next = newNode          #make current_node's next as newNode
                self.length +=1                 #increament lenght by one


    def delete_from_beg(self):           
        """Deletes element from beginning"""       
        if self.head is None:
            print("List is Empty")
        else:
            head = self.head                
            self.head = head.next               #promote next node to HEAD
            del head                            #delete previous HEAD

        self.length -= 1                        #decrease length by one

    def delete_from_end(self):
        last = self.head                        #begin from HEAD
        if last.next is None:
            self.head = None                    #delete the head node
            print("List is Empty")
            del last

        else:
            prev = None
            while last.next != None:            #traverse the list till last node
                prev = last                     #store second last node
                last = last.next                #store last node
            prev.next = None                    #make second last node as Last by setting its next None
            del last                            #delete last node

        self.length -=1

    def delete_at(self,pos):
        if pos> self.length or pos<0:                   #if pos > listLength or < 0 
            print("Please enter valid position")        #please enter valid position

        else:     
            if pos == 0:                        #if pos == 0; call delete_from_beg()
                self.delete_from_beg()

            elif pos == self.length:            #if pos == listLength; call delete_from_end()
                self.delete_from_end()

            else:
            #delete at middle
                count = 0                       #initialize count
                current = self.head             #begin count from HEAD
                prev = None                     #prev node
                
                while count < pos:              #keep counting till pos             
                    count +=1                   
                    prev = current              #store current as prev
                    current = current.next      #store current's next as current
                    
                #at count == pos
                prev.next = current.next        #make current_node's next as prev_node's next
                del current                     #delete current node
                self.length -= 1                #decreament length by one

    def listlength(self):
        """calculates the length of the linked list"""

        current = self.head             #set current node as HEAD
        count = 0                       #initialize count
        while current != None:          #run the loop till the current node is None
            count +=1
            current = current.next      #update current node to next node
        print("length of list:", count)                    #print the length

    def printlist(self):
        """prints the list"""
        if self.head == None:
            print("List is Empty")
        current = self.head             #set current node as HEAD
        while current != None:          #run the loop till the current node is None
            print(current.data)         #print the data in the node
            current = current.next      #update node to next node

    def insert_inorder(self,data):
        """Book Method"""
        #inserts the data in order
        newNode = Node(data)
        if self.head == None:
            self.insert_at_beg(data)

        else:
            current = self.head
            prev = None
            stop = False
            while current != None and not stop:
                if current.data > data:
                    stop = True
                else:
                    prev = current
                    current = current.next
            newNode.next = current
            prev.next = newNode
                
            self.length +=1
            
    def insert_in_order(self, el):
        """My method: traverse till the current.data < data, and hold the previous node too"""
        newNode = Node(el)
        if self.head == None:
            newNode.next = self.head
            self.head = newNode
        
        else:
            current = self.head
            prev = None
            while current.data < el:
                prev = current
                current = current.next
            prev.next = newNode
            newNode.next = current
            self.length +=1
            return

list = SLinkedList()
print(list.head)
list.insert_at_end(20)
list.insert_at_end(30)
list.insert_at_end(40)
list.insert_at_end(50)
list.insert_at_end(70)
list.insert_at_end(80)
list.insert_at_end(90)
list.insert_at_end(100)
list.printlist()
print("-"*80)
list.insert_in_order(60)
list.printlist()