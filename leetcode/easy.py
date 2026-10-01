#================================================================================================
# Q.1 1. Two Sum
nums = [2,1,4,9]
target = 10
def twoSum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i,j]
    haz = {}
    for i,num in enumerate(nums):
        a = target - num
        if a not in haz:
            haz[num] = i
            continue
        return [haz[a],i]
        
print(twoSum(nums,target))

#=====================================================================================================

# Q.2 9. Palindrome Number
x = "121"

def isPalindrome(x: int) -> bool:
    c = list(str(x))
    for i in c:
        p = c.pop()
        if i != p: return False
    return True

print(isPalindrome(x))

#=====================================================================================================

# Q.3 13. Roman to Integer
s = "CVI"

def romanToInt(s: str) -> int:
    haz = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    t = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and haz[s[i]] < haz[s[i + 1]]:
            t += haz[s[i + 1]] - haz[s[i]]
            i += 2  
        else:
            t += haz[s[i]]
            i += 1
    return t

print(romanToInt(s))
    
#=====================================================================================================   
 
# Q.4 14. Longest Common Prefix
strs = ["flower","flow","flight"]
def longestCommonPrefix(strs):
    
    shortest_string = min(strs, key=len)

    t = ""
    for i in range(len(shortest_string)):
        current_char = shortest_string[i]
        
        is_common = True
        for j in strs:
            if j[i] != current_char:
                is_common = False
                break 
            
        if not is_common:
            break  
        
        t += current_char

    return t
    
print(longestCommonPrefix(strs))
#=====================================================================================================

#Q.5 20. Valid Parentheses
def isValid(s):
        haz = {"{":"}","[":"]","(":")"}
        stack = []
        for char in s:
            if char in haz:
                stack.append(char)
            else:
                if not stack or haz[stack.pop()] != char:
                    return False
        
        return len(stack) == 0

print(isValid("{[()]}")) #True

#=====================================================================================================

#Q.6 21. Merge Two Sorted Lists





#=====================================================================================================

#Q.7 26. Remove Duplicates from Sorted Array
# Two pointers - same direction
def removeDuplicates(nums):
    i = 0
    for j in range(1,len(nums)):
        if not nums:
            return 0
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i+1

print(removeDuplicates([1,2,2,3,3,4,4]))

#=====================================================================================================

#Q.8 27. Remove Element

val = 3
def removeElement(nums):
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

print(removeElement([2,2,3,3]))

#=====================================================================================================

#Q.9 27. Remove Element

