#Question - https://leetcode.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
# Brute force is to store all the permutations and giving the next in a circular fashion
#         def sort_part(start):
#             #sorting only part of array
#             for i in range(start,len(nums)):
#                 m = min(nums[i:len(nums)])
#                 j = [x for x in range(i,len(nums)) if nums[x] == m][0] 
#                 #index gives the first occurence of the min element in list. Avoid that.
#                 nums[j],nums[i] = nums[i],nums[j]
        
#         def suffle(i):
#             #find element just bigger than element at i and sort the rest
#             m = 9999999999
#             new_j = 0
#             for j in range(i+1,len(nums)):
#                 if(nums[j]>nums[i]):
#                     if(m>nums[j]):
#                         m = nums[j]
#                         new_j = j
           
#             nums[i],nums[new_j] = nums[new_j],nums[i]
#             sort_part(i+1)
            
#         flag = 0
#         for i in range(len(nums)-2,-1,-1):
#             if nums[i] < nums[i+1]:
#                 #find the element whose next is greater than itself
#                 suffle(i)
#                 flag = 1
#                 break
#         if(flag==0):
#             nums.sort()

# # more efficient, no sorting is needed only reversal of remaining list would work. So then complexity is O(n) rather than O(n^2) 

        def suffle(i):
            #find element just bigger than element at i and sort the rest
            m = 9999999999
            new_j = 0
            for j in range(i+1,len(nums)):
                if(nums[j]>nums[i]):
                    if(m>=nums[j]):
                        m = nums[j]
                        new_j = j
           
            nums[i],nums[new_j] = nums[new_j],nums[i]
            nums[i+1:] = nums[i+1:][::-1]
            
        flag = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                #find the element whose next is greater than itself
                suffle(i)
                flag = 1
                break
        if(flag==0):
            nums.sort()

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().nextPermutation(nums)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
