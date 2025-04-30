class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def insertBSTNode(node, value):
    # Write your code here #
    if node is None:
        return BTNode(value)

    if value<node.item:
        node.left = insertBSTNode(node.left, value)
    if value>node.item:
         node.right = insertBSTNode(node.right,value)
    return node

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

if __name__ == "__main__":
    root = None
    print("Binary Search Tree Insertion Program")
    print("===================================")
    
    while True:
        value = input("\nEnter a value to insert (-1 to quit): ")
        if not value:
            continue  # Ignore empty inputs
        
        try:
            i = int(value)
            if i == -1:
                break
            
            root = insertBSTNode(root, i)
            print("\nCurrent BST structure:")
            printTree(root)
        
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nFinal BST structure:")
    printTree(root)