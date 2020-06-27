#Question - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute Force is to just go over every possible combination and get max
        #i -> 0 to n
        #j -> i+1 to n
        #O(n^2)
        
        #using 2 variables maxprofit and minprice
        if(len(prices)==0):
            return 0
        minprice = prices[0]
        maxprofit = 0
        for i in range(1,len(prices)):
            minprice = min(prices[i],minprice)
            maxprofit = max(maxprofit,prices[i]-minprice)
            
        return maxprofit

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
            prices = stringToIntegerList(line);
            
            ret = Solution().maxProfit(prices)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
