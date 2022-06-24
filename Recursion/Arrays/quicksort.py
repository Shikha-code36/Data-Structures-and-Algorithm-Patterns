'''
                                Quick Sort

Divide and conquer: Quicksort splits the array into smaller arrays until it ends up with an empty array, or one that has only one element, before recursively sorting the larger arrays.

The basic version of the algorithm does the following:

Divide the collection in two (roughly) equal parts by taking a pseudo-random element and using it as a pivot.

Elements smaller than the pivot get moved to the left of the pivot, and elements larger than the pivot to the right of it.

This process is repeated for the collection to the left of the pivot, as well as for the array of elements to the right of the pivot until the whole array is sorted.

Time Complexity - O(n^2)

'''


def quicksort(arr,left,right):
    if left<right:
        partition_pos = partition(arr,left,right)
        quicksort(arr,left,partition_pos-1)
        quicksort(arr,partition_pos+1,right)
    return arr

#this function returns the index of the pivot element
#after the first step of quicksort, when we have this index in partition_pos we can call quicksort on the original array 
# from index left to index partition position minus onewhich just means that we call quicksort on all elements that are less than the pivot element 
#we can call quick sort on the array from partition position plus one to the right so we call quicksort on the sub-array that contains all elements that are greater than the pivot element
def partition(arr,left,right): 
    i = left
    j = right-1
    pivot = arr[right] # choose the rightmost element as pivot

    #i moves to the right and j moves to the left until i and j cross will be checked by this while loop
    while i<j:
        while i<right and arr[i] < pivot: #i to the right while i is not at the end of the array and element is less than pivot we increase i
            i+=1
        while j>left and arr[i] >= pivot: #similiar for j  decrease j because j moves to the left
            j-=1

        if i<j: #if i and j didn't cross we swap elements
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i]>pivot: #if i and j crossed means element at i is greater than pivot then do swap those elements
        arr[i],arr[right] = arr[right],arr[i]

    return i  #to determine where to split the array to call quick sort recursively

arr=[7,9,10,3,5,12,90,43]
print(quicksort(arr,0,len(arr)-1)) #[5, 7, 9, 3, 10, 12, 43, 90]


