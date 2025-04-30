import random


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_linked_list(self):
        current = self.head

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()

    def search_linked_list(self, target):
        current = self.head
        while current is not None:
            if current.data == target:
                return True
            current = current.next

        return False

    def find_length(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next

        return length

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return self.head

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return self.head

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

        return self.head

    def insert_at_position(self, value, position):
        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return self.head

        prev = self.head
        count = 1

        while count < position - 1 and prev is not None:
            prev = prev.next
            count += 1

        if prev is None:
            print("Invalid Position")
            return

        new_node = Node(value)
        new_node.next = prev.next
        prev.next = new_node
        return self.head

    def delete_at_beginning(self):
        if self.head is None:
            return None
        self.head = self.head.next
        return self.head

    def delete_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return None

        second_last = self.head
        while second_last.next.next is not None:
            second_last = second_last.next

        second_last.next = None

        return self.head

    def delete_at_position(self, position):
        if self.head is None or position < 1:
            return None
        if position == 1:
            self.head = self.head.next
            return self.head

        prev = self.head
        count = 1
        while count < position - 1 and prev is not None:
            prev = prev.next
            count += 1

        if prev is None or prev.next is None:
            print("Invalid position")
            return self.head

        prev.next = prev.next.next

        return self.head

    # traverse_linked_list() same as this function
    def print_linked_list(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + "-->"
            current = current.next
        result += "None"
        print(result)


ll = LinkedList()
for i in range(50):
    ll.insert_at_beginning(random.randint(1, 100))

# can play around with linked list
# ll.print_linked_list()
# ll.delete_at_position(2)
# ll.print_linked_list()
# ll.delete_at_position(4)
# ll.insert_at_beginning(30)
# ll.print_linked_list()
