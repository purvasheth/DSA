#Question - https://leetcode.com/problems/merge-sorted-array/

def insert(arr,n,key,index):
    for i in range(n,index-1,-1):
        arr[i] = arr[i-1]
    arr[index]=key
    
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i =0
        j = 0
    
        while(i<m and j<n):
            if(nums2[j]<nums1[i]):
                insert(nums1,m,nums2[j],i)
            else:
                while(i<m and nums2[j]>nums1[i]):
                    i=i+1
                insert(nums1,m,nums2[j],i)
            #print(i,j,nums2[j],m)
            #print(nums1)
            i=i+1
            j=j+1
            m=m+1
     
        while(j<n):
            insert(nums1,m,nums2[j],m) 
            j = j+1
            m = m+1

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
            nums1 = stringToIntegerList(line);
            line = next(lines)
            m = int(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);
            line = next(lines)
            n = int(line);
            
            ret = Solution().merge(nums1, m, nums2, n)

            out = integerListToString(nums1)
            if ret is not None:
                print "Do not return anything, modify nums1 in-place instead."
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
