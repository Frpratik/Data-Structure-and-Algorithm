#creating a linkedlist=====================================================
#creating a node====
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#initiating linkedlist======
class Linkedlist():
    def __init__(self):
        self.head = None

    #adding element at last in linkedlist=======
    #Q.appending the element in linkedlist===============
    # def appendelement(self,data):
    #     new_node = Node(data)
    #     if not self.head:
    #         self.head = new_node
    #     else:
    #         current = self.head
    #         #traversing until last element
    #         while current.next:
    #             current = current.next
    #         current.next = new_node

    #adding element at first in linkedin========
    #Q.prepending the element in linkedlist========
    # def prependelement(self,data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node

    #Q.adding element at given position=======
    def addelementatpos(self,data,pos):
        new_node = Node(data)

        if pos < 0:
            print('Invalid position=============')
            return 
        
        if pos == 0:
            new_node.next = self.head 
            self.head = new_node
            return

        current = self.head
        count = 0
        ind = pos - 1
        while current and count < ind:
            current = current.next
            count += 1

        if not current:
            print("Position out of bounds!============")
            return

        new_node.next = current.next
        current.next = new_node

    #Q.length od singly linked list============
    def lenoflist(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        print(count)
        return

    #Q.removing element by value from linkedlist=========
    def removeelebyval(self,val):
        current = self.head

        if not current :
            print("List is empty=====")
            return
         
        #if value found at head
        if current.data == val:
            self.head = current.next
            current = None
            return
        
        #for tracking prev element
        prev = None

        #traversing until value found
        while current and current.data != val:
            prev = current
            current = current.next

        if not current:
            print("value doesnt exists in list=======")
            return

        #once value found linking prev emenet with next emement and removing current element
        prev.next = current.next
        current = None

    #Q.reverse the linkedlist
    def reverselinkedlist(self):
        prev = None
        current = self.head

        if not self.head:
            print("List is empty=====")
            return

        while current:
            #storing our next node in var
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    #printing linkedlist==========
    #Q.traversing through linkedlist===============
    def printlinkedlist(self):
        current = self.head
        while current:
            print(current.data,end='=>')
            current = current.next
        print("None")

li = Linkedlist()

# li.appendelement(1)
# li.appendelement(2)
# li.appendelement(3)

# li.prependelement(1)
# li.prependelement(2)
# li.prependelement(3)

li.addelementatpos(1,0)
li.addelementatpos(2,1)
li.addelementatpos(3,2)
li.addelementatpos(4,3)

li.lenoflist()       # length of list

# li.addelementatpos(4,5)  #bounding an index

# li.removeelebyval(1)
# li.removeelebyval(3)
# li.removeelebyval(6)   #value doesnt exists

li.printlinkedlist()

li.reverselinkedlist()

li.printlinkedlist()

#==================================================================================