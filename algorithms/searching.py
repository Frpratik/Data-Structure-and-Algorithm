#linear searching===========================================================
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
#=========================================================================
#binary searching================================================

# def binarysearch(arr,t):
#     left = 0
#     right = len(arr)-1
#     while left <= right:
#         mid = left + (right - left)//2
#         if arr[mid] == t:
#             return mid
#         elif arr[mid] < t:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
#
# arr = [1,2,4,5,6]
# t = 5
# print(binarysearch(arr,t))
#=============================================================
#jump searching=========================================

# def jumpsearch(arr,t):
#     n = len(arr)
#     step = int(n**0.5)
#     prev = 0
#
#     while prev < n and arr[step] < t:  # for checking t is present in block or not
#         prev = step
#         step += step
#
#     while prev < n and arr[prev] < t:  #if present then linear search in that block
#         prev += 1
#
#     if arr[prev] == t:
#         return prev
#
#     return -1
#
# arr = [1,2,3,4,5]
# t = 5
# print(jumpsearch(arr,t))
#=====================================================================
#interpolation searching========================================
#
# def interpolationsearch(arr,t):
#     low = 0
#     high = len(arr)-1
#     while low < high and arr[low] <= t <= arr[high]:
#         #interpolation formula only this step is imp in this searching algo
#          pos = low + ((t - arr[low]) * (high - low) // (arr[high] - arr[low])) 
#
#          if arr[pos] == t:
#              return pos
#
#          if arr[pos] < t:
#              low += 1
#          else:
#              high -= 1
#
#     return -1
#
# arr = [1,2,3,4,5]
# t = 4
# print(interpolationsearch(arr,t))
#=============================================================================
#exponential searching=================================================

# def exposearch(arr,t):
#     n = len(arr)
#     if n == 0:
#         return -1
    
#     if arr[0] == 0:
#         return 0 
    
#     i = 1

#     while i < n and arr[i] <= t:
#         i *= 2

#     def binarysearch(arr,left,right,t):
#         left = 0
#         right = len(arr)
#         while left < right:
#             mid = left  + (right-left) // 2
#             if arr[mid] == t:
#                 return mid
#             elif arr[mid] < t:
#                 left += 1
#             else:
#                 right -= 1
#         return -1

#     return binarysearch(arr,i//2,min(i,n),t)


# arr = [1,2,3,4,5]
# t = 5
# print(exposearch(arr,t))
    
#===========================================================================