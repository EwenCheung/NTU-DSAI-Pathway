class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item  # Store the item (integer)
        self.left = left  # Reference to the left child node
        self.right = right  # Reference to the right child node

def insertBSTNode(root, value):
    """ Iterative approach to insert a node into a BST. """
    if root is None:
        return BTNode(value)  # If tree is empty, create root

    parent = None
    current = root

    while current:
        parent = current
        if value < current.item:
            current = current.left
        elif value > current.item:
            current = current.right
        else:
            return root 

    if value < parent.item:
        parent.left = BTNode(value)
    else:
        parent.right = BTNode(value)

    return root

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def printBSTInOrder(node):
    """ Print BST items in sorted order using in-order traversal. """
    # Write your code here #
    if node is not None:
        return

    def inorder():
        printBSTInOrder(node.left)
        print(node.item,end=" ")
        printBSTInOrder(node.right)

    inorder()

if __name__ == "__main__":
    root = None
    print("Binary Search Tree In-Order Traversal Program")
    print("===========================================")
    
    print("\nFirst, let's build the BST:")
    
    while True:
        try:
            value = input("\nEnter a value to insert (-1 to quit): ")
            if not value:
                continue  # Ignore empty inputs
                
            i = int(value)
            if i == -1:
                break
                
            root = insertBSTNode(root, i)
            
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nBST structure:")
    printTree(root)
    print("\nIn-order traversal (sorted order):", end=" ")
    printBSTInOrder(root)
    print()
