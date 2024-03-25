class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False

# Example usage:
# Create the linked list
head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1  # This creates the cycle

# Check if the linked list has a cycle
print(hasCycle(head))  # Output: True
