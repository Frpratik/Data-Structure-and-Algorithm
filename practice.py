
# def bubblesort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range (n-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# arr = [3, 1, 2]
# print(bubblesort(arr))

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         a = arr[i]
#         j = i - 1
#         while j >=0 and arr[j] > a:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = a
#     return arr
# arr = [3, 1, 2]
# print('i========',insertion_sort(arr))
#
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         mini = i
#         for j in range(i+1, n):
#             if arr[j] < arr[mini]:
#                 mini = j
#         arr[i], arr[mini] = arr[mini], arr[i]
#     return arr
# arr = [3,2,5,4,1]
# print('s======', selection_sort(arr))

# def mergesort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2 #midpoint
#         left = arr[:mid] #leftside
#         right = arr[mid:] #rightside
#
#         mergesort(left) #recursion
#         mergesort(right) #recursion
#
#         i = 0 # loop for left side lists
#         j = 0 #loop for right side lists
#         k = 0 #merged list
#
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 arr[k] = left[i]
#                 i+=1
#             else:
#                 arr[k] = right[j]
#                 j+=1
#             k +=1
#
#         while i < len(left):  #for remaining elements
#             arr[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):  #for remaining elements
#             arr[k] = right[j]
#             j += 1
#             k += 1
#   return arr
#
#
# arr = [2,5,3,6,3,7,9,2]
# mergesort(arr)
# print('m=================', arr)

# def insertionsort(arr):
#     for i in range(1,len(arr)):
#         current = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > current:
#             arr[j + 1] = arr[j]
#             j -= 1
#
#         arr[j + 1] = current
#
# arr = [3,1,2,8]
# insertionsort(arr)
# print(arr)

# def selectionsort(arr):
#     n = len(arr)
#     for i in range(n):
#         mini = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[mini]:
#                 mini = j
#         arr[i], arr[mini] = arr[mini], arr[i]
#     return arr
# arr = [3,2,1,4,5,2,3]
# selectionsort(arr)
# print(arr)

# def mergesort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#
#         mergesort(left)
#         mergesort(right)
#
#         i = 0
#         j = 0
#         k = 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#
#             k += 1
#
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1
#
# arr = [1,4,7,3,2,5,6]
# mergesort(arr)
# print(arr)

# def quicksort(arr):
#     def partitian(low,high):
#         pivot = arr[high]
#         print('pivot========', pivot)
#         i = low-1
#         for j in range(low,high):
#             if arr[j] < pivot:
#                 print(arr[j],'<',pivot)
#                 i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#                 print('arr======', arr)
#         arr[i + 1], arr[high] = arr[high], arr[i + 1]
#         print('arr======', arr)
#
#         return i + 1
#
#     def recursionquicksort(low,high):
#         if low < high:
#             pi = partitian(low,high)
#             print('pi=====',pi)
#             recursionquicksort(low, pi-1)
#             recursionquicksort(pi+1, high)
#
#     recursionquicksort(0, len(arr)-1)
#
#     return arr
#
#
# arr = [3,2,1,5,8,3,5,2]
# quicksort(arr)
# print(arr)
#

#
# def mergesort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#
#         mergesort(left)
#         mergesort(right)
#
#         i = 0
#         j = 0
#         k = 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#
#             k += 1
#
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1
#
#         return arr
#
# arr = [3,2,5,1]
# mergesort(arr)
# print(arr)

# def quicksort(arr):
#     def partitian(low,high):
#         pivot = arr[high]
#         i = low - 1
#         for j in range(low,high):
#             if arr[j] < pivot:
#                 i += 1
#                 arr[i],arr[j] = arr[j], arr[i]
#         arr[i+1],arr[high] = arr[high], arr[i+1]
#         return i+1
#
#     def recursivequicksort(low,high):
#         if low < high:
#             pi = partitian(low,high)
#             recursivequicksort(low,pi-1)
#             recursivequicksort(pi+1,high)
#
#     recursivequicksort(0, len(arr)-1)
#
#     return arr
#
# arr = [3,2,5,6,1]
# quicksort(arr)
# # print(arr)
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return the index if target is found
#     return -1  # Return -1 if target is not found
#
# arr = [10, 23, 4, 15, 7, 8]
# target = 15
# index = linear_search(arr, target)
# if index != -1:
#     print(f"Target {target} found at index {index}.")
# else:
#     print(f"Target {target} not found in the array.")
#
# def binarysearch(arr,t):
#     left = 0
#     right = len(arr)-1
#     while left <= right:
#         mid = left + (right - left) // 2  # mid
#         if arr[mid] == t:
#             return mid
#         elif arr[mid] < t:   #if mid value is lwt target then only search in left side
#             left = mid+1
#         elif arr[mid] > t:   #if mid value is grt target then only search in right side
#             right = mid-1
#     return -1
#
# arr = [3,4,6,8,9]
# t = 9
# print(binarysearch(arr,t))


