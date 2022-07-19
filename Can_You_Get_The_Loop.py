# You are given a node that is the beginning of a linked list. 
# This list always contains a tail and a loop. Your objective is to determine the length of the loop.
def loop_size(node):
    slow, fast = node.next, node.next.next
    
    while slow != fast:
        slow = slow.next
        fast = fast.next.next

    count = 1
    fast = fast.next
    while slow != fast:
        count += 1
        fast = fast.next

    return count
