class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=''.join(ch for ch in s if ch.isalnum()).lower()
        return strs[::-1]==strs