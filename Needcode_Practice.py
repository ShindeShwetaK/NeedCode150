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
#######################################################################################
#Q2.
