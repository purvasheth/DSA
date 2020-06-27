#Question - https://leetcode.com/problems/global-and-local-inversions/
# def merge_sort(arr,temp,left,right):
#     c = 0
#     if(left<right):
#         mid = (left+right)//2
#         c = merge_sort(arr,temp,left,mid)
#         c = c + merge_sort(arr,temp,mid+1,right)
#         c = c+ merge(arr,temp,left,mid,right)
#     return c
# def merge(arr,temp,left,mid,right):
#     i = left
#     j = mid+1
#     k = left
#     c = 0
    
#     while i<=mid and j<=right:
#         if arr[i]<=arr[j]:
#             temp[k] = arr[i]
#             k = k+1
#             i = i+1
#         else:
#             temp[k] = arr[j]
#             c = c+ (mid-i+1)
#             k = k+1
#             j = j+1
#     while(i<=mid):
#         temp[k] = arr[i]
#         k = k+1
#         i = i+1
#     while(j<=right):
#         temp[k] = arr[j]
#         k = k+1
#         j = j+1
#     arr[:] = temp[:]
#     return c
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        #brute force
        # gc = 0
        # for i in range(len(A)):
        #     for j in range(i+1,len(A)):
        #         if(A[i]>A[j]):
        #             gc = gc + 1
        # lc = 0
        # for i in range(len(A)-1):
        #     if(A[i]>A[i+1]):
        #         lc = lc+1
        # #using merge sort for gc
        # temp = []
        # temp[:] = A[:]
        # gc = merge_sort(A,temp,0,len(A)-1)
        # if(len(A)<=1):
        #     gc = 0
        # print(gc)   
        # if (lc==gc):
        #     return True
        # return False
        #using basic logic
        for i, value in enumerate(A):
            if abs(i - value) > 1:
                return False
        return True

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
            A = stringToIntegerList(line);
            
            ret = Solution().isIdealPermutation(A)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
