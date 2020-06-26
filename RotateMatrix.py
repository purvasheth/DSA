#Question - https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       #transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        #reverse
        for row in matrix:
            row.reverse()
            
        # another method is to rotate in a square fashion. Its tricky to implememnt and time complexity is same for both these approaches O(n^2)

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
            matrix = stringToInt2dArray(line)
            
            ret = Solution().rotate(matrix)

            out = int2dArrayToString(matrix)
            if ret is not None:
                print("Do not return anything, modify matrix in-place instead.")
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