haystack = "leetcode"
needle = "cod"
def strStr(haystack,needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1

print(strStr(haystack,needle))

#=====================================================================================================

#Q.10 35. Search Insert Position

def searchInsert(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

print(searchInsert([4,5,6,8],7))

#=====================================================================================================

# Q.11 58. Length of Last Word

def lengthOfLastWord(s):
    s = s.rstrip()
    count = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == " ":
            break
        count += 1
    return count

print(lengthOfLastWord(" i love rasmalai "))
#=====================================================================================================

#Q.12 66. Plus One

def plusOne(digits):
    s = ""
    for i in digits:
        s += str(i)
    a = str(int(s) + 1)
    l = [int(i) for i in a]
    return l

print(plusOne([1,3,5]))

#=====================================================================================================

#Q.13 69. Sqrt(x)

def mySqrt(x):
    if x < 2:
        return x
    
    left, right = 1, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

print(mySqrt(8))

#=====================================================================================================
#Q.14 70. Climbing Stairs

def climbStairs(n):
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(climbStairs(5))

#=====================================================================================================

#Q 15. 83. Remove Duplicates from Sorted List

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = head
#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
#         return head

#=====================================================================================================

#Q 16. 88. Merge Sorted Array

# def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # """
    # Do not return anything, modify nums1 in-place instead.
    # """
    # last = m + n - 1
    
    # # Pointers for nums1 and nums2
    # i = m - 1
    # j = n - 1

    # # While there are elements to be merged
    # while i >= 0 and j >= 0:
    #     if nums1[i] > nums2[j]:
    #         nums1[last] = nums1[i]
    #         i -= 1
    #     else:
    #         nums1[last] = nums2[j]
    #         j -= 1
    #     last -= 1

    # # If nums2 is not exhausted
    # while j >= 0:
    #     nums1[last] = nums2[j]
    #     j -= 1
    #     last -= 1

#=====================================================================================================

#Q 17. 118. Pascal's Triangle

def generate(numRows):
    triangle = [] 
    for i in range(numRows):
        row = [1] * (i + 1)
        
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
        triangle.append(row)
    return triangle

print(generate(5))
#=====================================================================================================

#Q 18. 118. Pascal's Triangle II

def getRow(rowIndex):
    triangle = [] 
    if rowIndex == 0:
        triangle.append([1])
    else:
        for i in range(rowIndex+1):
            row = [1] * (i + 1)
            
            for j in range(1,i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
                
            triangle.append(row)
    return triangle[-1]

print(getRow(3))
#=====================================================================================================

#Q 19 121. Best Time to Buy and Sell Stock.

def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0 
    
    for price in prices[1:]:
        if price < min_price:
            min_price = price 
        elif price - min_price > max_profit:
            max_profit = price - min_price  

    return max_profit

print(maxProfit([4,3,6,2,7,4,9]))

#=====================================================================================================

#Q 20. 125. Valid Palindrome

def isPalindrome(s):
    a = ""
    for i in s:
        if i.isalnum():
            a+=i.lower()
    r = a[::-1]
    if a == r:
        return True
    return False

print(isPalindrome(" mo 00o:m"))
#=====================================================================================================

#Q 20. 136. Single Number
def singleNumber(nums):
    unique = 0
    for n in nums:
        unique ^= n
    return unique

print(singleNumber([1,2,4,2,1]))
#=====================================================================================================

#Q 21.217. Contains Duplicate

def containsDuplicate(nums):
    # 1.
    # sortedarr = sorted(nums)
    # for i in range(len(sortedarr)-1):
    #     if sortedarr[i+1] == sortedarr[i]:
    #         return True
    # return False
    
    # 2.
    ms = set()
    for i in nums:
        if i in ms:
            return True
        ms.add(i)
    return False
print(containsDuplicate([2,3,4,1,1]))
#=====================================================================================================

#Q.22. 228. Summary Ranges

def summaryRanges(nums):
    ls = []
    i = 0
    while i < len(nums):
        begin = nums[i]
        while i < len(nums)-1 and nums[i] == nums[i+1] - 1:
            i += 1
        end = nums[i]
        if begin == end:
            ls.append(str(begin))
        else:
            ls.append(f"{begin}->{end}")
        i += 1
    return ls

print(summaryRanges([0,2,3,4,6,7,9]))

#=====================================================================================================

#Q.22 242. Valid Anagram

def isAnagram(s, t):
    # 1.
    # return sorted(s) == sorted(t)
    
    # 2.
    if len(s) != len(t):
        return False

    count = {}

    # 1. Build frequency
    for char in s:
        count[char] = count.get(char, 0) + 1

    # 2. Subtract frequency
    for char in t:
        if char not in count:
            return False
        count[char] -= 1

    # 3. Check everything is zero
    for value in count.values():
        if value != 0:
            return False

    return True

print(isAnagram("cat","tac"))

#=====================================================================================================

#Q23. 344. Reverse String
#Two pointers - opposite direction - sorted array
def reverseString(S):
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i <= j:
            s[i],s[j] = s[j], s[i]
            i += 1
            j -= 1

print(reverseString("sdfghj"))

#=====================================================================================================

#Q24. 283. Move Zeroes - moves all zeroes to end 
#Two pointers - same direction - one is to find non-zero element and another one is to keep track on 0
def moveZeroes(nums):
    i = 0

    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))