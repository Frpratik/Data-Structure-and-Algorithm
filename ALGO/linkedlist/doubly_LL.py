class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Doublylinkedlist:
    def __init__(self):
        self.head = None

    #Q.append element in doubly linked list========
    def appendelement(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        else:
            Current = self.head
            while Current.next:
                Current = Current.next
            Current.next = new_node
            new_node.prev = Current

    #Q.prepend element in doubly linked list========
    def prependelement(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    #Q.add element at given position in doubly linked list=========
    def addeleatpos(self,data,pos):
        new_node = Node(data)

        if pos < 0:
            print("Invalid position=======")
            return
        
        if pos == 0:
            self.head = new_node
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        
        current = self.head
        count = 0
        ind = pos - 1

        while current and count < ind:
            current = current.next
            count += 1

        if not current:
            print("Pos out of bounds!==========")
            return

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node

    #Q.length of doubly linked list=======
    def lenofdbllist(self):
        current = self.head
        count = 0

        while current:
            count+= 1
            current = current.next
        print(count)
        return

    #Q.remove elemnt by given value in linked list======
    def removeelebyval(self,val):
        current = self.head

        if not current:
            print("list is epty======")
            return

        if current.data == val:
            self.head = current.next
            if self.head:
                self.head.prev = None
            current = None
            return
        
        previous = None

        while current and current.data != val:
            previous = current
            current = current.next

        if not current:
            print("Value doesnt exists===")
            return

        if current.next:
            current.next.prev = previous
        previous.next = current.next

        current = None

    #Q.reverse the doubly linked list======
    def reversedbllist(self):
        current = self.head
        prev_node = None

        while current:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node

            prev_node = current
            current = next_node

        self.head = prev_node

    def printdbllinkedlist(self):
        current = self.head
        while current:
            print(current.data, end="<=>")
            current = current.next
        print("None")


li = Doublylinkedlist()

# li.appendelement(1)
# li.appendelement(2)
# li.appendelement(3)

# li.prependelement(1)
# li.prependelement(2)
# li.prependelement(3)

li.addeleatpos(1,0)
li.addeleatpos(1,1)
li.addeleatpos(2,2)
li.addeleatpos(3,3)

li.lenofdbllist()    #length of doubly linkedlist

# li.removeelebyval(1)
# li.removeelebyval(4)

li.reversedbllist()    #reverse of doubly linked list

li.printdbllinkedlist()