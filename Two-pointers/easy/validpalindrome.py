"Leetcode - https://leetcode.com/problems/valid-palindrome/"
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            
            i+=1
            j-=1
        return True
        
#T:O(N)
#S:O(1)