'''
                                Linear Search 
Linear search is also called as sequential search algorithm. It is the simplest searching algorithm. In Linear search, we simply traverse the list completely and match each element of the list with the item whose location is to be found. If the match is found, then the location of the item is returned; otherwise, the algorithm returns NULL.
'''
#iterative approach
def linearsearch(list,target):
    for i in range(len(list)):
        if target==list[i]:
            return i
    return -1

list = [1,2,4,5,8]
print(linearsearch(list,8)) #4

#recursive approach
def linearsearch(list,curr_index,target):
    if curr_index == -1:
        return -1
    if list[curr_index] == target:
        return curr_index
    return linearsearch(list, curr_index-1,target)

list = [1,2,4,5,8]
print(linearsearch(list,len(list)-1,8)) #4
