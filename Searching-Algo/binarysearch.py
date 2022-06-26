'''
                                                             Binary Search
 Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.
'''

def binarysearch(list,target):
    left=0
    right=len(list)-1
    while left <= right:
        mid = (left+right)//2
        if target == list[mid]:
            return mid
        elif target> list[mid]:
            left=mid+1
        else:
            right=mid-1
            
    return -1

print(binarysearch([2,3,4,5],5)) #3