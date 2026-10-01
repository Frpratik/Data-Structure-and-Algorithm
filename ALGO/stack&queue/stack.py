# # Stack in list========================

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def push(self,data):
#         return self.stack.append(data)
    
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("Stack is empty")
#         return self.stack.pop()
    
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("Stack is empty")
#         return self.stack[-1]
    
#     def size(self):
#         return len(self.stack)
    
#     def printstack(self):
#         if self.is_empty():
#             raise IndexError("Stack is empty")
#         for i in reversed(self.stack):
#             print(i)

# s = Stack()

# print("Is stack empty:",s.is_empty())

# print("Stack items:")
# s.push(1)
# s.push(2)
# s.push(3)

# s.printstack()

# print("Size of stack is",s.size())

# print("Top item of stack:", s.peek())

# print("Popped item",s.pop())
# print("Popped item",s.pop())

# #============================================================================================================

# # Stack in Linked list======================

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedListStack:
#     def __init__(self):
#         self.top = None

#     def is_empty(self):
#         return self.top is None
    
#     def push(self,data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node

#     def pop(self):
#         if self.is_empty():
#             raise IndexError("stack is empty")
#         poppped_item = self.top.data
#         self.top = self.top.next
#         return poppped_item
    
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("stack is empty")
#         return self.top.data
    
#     def size(self):
#         current = self.top
#         count = 0
#         while current:
#             count += 1
#             current = current.next
#         return count
    
#     def printLLstack(self):
#         if self.is_empty():
#             raise IndexError("stack is empty")
#         current = self.top

#         while current:
#             print(current.data)
#             current = current.next



# s = LinkedListStack()

# print("Is stack empty:",s.is_empty())

# print("Stack items:")
# s.push(1)
# s.push(2)
# s.push(3)
# s.printLLstack()

# print("Size of stack is:",s.size())

# print("Top item of stack is:", s.peek())

# print("Popped item is:",s.pop())

# #============================================================================================================

# # Stack in Array======================

class Arraystack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1
    
    def push(self,item):
        if self.is_full():
            raise OverflowError("Array is full")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty Array")
        popped_item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return popped_item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Empty Array")
        return self.stack[self.top]
    
    def size(self):
        return self.top + 1
    
    def printArrayStack(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

s = Arraystack(3)
print("is stack is empty:",s.is_empty())
s.push(1)
s.push(2)
s.push(3)
s.printArrayStack()
print("is stack is empty:",s.is_empty())

print("Top item of stack is:",s.peek())
print("Size of stack is:",s.size())
# #=============================================================================================

# #Add item at bottom of stack problem(RECURSIVE APPROCH)===========

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def push(self,data):
#         return self.stack.append(data)
    
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("Stack is empty")
#         return self.stack.pop()

#     def addatbottom(self,data):
#         if self.is_empty():
#             self.push(data)
#         else:
#             top = self.pop()
#             self.addatbottom(data)
#             self.push(top)

#     def printstack(self):
#         if self.is_empty():
#             raise IndexError("Stack is empty")
#         for i in reversed(self.stack):
#             print(i)

# s = Stack()

# print("Is stack empty:",s.is_empty())

# print("Stack items:")
# s.push(10)
# s.push(20)
# s.push(30)

# s.addatbottom(40)

# s.printstack()


# #=============================================================================================

# #Add item at bottom of stack problem(ANOTHER APPROCH)===========

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def push(self,data):
#         return self.stack.append(data)
    
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("Stack is empty")
#         return self.stack.pop()

#     def addatbottom(self,data):
#         temp_stack = []
#         while not self.is_empty():
#             temp_stack.append(self.pop())
#         self.push(data)
#         while temp_stack:
#             self.push(temp_stack.pop())


#     def printstack(self):
#         if self.is_empty():
#             raise IndexError("Stack is empty")
#         for i in reversed(self.stack):
#             print(i)

# s = Stack()

# print("Is stack empty:",s.is_empty())

# print("Stack items:")
# s.push(10)
# s.push(20)
# s.push(30)

# s.addatbottom(80)

# s.printstack()

# #=============================================================================================

