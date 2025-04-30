class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

def printList(head):
    temp = head
    if temp is None:
        return
    while temp is not None:
        print(temp.item, end=" ")
        temp = temp.next
    print()

def findNode(ll, index):
    if ll is None or index < 0 or index >= ll.size:
        return None
    temp = ll.head
    while index > 0:
        temp = temp.next
        if temp is None:
            return None
        index -= 1
    return temp

def insertNode(ll, index, value):
    if ll is None or index < 0 or index > ll.size:
        return -1
    if ll.head is None or index == 0:
        cur = ll.head
        ll.head = ListNode(value)
        ll.head.next = cur
        if ll.size == 0:
            ll.tail = ll.head
        ll.size += 1
        return 0
    if index == ll.size:
        pre = ll.tail
        pre.next = ListNode(value)
        ll.tail = pre.next
        ll.size += 1
        return 0
    pre = findNode(ll, index - 1)
    if pre is not None:
        cur = pre.next
        pre.next = ListNode(value)
        pre.next.next = cur
        if index == ll.size:
            ll.tail = pre.next
        ll.size += 1
        return 0
    return -1

def removeNode(ll, index):
    if ll is None or index < 0 or index >= ll.size:
        return -1
    if index == 0:
        cur = ll.head.next
        ll.head = cur
        ll.size -= 1
        if ll.size == 0:
            ll.tail = None
        return 0
    pre = findNode(ll, index - 1)
    if pre is not None:
        if index == ll.size - 1:
            ll.tail = pre
            pre.next = None
        else:
            cur = pre.next.next
            pre.next = cur
        ll.size -= 1
        return 0
    return -1

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        insertNode(self.ll, 0, item)

    def pop(self):
        if self.isEmpty():
            return None
        item = self.ll.head.item
        removeNode(self.ll, 0)
        return item

    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.item

    def isEmpty(self):
        return self.ll.size == 0

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, item):
        insertNode(self.ll, self.ll.size, item)

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.ll.head.item
        removeNode(self.ll, 0)
        return item

    def isEmpty(self):
        return self.ll.size == 0

def palindrome(word):
#Write your code here #

if __name__ == "__main__":
    print("Sample String : A man a plan a canal Panama")
    palindrome("A man a plan a canal Panama")
    print("Sample String : Superman in the sky")
    palindrome("Superman in the sky")