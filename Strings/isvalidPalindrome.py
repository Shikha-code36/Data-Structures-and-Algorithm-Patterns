"Leetcode - https://leetcode.com/problems/valid-palindrome/"
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''


def isPalindrome(self, s):
    filtered_char = filter(lambda c: c.isalnum(), s)
    low_filterchar = map(lambda c: c.lower(), filtered_char)
    filt = list(low_filterchar)
    if filt == filt[::-1]:
        return True
    else:
        return False
