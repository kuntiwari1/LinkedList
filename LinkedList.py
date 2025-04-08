class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_start_of_loop(head):
    slow = fast = head

    # Step 1: Detect loop using Floyd's Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # No loop found
        return None

    # Step 2: Find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # This is the starting node of the loop

# 🧪 Input: Create a linked list with a loop
if __name__ == "__main__":
    # Create nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    # Link nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3  # 🔁 This creates the loop (node5 → node3)

    # Call the function
    loop_start = find_start_of_loop(node1)

    # Print the result
    if loop_start:
        print("Loop starts at node with data:", loop_start.data)
    else:
        print("No loop found.")
