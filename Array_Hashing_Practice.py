###############-------------------Arrays and Hashing---------------------------##################
#Q1.Duplicate Integer
#https://neetcode.io/problems/duplicate-integer
         for i in nums:
            if nums.count(i)>1:
               return True
         return False  
         #Leetcode it gave time limit extended for above
           #or

          for i in range(0,len(nums)):
              for j in range(1,len(nums)):
                   if nums[i]==nums[j] and i!=j:
                         print(True)
          print(False)
           #Leetcode it gave time limit extended for above
           #or
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        #best solution
           #or
          return len(set(nums)) != len(nums)
           #takes few ms more then above

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = []
        for i in nums:
            if i in duplicate:
                return True
            duplicate.append(i) 
        return False
         

Time complexity:

O(n), where n is the number of elements in the list.
Explanation: We iterate through the list once, performing O(1) operations for each element.
Space complexity:

O(n)
Explanation: The set used to store seen elements can contain up to n elements in the worst case.
#######################################################################################
#Q2.Is anagram
#https://neetcode.io/problems/is-anagram
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        else: return False
     #or
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
#Complexity: O(n)
######################################################################################
#Q3. 2 Sum
#https://neetcode.io/problems/two-integer-sum
       #best Solution compltes in 58ms

        prevMap = {}  # val -> index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
                 
                 #or Completes in 3323ms
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]
         #O(n)
########################################################################################
#Q4 Group Anagrams
https://neetcode.io/problems/anagram-groups?list=neetcode150
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
             anagram = defaultdict(list)
             for i in strs:
                      sorted_i = ''.join.(sorted(i))
                      anagram[sorted_i] = sorted_i
             return list(anagram.values())

#######################################################################################
#Q5 Top K Frequent Elements
http://neetcode.io/problems/top-k-elements-in-list?list=neetcode150
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
             count = {}
             for i in nums:
                      if i in count:
                               count[i] += 1
                      else:
                               count[i] = 1

             arr = []
             for i, n in enumerate(count.items()):
                      arr.append([n,i])
             arr.sort()
             
             result = []
             while len(result) < k:
                      result.append(arr.pop()[1])

#######################################################################################
#Q6 Encode Decode String
https://neetcode.io/problems/string-encode-and-decode?list=neetcode150

######################################################################################
#Q7 Products of Array Except Self
https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150


######################################################################################
#Q8 Valid Sudoku
https://neetcode.io/problems/valid-sudoku?list=neetcode150


######################################################################################
#Q9 Longest Consecutive Sequence
https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
             new_nums = set(nums)
             longest = 0
             for num in new_nums:
                      if num - 1 not in new_num:
                               curr_num = num
                               curr_count = 1
                               
                               while curr_num + 1 in new_num:
                                        curr_num += 1
                                        curr_count += 1

                                longest = max(longest, curr_count)
               return longest











        
         
