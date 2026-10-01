#Q.1 242. Group Anagram
strs = ["eat","tea","tan","ate","nat","bat"]
def groupAnagrams(strs):
    
    # 1.
    # TC: O(N × K log K)  SC: O(N × K) 
    # dct = {}

    # for word in strs:
    #     key = "".join(sorted(word))

    #     if key not in dct:
    #         dct[key] = [word]
    #     else:
    #         dct[key].append(word)

    # return list(dct.values())

    # 2.
    # TC: O(N × K)  SC: O(N × K) 
    dct = {}
    for word in strs:
        alp = [0] * 26

        for char in word:
            alp[ord(char) - ord('a')] += 1

        key = tuple(alp)

        if key not in dct:
            dct[key] = [word]
        else:
            dct[key].append(word)

    return list(dct.values())

print(groupAnagrams(strs))

#=====================================================================================================

#Q.1 167. Two Sum II - Input Array Is Sorted
# Two pointers - opposite direction - sorted array
numbers = [2,7,11,15], target = 9
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return [left+1, right+1]

        elif total < target:
            left += 1

        else:
            right -= 1

    return []
print(two_sum(numbers,target))
#=====================================================================================================
 