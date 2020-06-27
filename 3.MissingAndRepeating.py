# Question - https://www.hackerrank.com/contests/kcertc/challenges/find-the-repeating-and-the-missing

#Brute force approach. counts stores the counts of all the numbers Complexity -
# import collections
# def findMissingAndRepeat(nums):
#     counts = collections.Counter(nums)
#     miss = 0
#     repeat = 0
#     for i in range(1,len(nums)+1):
#         if i not in counts.keys():
#             miss = i
#             break
#     for k in counts.keys():
#         if(counts[k]!=1):
#             repeat = k
#             break
#     return repeat,miss

#O(n) without extra datastructure (visit and mark)
def findMissingAndRepeat(nums):
    miss = 0
    repeat = 0
    for i in range(1,len(nums)+1):
        if(i not in nums):
            miss = i
            break

    for n in nums:
        index = abs(n)-1
        if(nums[index]<0):
            repeat = index+1
            break
        else:
            nums[index] = - nums[index]

    return repeat,miss

# Other method mentioned on gfg include sorting and traversing
# if we consider always only 1 element is missing, other approaches like xor and sum+ product can be used.
# https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

def main():

    n = input()
    s = input()
    nums = s.split()
    nums = [int(n) for n in nums]
    repeat,miss = findMissingAndRepeat(nums)
    print(str(miss)+","+str(repeat))

if __name__ == '__main__':
    main()
