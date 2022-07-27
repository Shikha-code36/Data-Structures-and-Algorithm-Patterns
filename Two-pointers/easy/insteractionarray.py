"Leetcode- https://leetcode.com/problems/intersection-of-two-arrays/ "
'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
'''


def intersection(self, nums1, nums2):
    nums1.sort()
    nums2.sort()

    i = 0
    j = 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if i > 0 and nums1[i] == nums1[i-1]:
            i += 1
            continue
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
    return res

# T:O(N)
# S:O(N)


def intersection(self, nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set2 & set1)
# T:O(N+M)
# S:O(N+M)