# def jumpsearch(arr,t):
#     n = len(arr)-1
#     step = int(n ** 0.5)               #sqroot
#     prev = 0
#
#     while prev < n and arr[step] < t:  #checking step element is grt t if yes then step increase by step each time
#         prev = step                    #for checking t is present in block or not
#         step += step
#
#
#     while prev < n and  arr[prev] < t: #if t is lt step then liner search
#         prev += 1                      #if present in b;ock then liner search in that block
#
#     if arr[prev] == t:
#         return prev
#
#     return -1
#
# arr = [1,2,3,4,5]
# t = 4
# print(jumpsearch(arr,t))
#

# def ineterpolation(arr,t):
#     low = 0
#     high = len(arr)-1
#     while low < high and arr[low] <= t <= arr[high]:
#         pos = low + ((t - arr[low]) * (high - low) // (arr[high] - arr[low]))  # interpolation formula

#         if arr[pos] == t:
#             return pos

#         if arr[pos] < t:
#             low += 1
#         else:
#             high -= 1

#     return -1

# arr = [1,2,3,4,5]
# t = 5
# print(ineterpolation(arr,t))
#
# def insertionsort(arr):
#     n = len(arr)
#     for i in range(1,n):
#         current = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > current:
#             arr[j+1] = arr[j]
#             j -= 1
#         current,arr[j+1] = arr[j+1], current
#
# arr = [3,5,2,6,1]
# insertionsort(arr)
# print(arr)

#
# def selectionsort(arr):
#     n = len(arr)
#     for i in range(n):
#         mini = i
#         for j in range(i+1, n):
#             if (arr[j] < arr[mini]):
#                 mini = j
#         arr[i],arr[mini] = arr[mini],arr[i]
#     return arr
#
# arr = [3,2,4,1]
# selectionsort(arr)
# print(arr)
#
#
# def mergesort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
#
#         mergesort(left)
#         mergesort(right)
#
#         i = 0
#         j = 0
#         k = 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#
#             k += 1
#
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1
#
#         while j < len(right):
#                 arr[k] = right[j]
#                 j += 1
#                 k += 1
#
#     return arr
#
# arr = [3,2,4,1,5]
# mergesort(arr)


# def quicksort(arr):
#     def partitian(low,high):
#         pivot = arr[high]
#         i = low - 1
#         for j in range(low,high):
#             if arr[j] < pivot:
#                 i += 1
#                 arr [i],arr[j] = arr[j],arr[i]
#         arr[i+1],arr[high] = arr[high],arr[i+1]
#         return i+1

#     def recursiveQsort(low,high):
#         if low < high:
#             pi = partitian(low,high)
#             recursiveQsort(low,pi-1)
#             recursiveQsort(pi+1,high)

#     recursiveQsort(0,len(arr)-1)


#     return arr


# arr = [3,2,4,1]
# quicksort(arr)
# print(arr)


# def linearsearch(arr,t):
#     for i in range(len(arr)):
#         if arr[i] == t:
#             return i
#     return -1

# arr = [1,2,3,4,5]
# t = 5
# print(linearsearch(arr,t))

# def binarysearch(arr,t):
#     n = len(arr)
#     left = 0
#     right = n

#     while left <+ right:
#         for i in range(n):
#             mid = left + (right - left) // 2
#             if arr[mid] == t:
#                 return mid
#             elif arr[mid] < t:
#                 left += 1
#             else:
#                 right -= 1

#     return -1

# arr = [1,2,3,4,5]
# t = 5
# print(binarysearch(arr,t))

# def interpolation(arr,t):
#     n = len(arr)
#     low = 0
#     high = n -1
#     while low <= high and arr[low] <= t <= arr[high]:

