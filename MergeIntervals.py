#https://leetcode.com/problems/merge-intervals/
class Solution:
        def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            intervals = sorted(intervals) #sorts according to start time
            i = 1
            while(i<len(intervals)):
                if intervals[i-1][1]>=intervals[i][0]:
                    intervals[i][0]=intervals[i-1][0]
                    intervals[i][1]=max(intervals[i][1],intervals[i-1][1])
                    intervals.pop(i-1)
                else:
                    i = i+1
            return intervals

    
def stringToInt2dArray(input):
    return json.loads(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            intervals = stringToInt2dArray(line)
            
            ret = Solution().merge(intervals)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
