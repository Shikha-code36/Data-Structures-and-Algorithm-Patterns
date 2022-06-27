'''
                                            Bucket Sort
Bucket Sort is a sorting algorithm that divides the unsorted list elements into several groups called buckets. Each bucket is then sorted by using any of the suitable sorting algorithms or recursively applying the same bucket algorithm.

Finally, the sorted buckets are combined to form a final sorted list.

Average & Best Case Time Complexity: O(n+k)
Worst Case Time Complexity: O(n*n) 
'''
def bucketSort(list):
    bucket = []

    # Create empty buckets
    for i in range(len(list)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in list:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(list)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(list)):
        for j in range(len(bucket[i])):
            list[k] = bucket[i][j]
            k += 1
    return list


list = [.42, .32, .33, .52, .37, .47, .51]
print(bucketSort(list)) #[0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]