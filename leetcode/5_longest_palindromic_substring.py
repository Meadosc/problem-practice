class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome_list = []
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                pal = s[i:j]
                if self.isPalindrome(pal):
                    palindrome_list.append(pal)
        return max(palindrome_list, key=len)
        
        
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            last_index = len(s) - i - 1
            first = s[i]
            last = s[last_index]
            if first != last:
                return False
        return True
            
            
        
# INCOMPLETE