#Question - https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Brute force would be to go through all the subarrays -> O(n^2)
        #Using Kadane's Algo -> 0(n)
        #Explanation - https://www.youtube.com/watch?v=gwUGDXO5gHU&feature=youtu.be 
        g = nums[0]
        l = nums[0]
        
        for i in range(1,len(nums)):
            l = max(l+nums[i],nums[i])
            g = max(l,g)
                
        return g

def stringToIntegerList(input):
    return json.loads(input)

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
            
            ret = Solution().maxSubArray(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
