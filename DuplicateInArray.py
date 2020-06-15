class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #gives TLE. Complexity less than O(n^2)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]==nums[j]):
        #             return nums[i]
        # return -1
        
        #New Approach - Tortoise and hare.
#         fast = nums[0]
#         slow = nums[0]
#         while True:
#             fast = nums[nums[fast]]
#             slow = nums[slow]
#             if(fast==slow):
#                 break
                
#         slow = nums[0]
#         while(fast!=slow):
#             slow= nums[slow]
#             fast = nums[fast]
#         return fast
        
    #Last most efficient just O(n)
    
        for n in nums:
            if(nums[abs(n)]<0):
                return abs(n)
            nums[abs(n)] = -nums[abs(n)]
        
        return None
