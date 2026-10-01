class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_LL:
    def __init__(self):
        self.head = None

    def appendelemenet(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prependelement(self,data):
        new_node = Node(data)

        if not self.head:
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.head = new_node

    def addeleatpos(self, data, pos):
        new_node = Node(data)
        if pos < 0:
            print("Invalid position=========")
            return

        current = self.head

        # Add at position 0
        if pos == 0:
            if not self.head:
                self.head = new_node
                new_node.next = self.head
            else:
                while current.next != self.head:
                    current = current.next
                current.next = new_node
                new_node.next = self.head
                self.head = new_node
            return

        # Traverse to the position where the new node will be inserted
        count = 0
        ind = pos - 1
        while current.next != self.head and count < ind:
            current = current.next
            count += 1

        # Check if position is out of bounds
        if count != ind:
            print("Position out of bounds==============")
            return

        # Insert the new node at the specified position
        new_node.next = current.next
        current.next = new_node

    def removeelebyval(self,val):
        current = self.head
        if current.data == val:
            current = current.next
            current = None
            return
        
        prev = None
        while current and current.data != val:
            prev = current
            current = current.next

        if not current:
            print("not found in list============")
            return
        
        prev.next = current.next
        current = None
                
    def lenofCLL(self):
        current = self.head

        if not self.head:
            return 0
        
        count = 1
        while current.next != self.head:
            count += 1
            current = current.next
        print(count)
        return
    
    def reverseCLL(self):
        
        if not self.head or self.head.next == self.head:
            return

        prev = None
        current = self.head
        next_node = current.next
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break

        self.head.next = prev
        self.head = prev


    def printCLL(self):
        current = self.head

        if not self.head:
            print("List is empty=========")
            return

        while current:
            print(current.data, end="=>")
            current = current.next
            if current == self.head:
                break
        print()


li = Circular_LL()

li.appendelemenet(1)
li.appendelemenet(2)
li.prependelement(3)
li.prependelement(5)

li.addeleatpos(1,0)
li.addeleatpos(3,1)
# li.addeleatpos(3,2)

li.removeelebyval(3)

li.lenofCLL()

li.printCLL()

li.reverseCLL()

li.printCLL()