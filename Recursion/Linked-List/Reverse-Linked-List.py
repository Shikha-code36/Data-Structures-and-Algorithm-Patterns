'''
Given pointer to the head node of a linked list, the task is to recursively reverse the linked list. We need to reverse the list by changing links between nodes.

Examples:

Input : Head of following linked list  
       1->2->3->4->NULL
Output : Linked list should be changed to,
       4->3->2->1->NULL

'''


'''Recursive Approach'''


def reverseList(head):

    if not head:
        return None

    newHead = head  # head is current node that we are at in our recursive call
    if head.next:  # if we keep reversing
        newHead = reverseList(head.next)  # now the result will be new head
        head.next.next = head  # reversing the link between the next node and head
    head.next = None  # if head happens to be the first node in the list we're setting the next pointer to null

    return newHead  # reverse the list and return the new head


'''Iterative Approach'''


def reverseList(head):
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
