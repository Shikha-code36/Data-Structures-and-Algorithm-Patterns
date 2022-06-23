'''
                                        Tower of Hanoi
Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 
1) Only one disk can be moved at a time. 
2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack. 
3) No disk may be placed on top of a smaller disk.

ALGO-

1-Create a tower_of_hanoi recursive function and pass two arguments: the number of disks n and the name of the rods such as source, aux, and target.
2-We can define the base case when the number of disks is 1. In this case, simply move the one disk from the source to target and return.
3-Now, move remaining n-1 disks from source to auxiliary using the target as the auxiliary.
4-Then, the remaining 1 disk move on the source to target.
5-Move the n-1 disks on the auxiliary to the target using the source as the auxiliary.

'''


def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", target)
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print("Move disk", n, "from source", source, "to destination", target)
    tower_of_hanoi(n-1, auxiliary,  source, target)


print(tower_of_hanoi(4, 'A', 'B', 'C'))
# Move disk 1 from source A to destination B
# Move disk 2 from source A to destination C
# Move disk 1 from source B to destination C
# Move disk 3 from source A to destination B
# Move disk 1 from source C to destination A
# Move disk 2 from source C to destination B
# Move disk 1 from source A to destination B
# Move disk 4 from source A to destination C
# Move disk 1 from source B to destination C
# Move disk 2 from source B to destination A
# Move disk 1 from source C to destination A
# Move disk 3 from source B to destination C
# Move disk 1 from source A to destination B
# Move disk 2 from source A to destination C
# Move disk 1 from source B to destination C
