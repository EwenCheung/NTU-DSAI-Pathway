class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

def printList(head):
    print("Current List:", end=" ")
    cur = head
    while cur is not None:
        print(cur.item, end=" ")
        cur = cur.next
    print()

def findNode(head, index):
    if head is None or index < 0:
        return None
    cur = head
    while index > 0:
        cur = cur.next
        if cur is None:
            return None
        index -= 1
    return cur

def insertNode(ptrHead, index, item):
    newNode = ListNode(item)
    if index == 0:
        newNode.next = ptrHead[0]
        ptrHead[0] = newNode
        return True

    pre = findNode(ptrHead[0], index - 1)
    if pre is not None:
        newNode.next = pre.next
        pre.next = newNode
        return True
    return False

def removeNode(ptrHead, index):
    current = ptrHead
    for i in range()


if __name__ == "__main__":
    head = None
    ptrHead = [head]
    size = 0

    print("Enter a list of numbers, terminated by any non-digit character:")
    while True:
        try:
            item = int(input())
            if insertNode(ptrHead, size, item):
                size += 1
        except ValueError:
            break

    printList(ptrHead[0])

    while True:
        try:
            index = int(input("Enter the index of the node to be removed: "))
            if removeNode(ptrHead, index):
                size -= 1
                print("After the removal operation:")
                printList(ptrHead[0])
            else:
                print("The node cannot be removed.")
                break
        except ValueError:
            break

    printList(ptrHead[0])
