class Solution:
    def longestPalindrome(self, s: str) -> str:
        # put string in que. Or deque? Either way, I want to pop from the front and back to compare.
        # Let's do it the simple way first. Loop through each character, add to a palindrome, check if it's a palindrome
        # also, I'll need to store all the legal palindromes and check which is longest
        
        self.isPalindrome(s)

        pal = ""
        for ch in s:
            #print(ch)
            temp = pal + s
        
    def isPalindrome(self, s: str) -> bool:

        for i in range(len(s) // 2):
            last_index = len(s) - i - 1
            first = s[i]
            last = s[last_index]
            #print(f"{i}: {first}, {last_index}: {last}")
            if first != last:
                return False
        return True
            
            
# INCOMPLETE