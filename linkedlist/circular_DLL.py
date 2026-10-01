
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCLL:
    def __init__(self):
        self.head = None

    def appendelement(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def prepenedelement(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node  

    def addeleatpos(self,data,pos):
        new_node = Node(data)

        if pos < 0:
            print("Invalid pos=======")
            return
        
        if pos == 0:
            if not self.head:
                self.head = new_node
                new_node.next = new_node
                new_node.prev = new_node
            else:
                last = self.head.prev
                last.next = new_node
                new_node.prev = last
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                return

        count = 0
        ind = pos - 1
        current = self.head
    
        while current.next != self.head and count < ind:
            current = current.next
            count += 1 

        if count != ind:
            print("Position out of bounds==============")
            return

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

    def lengthofDCLL(self):
        if not self.head:
            return 0
        
        current = self.head

        count = 1

        while current.next != self.head:
            current = current.next
            count += 1
        print(count)
        return

    def reverseDCLL(self):
        if not self.head:
            return
        
        current = self.head
        previous = None

        while True:
            next_node = current.next
            current.next = previous
            current.prev = next_node
            previous = current
            current = next_node
            if current == self.head:
                break

        self.head.next = previous
        self.head = previous

            

    def printDCLL(self):
        if not self.head:
            print("List is empty=======")
            return
        current = self.head
        while current:
            print(current.data, end="<=>")
            current = current.next
            if current == self.head:
                break
        print() 

LI = DoublyCLL()
LI.appendelement(1)
LI.appendelement(2)
LI.appendelement(3)

LI.prepenedelement(4)
LI.prepenedelement(5)

LI.addeleatpos(5,5)
LI.addeleatpos(6,6)

LI.lengthofDCLL()

LI.printDCLL()

LI.reverseDCLL()

LI.printDCLL()