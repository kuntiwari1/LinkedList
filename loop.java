class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class LoopStartFinder {

    // Function to detect the start of the loop
    public static Node findStartOfLoop(Node head) {
        Node slow = head;
        Node fast = head;

        // Step 1: Detect loop using Floyd's Cycle Detection
        while (fast != null && fast.next != null) {
            slow = slow.next;          // move by 1
            fast = fast.next.next;     // move by 2

            if (slow == fast) {        // cycle detected
                break;
            }
        }

        // If no loop was found
        if (fast == null || fast.next == null) {
            return null;
        }

        // Step 2: Move one pointer to head
        fast = head;

        // Move both one step at a time to find loop start
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }

        return slow; // This is the start of the loop
    }

    public static void main(String[] args) {
        // Create nodes
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        head.next.next.next.next.next = new Node(6);

        // Create a loop: 6 -> 3
        head.next.next.next.next.next.next = head.next.next;

        Node loopStart = findStartOfLoop(head);

        if (loopStart != null) {
            System.out.println("Loop starts at node with value: " + loopStart.data);
        } else {
            System.out.println("No loop detected.");
        }
    }
}
