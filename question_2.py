class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    if not head or not head.next:
        return None
    
    # Check if there's a cycle
    slow = head
    fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            has_cycle = True
            break
    
    # If there's no cycle, return None
    if not has_cycle:
        return None
    
    # Find the starting node of the cycle
    slow = head
    
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

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

# Find the starting node of the cycle
start_of_cycle = detectCycle(head)
if start_of_cycle:
    print("Tail connects to node index", start_of_cycle.val)
else:
    print("No cycle")
