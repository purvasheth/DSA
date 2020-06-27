#Question - https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #DP problem - use the previous row to get next 
        if(numRows==0):
            return None
        
        ans = [[1,1] for i in range(numRows) ]
        ans[0].pop() # as first row only has one 1
        
        for i in range(2,numRows):
            for j in range(len(ans[i-1])-1):
                ans[i].insert(j+1,ans[i-1][j]+ans[i-1][j+1])
        return ans

def stringToInt(input):
    return int(input)

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
            numRows = stringToInt(line)
            print(numRows)
            ret = Solution().generate(numRows)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
