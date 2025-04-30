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
            return root  # Value already exists, return root unchanged

    if value < parent.item:
        parent.left = BTNode(value)
    else:
        parent.right = BTNode(value)

    return root

def printBSTInOrder(node):
    """ Print BST items in sorted order using in-order traversal. """
    if node:
        printBSTInOrder(node.left)
        print(node.item, end=" ")
        printBSTInOrder(node.right)

def printTree(node, level=0, prefix="Root: "):
    """ Pretty prints the tree structure for better visualization """
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def isBST(node, min_val=float('-inf'), max_val=float('inf')):
    """ Checks if a tree is a valid BST using min/max constraints. """
    # Write your code here #
    if node is None:
        return True

    if node.left and node.left.item >= node.item:
        return False

    if node.right and node.right.item <= node.item:
        return False

    return isBST(node.left) and isBST(node.right)

    # if node is None:
    #     return True  # Base case: An empty tree is a valid BST
    #
    # if not (min_val < node.item < max_val):
    #     return False  # If node value is out of range, it's not a BST
    #
    # return isBST(node.left, min_val, node.item) and isBST(node.right, node.item, max_val)

def createInvalidBST():
    """ Creates a binary tree that is NOT a valid BST for testing. """
    root = BTNode(5)
    root.left = BTNode(3)
    root.right = BTNode(7)
    root.left.right = BTNode(6)  # Invalid: 6 is greater than parent 3
    return root

if __name__ == "__main__":
    root = None
    print("Binary Search Tree In-Order Traversal & Validation Program")
    print("===========================================================")
    
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
            
            # Print both in-order traversal and tree structure after each insertion
            print("\nCurrent in-order traversal:", end=" ")
            printBSTInOrder(root)
            print("\n\nCurrent BST structure:")
            printTree(root)
            print()  # New line for better readability
            
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nFinal in-order traversal (sorted order):", end=" ")
    printBSTInOrder(root)
    print("\n\nFinal BST structure:")
    printTree(root)
    print()

    # Validate if the final tree is a BST
    print("\nChecking if the tree is a valid BST...")
    if isBST(root):
        print("The tree is a valid BST!")
    else:
        print("The tree is NOT a valid BST!")

    # Test with an invalid BST
    print("\nTesting with an invalid binary tree...")
    invalid_root = createInvalidBST()
    print("\nInvalid BST structure:")
    printTree(invalid_root)

    print("\nChecking if the invalid tree is a BST...")
    if isBST(invalid_root):
        print("The tree is a valid BST!")
    else:
        print("The tree is NOT a valid BST!")
