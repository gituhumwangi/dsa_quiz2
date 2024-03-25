class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Example usage:
# Create the linked list
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)

head.next = node1
node1.next = node2
node2.next = node3

# Reverse the linked list
reversed_head = reverseLinkedList(head)

# Print the reversed linked list
while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next
