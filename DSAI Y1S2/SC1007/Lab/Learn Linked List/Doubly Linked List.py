class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def forward_traversal(self):
        current = self.head
        while current is not None:
            print(current.data, end="-->")
            current = current.next
        print("None")

    def backward_traversal(self):
        current = self.tail
        while current is not None:
            print(current.data, end="-->")
            current = current.prev
        print("None")

    def find_length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        return self.head

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

        self.tail = new_node

        return self.head

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position < 1:
            print("Invalid Position")
            return self.head

        if position == 1:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
            return self.head

        previous = self.head
        count = 1
        while count < position - 1 and previous is not None:
            previous = previous.next
            count += 1

        if previous is None:
            print("Invalid Position")
            return self.head

        new_node.next = previous.next
        new_node.prev = previous
        if previous.next is not None:
            previous.next.prev = new_node
        else:
            self.tail = new_node
        previous.next = new_node

        return self.head

    def del_head(self):
        if self.head is None:
            return None

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        return self.head

    def del_end(self):
        if self.head is None:
            print("List is already empty")
            return None
        if self.head.next is None:
            self.head = None
            self.tail = None
            return self.head

        current = self.tail
        current.prev.next = None
        self.tail = current.prev
        return self.head

    def del_position(self, position):
        if self.head is None:
            print("List is empty")
            return None

        if position < 1:
            print("Invalid Position")
            return self.head
        if position == 1:
            if self.head.next is None:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return self.head

        prev = self.head
        count = 1
        while count < position - 1 and prev is not None:
            prev = prev.next
            count += 1

        if prev is None or prev.next is None:
            print("Position out of bounds")
            return self.head

        if prev.next.next is None:
            prev.next = None
            self.tail = prev
        else:
            prev.next = prev.next.next
            prev.next.prev = prev

        return self.head

    def del_position2(self, position):
        if self.head is None:
            print("List is empty")
            return None

        if position < 1:
            print("Invalid Position")
            return self.head

        if position == 1:
            if self.head.next is None:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return self.head

        current = self.head
        count = 1
        while count < position and current is not None:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bounds")
            return self.head

        if current.next is None:
            current.prev.next = None
            self.tail = current.prev
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

        return self.head



ll = LinkedList()
ll.head = Node(4)
node2 = Node(5)
node3 = Node(9)

ll.head.next = node2
node2.prev = ll.head
node2.next = node3
node3.prev = node2

# remember to set tail
ll.tail = node3

ll.forward_traversal()
ll.backward_traversal()

ll.insert_at_beginning(2)
ll.insert_at_end(11)

ll.forward_traversal()

ll.insert_at_position(4, 4)

ll.forward_traversal()

ll.del_position(5)
ll.forward_traversal()
