###############-------------------Arrays---------------------------##################
#Q1.Duplicate Integer
#https://neetcode.io/problems/duplicate-integer
         for i in nums:
            if nums.count(i)>1:
               return True
         return False
           #or

          for i in range(0,len(nums)):
              for j in range(1,len(nums)):
                   if nums[i]==nums[j] and i!=j:
                         print(True)
          print(False)
             #or

          hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
           #or
          return len(set(nums)) != len(nums)

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
