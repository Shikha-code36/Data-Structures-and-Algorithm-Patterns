'''
                                Linear Search 
Linear search is also called as sequential search algorithm. It is the simplest searching algorithm. In Linear search, we simply traverse the list completely and match each element of the list with the item whose location is to be found. If the match is found, then the location of the item is returned; otherwise, the algorithm returns NULL.
'''

def linearsearch(n,t):
    for i in range(len(n)):
        if t==n[i]:
            return i
    return -1

a = [1,2,4,5,8]
print(linearsearch(a,8)) #4