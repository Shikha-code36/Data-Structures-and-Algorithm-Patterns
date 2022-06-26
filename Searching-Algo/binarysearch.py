'''
                                                             Binary Search
 Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.
'''
# iterative approach
def binarysearch(list, target):
    left = 0
    right = len(list)-1
    while left <= right:
        mid = (left+right)//2
        if target == list[mid]:
            return mid
        elif target > list[mid]:
            left = mid+1
        else:
            right = mid-1

    return -1


print(binarysearch([2, 3, 4, 5], 5))  # 3

# recursive approach
def binarysearch(list, left, right, target):
    if right >= left:
        mid = (left+right)//2

        if target == list[mid]:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif list[mid] > target:
            return binarysearch(list, left, mid-1, target)
        # Else the element can only be present in right subarray
        else:
            return binarysearch(list, mid+1, right, target)
    else:
        return -1


list = [2, 3, 4, 10, 11, 16, 90, 32, 7]
target = 16
print(binarysearch(list, 0, len(list)-1, target))  # 5
