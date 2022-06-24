'''
                                        Merge Sort  

Merge sort is a Divide and Conquer based Algorithm. It divides the input array into two-parts, until the size of the input array is not ‘1’. In the return part, it will merge two sorted arrays a return a whole merged sorted array.

This is the recursive approach for implementing merge sort. The steps needed to obtain the sorted array through this method can be found below:

1.The list is divided into left and right in each recursive call until two adjacent elements are obtained.

2.Now begins the sorting process. The i and j iterators traverse the two halves in each call. The k iterator traverses the whole lists and makes changes along the way.

3.If the value at i is smaller than the value at j, left[i] is assigned to the arr[k] slot and i is incremented. If not, then right[j] is chosen.

4.This way, the values being assigned through k are all sorted.

5.At the end of this loop, one of the halves may not have been traversed completely. Its values are simply assigned to the remaining slots in the list.

And with that, the merge sort has been implemented!

Time Complexity - O(nlogn)

'''

def mergesort(arr):
    if len(arr)>1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]

        #recursion
        mergesort(left)
        mergesort(right)

        #merge
        i=0 #left array index
        j=0 #right array index
        k=0 #merged array index

        #to look at every element in the right array and transfer every element from the right to the merged array
        while i<len(left) and j<len(right):
            if left[i] <right[j]:
                arr[k] = left[i]
                i += 1
                #k += 1
            else:
                arr[k] = right[j]
                j += 1
                #k += 1
            k += 1 #in both cases we need to increment k

        #to look at every element in the left array and transfer every element from the left to the merged array
        while i<len(left): #because there's element  missing from the left array to transfer
            arr[k] = left[i]
            i += 1
            k += 1

        while j<len(right): #to check if we are not at the end of array
            arr[k] = right[j]
            j += 1
            k += 1
    
    return arr

print(mergesort([8, 3, 5, 6, 11, 19, 7])) #[3, 5, 6, 7, 8, 11, 19]
        


