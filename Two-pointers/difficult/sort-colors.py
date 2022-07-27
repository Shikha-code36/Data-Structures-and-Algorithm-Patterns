"Leetcode- https://leetcode.com/problems/sort-colors/ "
'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''
def sortColors(self, nums):
        l=0
        r=len(nums)-1
        m=0
        
        while m<=r:
            if nums[m]==0:
                nums[m],nums[l]=nums[l],nums[m]
                l+=1
                m+=1
            elif nums[m]==2:
                nums[m],nums[r]=nums[r],nums[m]
                r-=1
            else:
                m+=1
        return nums

#T=O(n)
#S=O(1)