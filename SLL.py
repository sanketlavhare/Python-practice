
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create linked list by inserting at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Traverse and print node values
    def print_list(self):
        current = self.head
        values = []

        while current:
            values.append(str(current.data))
            current = current.next

        print("Linked List:", " -> ".join(values))

    # Insert a node at a given position
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position < 1:
            return

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 1

        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            return

        new_node.next = current.next
        current.next = new_node

    # Find the middle node
    def find_middle(self):
        slow = self.head
        fast = self.head

        if self.head is None:
            return None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    # Delete a node by value
    def delete_node(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if current is None:
            return

        previous.next = current.next

    # Reverse the linked list
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # Sum of every two consecutive node values
    def consecutive_sums(self):
        current = self.head
        result = []

        while current and current.next:
            result.append(current.data + current.next.data)
            current = current.next

        print("Sum of Consecutive Nodes:", *result)


def solution():
    ll = LinkedList()

    # Create linked list
    for value in [10, 20, 30, 40, 50]:
        ll.append(value)

    print("1. Original Linked List")
    ll.print_list()

    # Insert a node
    print("\n2. After Inserting 25 at Position 3")
    ll.insert_at_position(25, 3)
    ll.print_list()

    # Find middle node
    print("\n3. Finding Middle Number")
    print("Middle Number:", ll.find_middle())

    # Delete a node
    print("\n4. After Deleting Node 25")
    ll.delete_node(25)
    ll.print_list()

    # Reverse linked list
    print("\n5. Reversed Linked List")
    ll.reverse()
    ll.print_list()

    # Sum of consecutive nodes
    print("\n6. Sum of Consecutive Nodes")
    ll.consecutive_sums()


if __name__ == "__main__":
    solution()
