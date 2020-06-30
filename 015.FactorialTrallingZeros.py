#question - https://leetcode.com/problems/factorial-trailing-zeroes/
#solution - https://leetcode.com/problems/factorial-trailing-zeroes/discuss/711946/Very-simple-solution-wvideo-whiteboard-explanation
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num_fives = 0
        ans = 0
        m = n
        while(m>0):
            num_fives = num_fives + 1
            ans = ans + n//pow(5,num_fives)
            #print(ans)
            m = m//5
            
        return ans

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
            n = int(line);
            
            ret = Solution().trailingZeroes(n)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
