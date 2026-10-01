# #bogosort===============================================
# import random
# def is_sorted(arr):
#     # Check each pair of adjacent numbers in the list
#     for i in range(len(arr) - 1):
#         # If any pair is out of order, return False
#         if arr[i] > arr[i + 1]:
#             return False
#     # If all pairs are in order, return True
#     return True
# def bogosort(arr):
#     # Keep shuffling the list until it's sorted
#     while not is_sorted(arr):
#         # Shuffle the list randomly
#         random.shuffle(arr)
#     # Return the sorted list
#     return arr
# arr = [3, 1, 2]
# sorted_arr = bogosort(arr)
# print("Sorted array using Bogosort:", sorted_arr)
#
# #================================================================
#
# #bubble sorting===========================================
# arr = [2,3,7,4,6,1]
# n = len(arr)
# for i in range(n):
#     print('\ni:', i)
#     for j in range(0, n-1):
#         print('j:', j)
#         if arr[j] > arr[j + 1]:
#             print(f'{arr[j]} > {arr[j+1]} True')
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             print('arr============', arr)
# print(arr)
#
# #=====================================================================
#
# #selection sorting==============================================
#
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         # Assume the minimum is the first element of the unsorted portion
#         min_index = i
#
#         # Test against elements after i to find the smallest
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 # Update min_index if a smaller element is found
#                 min_index = j
#
#         # Swap the found minimum element with the first element of the unsorted portion
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#
#     return arr
#
#
# # Example usage
# arr = [64, 25, 12, 22, 11]
# sorted_arr = selection_sort(arr)
# print("Sorted array:", sorted_arr)
#
# #=====================================================================
#
# #insertion sorting==================================
# arr = [2, 1, 6, 3, 8, 4]
#
# for i in range(1, len(arr)):
#     current = arr[i]
#     print('\nCurrent:', current)
#     j = i - 1
#     print('j:', j)
#     while j >= 0 and arr[j] > current:
#         arr[j + 1] = arr[j]
#         j -= 1
#         print(arr, '=============')
#     arr[j + 1] = current
#     print('Current final arr:', arr)
#
# print(arr)

#=====================================================================
#merge sorting================================
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
#
#
# arr = [2,5,3,6,3,7,9,2]
# mergesort(arr)
# print('m=================', arr)
#========================================================================
#Quick sorting=====================================================
# def quicksort(arr):
#     def partitian(low,high):
#         pivot = arr[high]
#         i = low-1
#         for j in range(low,high):
#             if arr[j] < pivot:
#                 i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#         arr[i + 1], arr[high] = arr[high], arr[i + 1]
#
#         return i + 1
#
#     def recursionquicksort(low,high):
#         if low < high:
#             pi = partitian(low,high)
#             recursionquicksort(low, pi-1)
#             recursionquicksort(pi+1, high)
#
#     recursionquicksort(0, len(arr)-1)
#
#     return arr
#
#
# arr = [3,2,1,5,8,3,5,9]
# quicksort(arr)
# print(arr)
#======================================================================