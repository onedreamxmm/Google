'''
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.


Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].

'''


'''
Approach1:
time complexity: O(mn), m, n = len(S), len(T)
space complexity: O(m+n)
'''
from collections import defaultdict
class Solution:
    def minWindow1(self, S, T):
        n = len(T)
        dp = [-1 for i in range(n)]
        length = float('inf')
        dic = defaultdict(list)

        for i, c in enumerate(T):
            dic[c].append(i)

        for idx, c in enumerate(S):
            if c not in dic:
                continue
            for i in dic[c][::-1]:
                if i == 0:
                    dp[0] = idx
                else:
                    dp[i] = dp[i - 1]
                if i == n - 1 and dp[i] >= 0 and idx - dp[i] + 1 < length:
                    start = dp[i]
                    length = idx - dp[i] + 1

        if dp[-1] == -1:
            return ''
        return S[start: start + length]


    def minWindow2(self, S, T):
        # Find - Get ending point of subsequence starting after S[s]
        def find_subseq(s):
            t = 0
            while s < len(S):
                if S[s] == T[t]:
                    t += 1
                    if t == len(T):
                        break
                s += 1
            return s if t == len(T) else None  # Ensure last character of T was found before loop ended

        # Improve - Get best starting point of subsequence ending at S[s]
        def improve_subseq(s):
            t = len(T) - 1
            while t >= 0:
                if S[s] == T[t]:
                    t -= 1
                s -= 1
            return s + 1

        s, min_len, min_window = 0, float('inf'), ''

        while s < len(S):
            end = find_subseq(s)  # Find end-point of subsequence
            if not end:
                break

            start = improve_subseq(end)  # Improve start-point of subsequence
            if end - start + 1 < min_len:  # Track min length
                min_len = end - start + 1
                min_window = S[start:end + 1]

            s = start + 1  # Start next subsequence search

        return min_window

if __name__ == '__main__':
    o = Solution()
    S = "abcdebdde"
    T = "bde"
    print(o.minWindow1(S, T))
