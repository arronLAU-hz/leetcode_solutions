class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last_idx = {}
        left = 0
        ans = 0

        for right, ch in enumerate(s):

            if ch in last_idx and last_idx[ch] >= left:
                left = last_idx[ch] + 1

            last_idx[ch] = right

            ans = max(ans, right - left + 1)

        return ans


if __name__ == "__main__":
    cases = ["abcabcbb", "bbbbb", "pwwkew", "", "dvdf"]
    for s in cases:
        print(s, "->", Solution().lengthOfLongestSubstring(s))