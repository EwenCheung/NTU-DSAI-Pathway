class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def insertInEmptyList(self, data):
        if self.head is not None:
            print("This list is not empty")
            return self.head

        new_node = Node(data)
        new_node.next = new_node
        self.head = new_node
        return self.head

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = self.last = new_node
            return self.head

        new_node.next = self.head
        self.last.next = new_node
        self.head = new_node
        return self.head

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = self.last = new_node
            return self.head

        self.last.next = new_node
        new_node.next = self.head
        self.last = new_node
        return self.head

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if self.head is None:
            if position != 1:
                print("Out of bound: Invalid position")
                return self.head
            new_node.next = new_node
            self.head = self.last = new_node
            return self.head

        if position < 1:
            print("Invalid Position")
            return self.head

        if position == 1:
            self.last.next = new_node
            new_node.next = self.head
            self.head = new_node
            return self.head

        prev = self.head
        count = 1
        while count < position - 1:
            prev = prev.next
            count += 1
            if prev == self.head:
                print("Out of bound")
                return self.head

        new_node.next = prev.next
        prev.next = new_node

        if prev == self.last:
            self.last = new_node

        return self.head

    def delete_first_node(self):
        if self.head is None:
            print("The list is empty")
            return None

        if self.head.next == self.head:
            self.head = self.last = None
            return None

        self.head = self.head.next
        self.last.next = self.head
        return self.head

    def delete_last_node(self):
        if self.head is None:
            print("The list is empty")
            return None

        if self.head.next == self.head:
            self.head = self.last = None
            return None

        second_last = self.head
        while second_last.next != self.last:
            second_last = second_last.next

        second_last.next = self.head
        self.last = second_last
        return self.head

    def delete_position(self, position):
        if self.head is None:
            print("The list is empty")
            return None

        if position < 1:
            print("Invalid Position")
            return self.head

        if self.head.next == self.head:
            if position == 1:
                self.head = self.last = None
                return None
            print("Out of bound: Invalid")
            return self.head

        if position == 1:
            self.head = self.head.next
            self.last.next = self.head
            return self.head

        prev = self.head
        count = 1
        while count < position - 1:
            prev = prev.next
            count += 1
            if prev == self.head:
                print("Out of bound")
                return self.head

        if prev.next == self.last:
            prev.next = self.head
            self.last = prev
            return self.head

        prev.next = prev.next.next
        return self.head

    def delete_specific_node(self, key):
        if self.head is None:
            print("The list is empty")
            return None

        prev = self.last
        current = self.head

        # Case 1: Deleting the only node in the list
        if self.head.next == self.head and current.data == key:
            self.head = self.last = None
            return None


        while True:
            if current.data == key:
                prev.next = current.next
                if current == self.head:
                    self.head = current.next
                if current == self.last:
                    self.last = prev
                return self.head

            prev = current
            current = current.next

            if current == self.head:
                break

        print(f"Node with data {key} not found.")
        return self.head

    def delete_all_occurrences(self, key):
        if self.head is None:
            print("The list is empty")
            return

        prev = self.last
        current = self.head
        found = False

        # Handle head nodes with the target value
        while self.head and self.head.data == key:
            found = True
            if self.head.next == self.head:
                self.head = self.last = None
                return
            prev.next = self.head.next
            self.head = self.head.next

        # Traverse and handle remaining nodes
        while current != self.last:
            if current.next.data == key:
                found = True
                if current.next == self.last:
                    self.last = current
                current.next = current.next.next
            else:
                current = current.next

        if not found:
            print(f"Node with data {key} not found.")

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end="-->")
            current = current.next
            if current == self.head:
                break
        print()


ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(8)
ll.insert_at_beginning(5)
ll.insert_at_beginning(5)
ll.insert_at_beginning(5)
ll.insert_at_beginning(5)
ll.insert_at_beginning(5)
ll.insert_at_beginning(5)
ll.insert_at_beginning(6)
ll.insert_at_beginning(5)
ll.insert_at_beginning(5)
ll.insert_at_end(7)
ll.insert_at_end(5)

ll.print_list()

ll.delete_specific_node(5)

ll.print_list()