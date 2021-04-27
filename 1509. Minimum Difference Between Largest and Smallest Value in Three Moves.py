'''
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.
Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

Example 1:
Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.
Example 2:
Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1].
The difference between the maximum and minimum is 1-0 = 1.
Example 3:
Input: nums = [6,6,0,1,1,4,6]
Output: 2
Example 4:
Input: nums = [1,5,6,14,15]
Output: 1

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

'''

'''
Intuition
If we can do 0 move, return max(A) - min(A)
If we can do 1 move, return min(the second max(A) - min(A), the max(A) - second min(A))
and so on.


Explanation
We have 4 plans:

kill 3 biggest elements
kill 2 biggest elements + 1 smallest elements
kill 1 biggest elements + 2 smallest elements
kill 3 smallest elements


A = [1,5,6,13,14,15,16,17]
n = 8

Case 1: kill 3 biggest elements

All three biggest elements can be replaced with 14
[1,5,6,13,14,15,16,17] -> [1,5,6,13,14,14,14,14] == can be written as A[n-4] - A[0] == (14-1 = 13)

Case 2: kill 2 biggest elements + 1 smallest elements

[1,5,6,13,14,15,16,17] -> [5,5,6,13,14,15,15,15] == can be written as A[n-3] - A[1] == (15-5 = 10)

Case 3: kill 1 biggest elements + 2 smallest elements

[1,5,6,13,14,15,16,17] -> [6,6,6,13,14,15,16,16] == can be written as A[n-2] - A[2] == (16-6 = 10)

Case 4: kill 3 smallest elements

[1,5,6,13,14,15,16,17] -> [13,13,13,13,14,15,16,17] == can be written as A[n-1] - A[3] == (17-13 = 4)

Answer is minimum of all these cases!

'''
import heapq
class Solution:

    def minDifference1(self, nums):
        nums.sort()    #O(nlogn)
        return min(a - b for a, b in zip(nums[-4:], nums[:4]))


    def minDifference2(self, nums):
        arr = zip(heapq.nlargest(4, nums), heapq.nsmallest(4, nums)[::-1])    #O(nlogk), k is 4 here
        return min(a - b for a, b in arr)

'''
Solution 2: Partial Sorting
Time O(NlogK)   in this case, k = 4
Space O(K)
'''


if __name__ == '__main__':
    o = Solution()
    nums1 = [5,3,2,4]
    nums2 = [1, 5, 0, 10, 14]
    nums3 = [6, 6, 0, 1, 1, 4, 6]
    nums4 = [1, 5, 6, 14, 15]
    nums5 = [3]
    print(o.minDifference1(nums1))
    print(o.minDifference1(nums2))
    print(o.minDifference1(nums3))
    print(o.minDifference1(nums4))
    print(o.minDifference1(nums5))
    print(o.minDifference2(nums1))
    print(o.minDifference2(nums2))
    print(o.minDifference2(nums3))
    print(o.minDifference2(nums4))
    print(o.minDifference2(nums5))