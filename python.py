class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def detect_loop_start(head):
    slow = head
    fast = head

    # Step 1: Detect loop using Floyd’s algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # If no loop
    if not fast or not fast.next:
        return None

    # Step 2: Find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # This is the start of the loop
