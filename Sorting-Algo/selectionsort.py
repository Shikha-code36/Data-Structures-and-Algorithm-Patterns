'''
                                        Selection Sort

Selection sort is a sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

Time Complexity - O(n^2)
'''
def selectionSort(list, length):
   
    for step in range(length):
        min_idx = step

        for i in range(step + 1, length):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if list[i] < list[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (list[step], list[min_idx]) = (list[min_idx], list[step])


array = [-2, 45, 0, 11, -9]
length = len(array)
selectionSort(array, length)
print(array) #[-9, -2, 0, 11, 45]