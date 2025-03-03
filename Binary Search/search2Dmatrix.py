class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bot = 0, len(matrix)-1

        while bot >= top:
            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = bot - 1
            else: 
                break
        
        if not(bot >= top):
            return False
        
        row = (top + bot) // 2
        l, r = 0, len(matrix[row])-1
        
        while r >= l:
            m = (l + r) // 2

            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True
        
        return False