#         pos = low + ((t - arr[low]) * (high - low) // (arr[high] - arr[low])) 

#         if arr[pos] == t:
#             return pos
#         elif arr[pos] < t:
#             left += 1
#         else:
#             rigt -= 1

#     return -1

# arr = [1,2,3,4,5]
# t = 5
# print(interpolation(arr,t))

# def exposearch(arr,t):
#     n = len(arr)

#     if arr[0] == t:
#         return 0
    
#     i = 1

#     while i < n and arr[i] <= t:
#         i *= 2

#     def binarysearch(arr, left, right, target):
#         while left <= right:
#             mid = left + (right - left) // 2
#             if arr[mid] == target:
#                 return mid
#             elif arr[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1


#     return binarysearch(arr,i // 2,min(i,n-1),t)

# arr = [1,2,3,4,5]
# t = 3
# print(exposearch(arr,t))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def print_list(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")


# # Example usage
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.print_list()



#LINKEDLIST============================

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def appendelement(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def printlinkedlist(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# li = Linkedlist()
# li.appendelement(3)
# li.appendelement(4)
# li.appendelement(5)
# li.printlinkedlist()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    
# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def appendelement(self,data):
#         new_node = Node(data)

#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
 
#     def prependelement(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def addelementatpos(self,data,pos):
#         new_node = Node(data)

#         if pos < 0:
#             print("Invalid position==========")
#             return
        
#         if pos == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return

#         current = self.head
#         count = 0
#         ind = pos - 1

#         while current and count < ind:
#             current = current.next
#             count += 1

#             if not current:
#                 print("Postion out of bounds========")
#                 return

#         new_node.next = current.next
#         current.next = new_node

#     def removeelebyval(self,val):
#         current = self.head
#         if not current:
#             print("List is empty=====")
#             return
#         #chechikg if value found in head
#         if current.data == val:
#             self.head = current.next
#             current = None
#             return
        
#         #tracking prev element
#         prev = None

#         #TRAVERSING UNTIL VLUE FOUND
#         while current and current.data != val:
#             prev= current
#             current = current.next

#         if not current:
#             print("value doesnt found in list======")
#             return

#         #removing element and linking pore element with next one
#         prev.next = current.next
#         current = None


#     def printlinkedlist(self):
#         current = self.head
#         while current:
#             print(current.data, end="=>")
#             current = current.next
#         print("None")

# li = Linkedlist()
# # li.appendelement(3)
# # li.appendelement(4)
# # li.appendelement(5)

# # li.prependelement(1)
# # li.prependelement(2)
# # li.prependelement(3)

# li.addelementatpos(1,0)
# li.addelementatpos(2,1)
# li.addelementatpos(3,2)
# li.addelementatpos(4,3)
# li.addelementatpos(4,5)  #bounding an index
# li.removeelebyval(3)
# li.removeelebyval(4)
# li.printlinkedlist()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         new_node = Node(data)

#         if not self.head:
#             self.head = new_node 
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

#     def prepend(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def addeleatpos(self,data,pos):
#         new_node = Node(data)

#         if pos < 0:
#             print("Invalid position======")
#             return
        
#         if pos == 0:
#             new_node.next = self.head
#             self.head = new_node
#             return

#         current = self.head
#         count = 0
#         ind = pos - 1

#         while current and count < ind:
#             current = current.next
#             count += 1

#         if not current:
#             print("position out of bounds======")   
#             return  

#         new_node.next = current.next
#         current.next = new_node

#     def removelebyval(self,val):
#         current = self.head

#         if current.data == val:
#             current = current.next
#             current = None

#         prev = None

#         while current and current.data != val:
#             prev = current
#             current = current.next

#         if not current:
#             print("value doesnt exists in list=====")
#             return
        
#         prev.next = current.next
#         current = None

#     def lenoflist(self):
#         current = self.head
#         count = 0
#         if current:
#             while current:
#                 count += 1
#                 current = current.next
#         print(count)


#     def reverselinkedlist(self):
#         prev = None
#         current = self.head

#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head = prev
    


#     def printlist(self):
#         current = self.head
#         while current:
#             print(current.data, end="=>")
#             current = current.next
#         print("None")

# li = Linkedlist()
# # li.append(4)
# # li.append(5)
# # li.prepend(2)
# # li.prepend(3)
# li.addeleatpos(1,0)
# li.addeleatpos(2,1)
# # li.removelebyval(2)
# li.lenoflist()
# li.printlist()
# li.reverselinkedlist()
# li.printlist()

# a = [[1,2,3],[4,5,6],[7,8,9]]
# op = []
# for i in range(len(a[0])):
#     l = []
#     for j in a:
#         l.append(j[i])
#     op.append(l)
# print(op)


# a = "abc13b8"
# c = "0"
# ans = 0
 
# for i in a:
#     try: 
#         int(i)
#         c += i
#     except: 
#         int_c = int(c)
#         ans += int_c
#         c = "0"
#         continue
# ans += int(c)
# print(ans)

# a = "fgh657cfgji67u67"
# c = "0"
# ans = 0

# for i in a:
#     if '0' <= i <= '9':
#         c += i
#     else:
#         ans += int(c)
#         c = "0"

# ans += int(c)
# print(ans)


# a = [[1,2,3,4],[7,5,6,7],[8,9,0,2]]

# op = [1,7,8,9,5,2,3,6,0,2,7,4]


 
# a = [[1,2,3,4],
#      [4,5,6,7],
#      [8,9,0,1],
#      [9,3,4,8]]
# b = 0
# for i in range(len(a)):
#     b += a[i][len(a)-i-1]                                                      
# print(b)


# a = [[1,2,3,4],[0,6,7,8],[0,0,11,12],[0,1,0,16]]
 
# def uppertri(arr):
#     for i in a:
#         print(i) 
#     for i in range(len(arr)):
#         for j in arr[i][0:i]:
#             if j!= 0:
#                 return False
#     return True
# print(uppertri(a))


# a = [[3,2,1],
#      [1,7,6],
#      [2,7,7]]

# a = [[3,1,2,2],
#      [1,4,4,5],
#      [2,4,2,2],
#      [2,4,2,2]]

# count = 0
# for i in range(len(a)):
#     row = a[i]
#     for k in range(len(a)):
#         col = []
#         for j in range(len(a)):
#             col.append(a[j][k])
#         if row == col:
#             count += 1
# print(count)


# class Node:
#     def __init__(self,data):
#         self.data = data 
#         self.next = None

# class CircularLL:
#     def __init__(self):
#         self.head = None

#     def appendelement(self,data):
#         new_node = Node(data)

#         if not self.head:
#             self.head = new_node
#             self.head.next = self.head
#         else:
#             current = self.head
#             while current.next != self.head:
#                 current = current.next
#             current.next = new_node
#             new_node.next = self.head

#     def prependelement(self,data):
#         new_node = Node(data)
#         if not self.head:
#             new_node.next = new_node
#         else:
#             current = self.head
#             while current.next != self.head:
#                 current = current.next
#             current.next = new_node
#             new_node.next = self.head
#         self.head = new_node

    
#     def addeleatpos(self, data, pos):
#         new_node = Node(data)
#         if pos < 0:
#             print("Invalid position=========")
#             return

#         current = self.head

#         # Add at position 0
#         if pos == 0:
#             if not self.head:
#                 self.head = new_node
#                 new_node.next = self.head
#             else:
#                 while current.next != self.head:
#                     current = current.next
#                 current.next = new_node
#                 new_node.next = self.head
#                 self.head = new_node
#             return

#         # Traverse to the position where the new node will be inserted
#         count = 0
#         ind = pos - 1
#         while current.next != self.head and count < ind:
#             current = current.next
#             count += 1

#         # Check if position is out of bounds
#         if count != ind:
#             print("Position out of bounds==============")
#             return

#         # Insert the new node at the specified position
#         new_node.next = current.next
#         current.next = new_node
            
#     def removeelebyval(self,val):
#         current = self.head
#         if current.data == val:
#             current = current.next
#             current = None

#         prev = None

#         while current and current.data != val:
#             prev = current
#             current= current.next

#         if not current:
#             print("val doesnt exists in list=========")
#             return

#         prev.next = current.next
#         current = None


#     def lenofCLL(self):
#         current = self.head

#         if not self.head:
#             return 0

#         count = 1 
#         while current.next != self.head:
#             count += 1
#             current = current.next
#         print(count)
#         return
    
#     def reverseCLL(self):
#         previous = None
#         current = self.head
        
#         if not self.head or self.head.next == self.head:
#             return
        
#         while True:
#             next_node = current.next
#             current.next = previous
#             previous = current
#             current = next_node

#             if current == self.head:
#                 break

#         self.head.next = previous
#         self.head = previous           
            
          
#     def printCLL(self):
#         if not self.head:
#             print("List is empty=========")
#             return
#         current = self.head
#         while current:
#             print(current.data,end="=>")
#             current = current.next
#             if current == self.head:
#                 break
#         print()

# li = CircularLL()
# # li.appendelement(1)
# # li.appendelement(2)
# # li.appendelement(3)
# # li.prependelement(1)
# # li.prependelement(2)
# li.addeleatpos(4,0)
# li.addeleatpos(4,1)
# li.addeleatpos(5,5)
# li.addeleatpos(6,6)
# # li.removeelebyval(3)
# li.lenofCLL()
# # li.reverseCLL()
# li.printCLL()


# input = "bar(bar)"
# m = input.index("(")
# k = input.index(")")

# for j in range(m,k):
#         input[m:k] = input[k:m:-1]

# l=[[7,8,9],
#    [4,5,6],
#    [1,2,3]]
# l1=[]
# for i in range(len(l)):
#     if i%2==0:
#         k=0
#         for j in range(len(l[i])):
#             l1.append(l[k][i])
#             k+=1
#     else:
#         k=len(l)-1
#         for j in range(len(l[i])):
#             l1.append(l[k][i])
#             k-=1
# print(l1)


# l = [[7, 8, 9],
#      [4, 5, 6],
#      [1, 2, 3]]

# l1 = []

# for j in range(len(l[0])):
#     if j % 2 == 0:
#         for i in range(len(l)):
#             l1.append(l[i][j])
#     else:
#         for i in range(len(l) - 1, -1, -1):
#             l1.append(l[i][j])

# print(l1)

#============================imp===========================================================
# l = [[7, 8, 9],
#      [4, 5, 6],
#      [1, 2, 3],
#      [14, 16, 18],
#      [8, 10, 12],
#      [2, 4, 6]]

# row = len(l[0])
# column = len(l)

# top = 0
# left = 0
# right = row- 1
# bottom = column - 1

# while (top <= bottom and left <= right):

#     for i in range(left,right+1):
#         print(l[top][i], end='=>')
        
#     top += 1

#     for i in range(top,bottom+1):
#         print(l[i][right], end='=>')

#     right -= 1

#     if top<= bottom:
#         for i in range(right,left-1,-1):
#             print(l[bottom][i], end='=>')

#         bottom -= 1

#     if left<= right:
#         for i in range(bottom,top-1,-1):
#             print(l[i][left], end='=>')

#         left += 1

#============================imp===========================================================

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class CircularLL:
#     def __init__(self):
#         self.head = None

#     def appendelement(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.head.next = new_node
#         else:
#             current = self.head
#             while current.next != self.head:
#                 current = current.next
#             current.next = new_node
#             new_node.next = self.head

#     def prependelement(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             self.head.next = new_node
#         else:
#             current = self.head
#             while current.next != self.head:
#                 current = current.next
#             current.next = new_node
#             new_node.next = self.head
#         self.head = new_node

#     def addeleatpos(self,data,pos):
#         new_node = Node(data)
#         if pos < 0 :
#             print("Invalid position==========")
#             return
        
#         current = self.head

#         if pos == 0:
#             if not self.head:
#                 self.head = new_node
#                 self.head.next = self.head
#             else:
#                 while current.next != self.head:
#                     current = current.next
#                 current.next = new_node
#                 new_node.next = self.head
#                 self.head = new_node
#                 return

#         count = 0
#         ind = pos - 1

#         while current.next != self.head and count < ind:
#             current = current.next
#             count += 1
        
#         if count != ind:
#             print("Position out of bounded=========")
#             return
        
#         new_node.next = current.next
#         current.next = new_node

#     def removeelebyval(self,val):
#         current = self.head
#         if current.data == val:
#             current = current.next
#             current = None
#             return
        
#         prev = None
#         while current and current.data != val:
#             prev = current
#             current = current.next

#         if not current:
#             print("not found in list============")
#             return
        
#         prev.next = current.next
#         current = None
                
#     def lenofCLL(self):
#         current = self.head

#         if not self.head:
#             return 0
        
#         count = 1
#         while current.next != self.head:
#             count += 1
#             current = current.next
#         print(count)
#         return
    
#     def reverseCLL(self):
        
#         if not self.head or self.head.next == self.head:
#             return

#         prev = None
#         current = self.head
#         next_node = current.next
#         while True:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#             if current == self.head:
#                 break

#         self.head.next = prev
#         self.head = prev



#     def printCLL(self):
#         if not self.head:
#             print("List is empty=========")
#             return
#         current = self.head
#         while current:
#             print(current.data,end="=>")
#             current = current.next
#             if current == self.head:
#                 break
#         print()


# li = CircularLL()
# li.appendelement(1)
# li.appendelement(2)
# li.appendelement(3)
# li.prependelement(4)
# li.prependelement(5)
# li.addeleatpos(6,0)
# li.addeleatpos(6,6)
# li.removeelebyval(5)
# li.removeelebyval(1)
# li.lenofCLL()
# li.printCLL()
# li.reverseCLL()
# li.printCLL()


#==================================================================================================

#Doubly linked list 

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyCLL:
#     def __init__(self):
#         self.head = None

#     def appendelement(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             new_node.next = new_node
#             new_node.prev = new_node
#         else:
#             last = self.head.prev
#             last.next = new_node
#             new_node.prev = last
#             new_node.next = self.head
#             self.head.prev = new_node

#     def prepenedelement(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             new_node.next = new_node
#             new_node.prev = new_node
#         else:
#             last = self.head.prev
#             last.next = new_node
#             new_node.prev = last
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node  

#     def addeleatpos(self,data,pos):
#         new_node = Node(data)

#         if pos < 0:
#             print("Invalid pos=======")
#             return
        
#         if pos == 0:
#             if not self.head:
#                 self.head = new_node
#                 new_node.next = new_node
#                 new_node.prev = new_node
#             else:
#                 last = self.head.prev
#                 last.next = new_node
#                 new_node.prev = last
#                 new_node.next = self.head
#                 self.head.prev = new_node
#                 self.head = new_node
#                 return

#         count = 0
#         ind = pos - 1
#         current = self.head
    
#         while current.next != self.head and count < ind:
#             current = current.next
#             count += 1 

#         if count != ind:
#             print("Position out of bounds==============")
#             return

#         new_node.next = current.next
#         new_node.prev = current
#         current.next.prev = new_node
#         current.next = new_node

#     def lengthofDCLL(self):
#         if not self.head:
#             return 0
        
#         current = self.head

#         count = 1

#         while current.next != self.head:
#             current = current.next
#             count += 1
#         print(count)
#         return

#     def reverseDCLL(self):
#         if not self.head:
#             return
        
#         current = self.head
#         previous = None

#         while True:
#             next_node = current.next
#             current.next = previous
#             current.prev = next_node
#             previous = current
#             current = next_node
#             if current == self.head:
#                 break

#         self.head.next = previous
#         self.head = previous

            

#     def printDCLL(self):
#         if not self.head:
#             print("List is empty=======")
#             return
#         current = self.head
#         while current:
#             print(current.data, end="<=>")
#             current = current.next
#             if current == self.head:
#                 break
#         print() 

# LI = DoublyCLL()
# LI.appendelement(1)
# LI.appendelement(2)
# LI.appendelement(3)

# LI.prepenedelement(4)
# LI.prepenedelement(5)

# LI.addeleatpos(5,5)
# LI.addeleatpos(6,6)

# LI.lengthofDCLL()

# LI.printDCLL()

# LI.reverseDCLL()

# LI.printDCLL()

#===================================================================================

#stack================
# stack in list=====================
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            print("Stack (top to bottom):")
            for item in reversed(self.stack):
                print(item)

# Usage Example
stack = Stack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Print stack elements
stack.print_stack()  # Output: Stack (top to bottom): 3, 2, 1

# Peek at the top element
print("Top element:", stack.peek())  # Output: Top element: 3

# Check if stack is empty
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

# Pop elements from the stack
print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Popped element:", stack.pop())  # Output: Popped element: 2
print("Popped element:", stack.pop())  # Output: Popped element: 1

# Check if stack is empty after popping all elements
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? True

# Attempting to peek or pop from an empty stack will raise an IndexError
# stack.peek()
# stack.pop()


#stack in linked list===============

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        popped_item = self.top.data
        self.top = self.top.next
        return popped_item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.top.data
    
    def printLLStack(self):
        if self.is_empty():
            raise IndexError("Print from an empty stack")
        current = self.top
        print("Stack (top to bottom):")
        while current:
            print(current.data)
            current = current.next

# Usage Example
stack = Stack()

# Push elements onto the stack
stack.push(5)
stack.push(6)
stack.push(7)

# Print stack elements
stack.print_stack()  # Output: Stack (top to bottom): 3, 2, 1

# Peek at the top element
print("Top element:", stack.peek())  # Output: Top element: 3

# Check if stack is empty
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

# Pop elements from the stack
print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Popped element:", stack.pop())  # Output: Popped element: 2
print("Popped element:", stack.pop())  # Output: Popped element: 1

# Check if stack is empty after popping all elements
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? True

#================================================================================

#queue

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def is_empty(self):
#         return len(self.queue) == 0
    
#     def enqueue(self,item):
#         self.queue.append(item)

#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError("List is empty")
#         return self.queue.pop(0)
    
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("List is empty")
#         return self.queue[0]

#     def size(self):
#         return len(self.queue)
    
#     def printQueue(self):
#         if self.is_empty():
#             raise IndexError("List is empty")
#         print("Queue elements are:")
#         for i in reversed(self.queue):
#             print(i)
    

# q = Queue()

# print("is queue is empty:",q.is_empty())

# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)

# q.printQueue()

# print("is queue is empty:",q.is_empty())
# print("Popped item:",q.dequeue())
# print("Top item of queue is:",q.peek())
# print("Size of queue is:",q.size())

#Queue in array(normal array)

# class Queue:
#     def __init__(self,size):
#         self.queue = [None] * size
#         self.front = 0
#         self.top = 0
#         self.size = size

#     def is_empty(self):
#         return self.front == self.top
    
#     def is_full(self):
#         return self.top == self.size
    
#     def enqueue(self,item):
#         if self.is_full():
#             raise IndexError("Array is full")
#         self.queue[self.top] = item
#         self.top += 1

#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError("Array is empty")
#         popped_item = self.queue[self.front]
#         for i in range(1,self.top):
#             self.queue[i-1] = self.queue[i]
#         self.top -= 1
#         return popped_item

#     def peek(self):
#         if self.is_empty():
#             raise IndexError("Array is empty")
#         return self.queue[self.front]
    
#     def printArayQueue(self):
#         if self.is_empty():
#             raise IndexError("Array is empty")
#         print("Queue elements are:")
#         for i in range(self.top - 1, self.front - 1, -1):
#             print(self.queue[i])

# q = Queue(3)
# print("Is array empty:",q.is_empty())
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.printArayQueue()
# print("Is array empty:",q.is_empty())
# print("Is array empty:",q.is_full())
# print("Top item of array:",q.peek())

#===================================================================================================

#Queue in array(circular manner)

class CircularQueue:
    def __init__(self,size):
        self.queue = [None] * size
        self.front = -1
        self.top = -1
        self.size = size

    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return self.front == (self.top + 1) % self.size
    
    def enqueue(self,item):
        if self.is_full():
            raise IndexError("Array is full")
        if self.is_empty():
            self.front = 0
        self.top = (self.top + 1) % self.size
        self.queue[self.top] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Array is empty")
        popped_item = self.queue[self.front]
        if self.front == self.top:
            self.front = -1
            self.top - 1
        else:
            self.front = (self.front + 1) % self.size
        return popped_item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Array is empty")
        return self.queue[self.front]
    
    def printCircularArrayQueue(self):
        if self.is_empty():
            raise IndexError("Array is empty")
        print("Circular Queue elements are:")
        i = self.front
        while True:
            print(self.queue[i])
            if i == self.top:
                break
            i = (i + 1) % self.size

q = CircularQueue(3)
print("Is array empty:",q.is_empty())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(7)  #at 0th index due to circular manner
q.printCircularArrayQueue()
print("Is array empty:",q.is_empty())
print("Is array empty:",q.is_full())
