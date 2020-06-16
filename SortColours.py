class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        curr = 0
        right = len(nums)-1
        while(curr<=right):
            if(curr>left and nums[curr]==0):
                nums[curr],nums[left] = nums[left],nums[curr]
                left = left + 1
            elif(nums[curr]==2):
                nums[right],nums[curr] = nums[curr],nums[right]
                right = right - 1
            else:
                curr = curr + 1

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
            
            ret = Solution().sortColors(nums)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
