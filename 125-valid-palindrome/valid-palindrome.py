class Solution:
    def isPalindrome(self, s: str) -> bool:
        right=len(s)-1
        for index,ch in enumerate(s):
            if index > right:
                break
            if ch.isalnum():
                while not s[right].isalnum():
                    right -= 1
                if ch.lower() !=  s[right].lower():
                    return False
                right -= 1
        return True

