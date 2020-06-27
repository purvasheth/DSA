#Question - https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#Not efficient with space O(1)        
#         def set_zero(visit):
#             [i,j] = visit.pop()
#             for col in range(0,len(matrix[0])):
#                 if matrix[i][col]==0:
#                     visit.append([i,col])
#                 matrix[i][col]='-'
#             for row in range(0,len(matrix)):
#                 if matrix[row][j]==0:
#                     visit.append([row,j])
#                 matrix[row][j] = '-'
                
#         cols = len(matrix[0])
#         rows = len(matrix)
#         visit = []
#         for i in range(rows):
#             for j in range(cols):
#                 if(matrix[i][j]==0):
#                     #print(i,j)
#                     visit.append([i,j])
#                     set_zero(visit)
#                     while(len(visit)!=0):
#                         set_zero(visit)

#         #print(matrix)
#         for i in range(rows):
#             for j in range(cols):
#                 if(matrix[i][j]=='-'):
#                     matrix[i][j]=0

#More efficient with space O(1)

        rows = len(matrix)
        cols = len(matrix[0])
        flag_row = False
        flag_col = False

        for i in range(rows):
            if matrix[i][0]!='-':
                for j in range(cols):
                    if matrix[i][j]==0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
                        if i==0:
                            flag_row = True
                        if j==0:
                            flag_col = True
                            
        for i in range(1,rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j]=0
        for j in range(1,cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j]=0
        if(flag_col):
            for i in range(rows):
                matrix[i][0] = 0
        if(flag_row):
            for j in range(cols):
                matrix[0][j] = 0

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
            
            ret = Solution().setZeroes(matrix)

            out = int2dArrayToString(matrix)
            if ret is not None:
                print ("Do not return anything, modify matrix in-place instead.")
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
