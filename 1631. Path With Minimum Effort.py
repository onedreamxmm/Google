'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.


Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

Solution 1: Dijikstra
Idea:
If we observe, this problem is to find the shortest path from a source cell (0, 0) to a destination cell (m-1, n-1). Here, the shortest path is the one with minimum distance, and distance is defined as maximum absolute difference in heights between two consecutive cells of the path.
Thus, we could use Dijikstra's algorithm which is used to find the shortest path in a weighted graph with a slight modification of criteria for the shortest path, which costs O(E log V), where E is number of edges E = 4*M*N, V is number of veritices V = M*N
Complexity:

Time: O(ElogV) = O(M*N log M*N), where M is the number of rows and N is the number of columns in the matrix.
Space: O(M*N)
'''
import heapq
class Solution:
    def minEffort(self, heights):
        row, col = len(heights), len(heights[0])
        diff = [[float('inf')] * col for _ in range(row)]
        # diff = [[float('inf')] * col] * row    #why wrong????
        # print(diff)
        diff[0][0] = 0
        minHeap = [(0, 0, 0)]  # (difference, row, column)
        while minHeap:
            d, x, y = heapq.heappop(minHeap)
            if x == row - 1 and y == col - 1:
                return d
            for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                if 0 <= r < row and 0 <= c < col:
                    newDiff = max(d, abs(heights[x][y] - heights[r][c]))
                    if diff[r][c] > newDiff:
                        diff[r][c] = newDiff
                        heapq.heappush(minHeap, (diff[r][c], r, c))

if __name__ == '__main__':
    o = Solution()
    heights1 = [[1,2,2],[3,8,2],[5,3,5]]
    heights2 = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    heights3 = [[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]
    print(o.minEffort(heights1))
    print(o.minEffort(heights2))
    print(o.minEffort(heights3))