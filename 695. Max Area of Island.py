'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

'''
from collections import deque
class Solution:
    def maxArea1(self, grid):
        row, col = len(grid), len(grid[0])
        res = 0
        for r in range(row):
            for c in range(col):
                if not grid[r][c]:
                    continue
                queue = deque([(r, c)])
                area = 0
                grid[r][c] = 0
                while queue:
                    xx, yy = queue.popleft()
                    area += 1
                    for x, y in (xx, yy+1), (xx, yy-1), (xx+1, yy), (xx-1, yy):
                        if 0 <= x < row and 0 <= y < col and grid[x][y]:
                            queue.append((x, y))
                            grid[x][y] = 0
                res = max(res, area)
        return res
'''
Approach #1: breadth-First Search
Time Complexity: O(R*C), where R is the number of rows in the given grid, and C is the number of columns. We visit every square once.
Space complexity: O(R*C), the space used by queue.
'''


    def maxArea2(self, grid):
        row , col = len(grid), len(grid[0])
        def dfs(r, c):
            if 0 <= r < row and 0 <= c < col and grid[r][c]:
                grid[r][c] = 0
                return 1 + dfs(r, c+1) + dfs(r, c-1) + dfs(r+1, c) + dfs(r-1, c)
            return 0

        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    res = max(dfs(r, c), res)
        return res
'''
Approach #2: Depth-First Search
Time Complexity: O(R*C), where R is the number of rows in the given grid, and C is the number of columns. We visit every square once.
Space complexity: O(R*C), the space used by the call stack during our recursion.
'''

if __name__ == "__main__":
    o = Solution()
    grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid2 = [[0,0,0,0,0,0,0,0]]
    #print(o.maxArea1(grid1))
    #print(o.maxArea1(grid2))
    print(o.maxArea2(grid1))
    #print(o.maxArea2(grid2))









