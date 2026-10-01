"""Question 1 — Easy
Given a sorted array of integers, determine whether there are two numbers whose sum equals target."""

"""
left + right == target → True
sum < target → move left forward
sum > target → move right backward
pointers eventually cross → False
"""
nums = [1, 2, 4, 6, 8, 9, 14]
target = 20
def two_sum(nums, target):
  left,right = 0,len(nums)-1
  for i in range(len(nums)):
    if nums[left] + nums[right] == target:
      return True
    elif nums[left] + nums[right] < target:
      left += 1
    else:
      right -= 1
  return False

print(two_sum(nums,target))

#===========================================================================

"""Question 2 — Easy
Given a sorted array, remove duplicates in-place and return the number of unique elements."""

"""
i → fast pointer → explores every element
j → slow pointer → keeps track of the position of the last unique element
"""
nums = [1, 1, 2, 2, 3, 4, 4]
def remove_duplicates(nums):
  j = 0
  for i in range(1,len(nums)):
    if nums[i] != nums[j]:
      j += 1
      nums[j] = nums[i]
  return j+1

print(remove_duplicates(nums))

#===========================================================================

"""Question 3 — Easy
Given an array of integers, move all zeroes to the end while maintaining the relative order of the non-zero elements."""

"""
j = where the next non-zero element should go.
i scans the entire array.
"""

nums = [0, 1, 0, 3, 12]
def move_zeroes(nums):
  j = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[i],nums[j] = nums[j],nums[i]
      j += 1
  return nums

print(move_zeroes(nums))

#===========================================================================

"""Question 4 — Easy
Given an array, remove all occurrences of a given value in-place and return the number of remaining elements."""

"""
i → scans every element
j → tells where the next valid element should be placed
"""

nums = [2, 1, 2, 2, 3, 0, 4, 1]
val = 2
def remove_element(nums, val):
  j = 0
  for i in range(len(nums)):
    if nums[i] != val:
      nums[j] = nums[i]
      j += 1
  return j

print(remove_element(nums,val))

#===========================================================================

"""
Question 5 — Easy
Problem: Valid Palindrome
Given a string, determine whether it reads the same forward and backward.
"""

"""
i → starts from the left
j → starts from the right
"""
s = "racecar"
def is_palindrome(s):
  i,j = 0,len(s)-1
  while i <= j:
    if s[i] != s[j]:
      return False
    i += 1
    j -= 1
  return True

print(is_palindrome(s))
#===========================================================================
#===========================================================================
