class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def print_tree_in_order(node):
    if node is None:
        return
    print_tree_in_order(node.left)
    print(node.item, end=", ")
    print_tree_in_order(node.right)

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def hasGreatGrandchild(node):
    # Write your code here #
    if node is None:
        return 0
    left_height = hasGreatGrandchild(node.left)
    right_height = hasGreatGrandchild(node.right)
    max_height = max(left_height, right_height)

    if max_height >= 3:
        print(node.item, end=" ")
     
    return max_height +1

if __name__ == "__main__":
    # Create a tree with nodes having great-grandchildren
    root = BTNode(1)
    
    # Left subtree
    root.left = BTNode(2)
    root.left.left = BTNode(4)
    root.left.left.left = BTNode(8)
    root.left.left.left.left = BTNode(16)
    
    # Right subtree  
    root.right = BTNode(3)
    root.right.right = BTNode(7)
    root.right.right.right = BTNode(15)
    root.right.right.right.right = BTNode(31)

    print("Visual representation of the tree:")
    printTree(root)
    
    print("\nTree (In-Order):")
    print_tree_in_order(root)
    
    print("\nNodes with great-grandchildren:", end=" ")
    hasGreatGrandchild(root)
    print()