'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

Example 1:
Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
Example 2:
Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:
Input: n = 21, k = 17, maxPts = 10
Output: 0.73278

Constraints:
0 <= k <= n <= 104
1 <= maxPts <= 104

Intuition:
The same problems as "Climbing Stairs" or "Fibo Sequence".

Explanation:
dp[i] is the probability that we get points i at some moment.
In another word:
1 - dp[i]is the probability that we skip the points i.

The do equation is that:
dp[i] = sum(last W dp values) / W

To get Wsum = sum(last W dp values),
we can maintain a sliding window with size at most W.

Time Complexity:
Time O(N)
Space O(N), can be improve to O(W)
'''


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1
        dp = [1.0] + [0] * n
        pSum = 1.0

        for i in range(1, n + 1):
            dp[i] = pSum / maxPts
            if i < k:
                pSum += dp[i]
            if i - maxPts >= 0:
                pSum -= dp[i - maxPts]

        return sum(dp[k:])