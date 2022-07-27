"Leetcode- https://leetcode.com/problems/reverse-string/ "
'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
'''
def reverseString(s):
        i=0
        j=len(s)-1
        
        while i<=j:
            s[i],s[j]=s[j],s[i]
            i,j = i+1,j-1

        return s

#T:O(N)
#S:O(1)