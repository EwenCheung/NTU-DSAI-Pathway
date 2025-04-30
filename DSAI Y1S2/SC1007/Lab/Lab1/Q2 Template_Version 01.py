class ListNode:
    def __init__(self, item):  
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):  
        self.head = None
        self.size = 0

def printList2(ll):
    if ll.head is not None:
        cur = ll.head
        print(f"Current List has {ll.size} elements: ", end="")
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print()

def findNode2(ll, index):
    if ll.head is not None:
        cur = ll.head
        if cur is None or index < 0 or index >= ll.size:
            return None
        while index > 0:
            cur = cur.next
            if cur is None:
                return None
            index -= 1
        return cur
    else:
        return None

def insertNode2(ll, index, item):
    newNode = ListNode(item)
    # If empty list or inserting first node, update head pointer
    if index == 0:
        newNode.next = ll.head
        ll.head = newNode
        ll.size += 1
        return True
    # Find the nodes before and at the target position
    # Create a new node and reconnect the links
    pre = findNode2(ll, index - 1)
    if pre is not None:
        newNode.next = pre.next
        pre.next = newNode
        ll.size += 1
        return True
    return False

def removeNode2(ll, index):
    # Write your code here #

if __name__ == "__main__":  
    ll = LinkedList()
    print("Enter one number per line (press Enter after each number).")
    print("Enter any non-digit character to finish input:")
    try:
        while True:
            item = int(input())
            if not insertNode2(ll, ll.size, item):
                break
    except ValueError:
        pass
    printList2(ll)
    
    while True:
        try:
            index = int(input("Enter the index of the node to be removed: "))
            if not removeNode2(ll, index):
                print("The node cannot be removed.")
                break
            print("After the removal operation:")
            printList2(ll)
        except ValueError:
            break
    printList2(ll)