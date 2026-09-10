class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_start = 0
        longest_end = 0

        def expand(left, right):
            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                left -= 1
                right += 1

            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindrome: "racecar"
            left1, right1 = expand(i, i)

            # Even-length palindrome: "abba"
            left2, right2 = expand(i, i + 1)

            if right1 - left1 > longest_end - longest_start:
                longest_start = left1
                longest_end = right1

            if right2 - left2 > longest_end - longest_start:
                longest_start = left2
                longest_end = right2

        return s[longest_start:longest_end + 1]
        