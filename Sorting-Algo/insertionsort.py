'''
                                Insertion Sort
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

Time Complexity - O(n)
'''
def insertionSort(list):

    for step in range(1, len(list)):
        target = list[step]
        j = step - 1
        
        # Compare target with each element on the left of it until an element smaller than it is found
        # For descending order, change target<list[j] to target>list[j].        
        while j >= 0 and target < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        
        # Place target at after the element just smaller than it.
        list[j + 1] = target


list = [9, 5, 1, 4, 3]
insertionSort(list)
print(list) #[1, 3, 4, 5, 9]