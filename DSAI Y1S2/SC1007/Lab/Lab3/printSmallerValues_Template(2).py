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

def printSmallerValues(node, m):
    # Write your code here #
    if node is None:
        return
    if node.item < m:
        print(node.item,end =" ")

    printSmallerValues(node.left, m)
    printSmallerValues(node.right,m)


if __name__ == "__main__":
    root = BTNode(4)
    root.left = BTNode(5)
    root.right = BTNode(2)
    root.left.right = BTNode(6)
    root.right.left = BTNode(3)
    root.right.right = BTNode(1)

    print("Tree Structure:")
    printTree(root)

    print("\nTree (In-Order):")
    print_tree_in_order(root)
    print()

    # Using a hardcoded value instead of input()
    m = 4  # You can change this value for testing
    print(f"\nThe values smaller than {m} are:", end=" ")
    printSmallerValues(root, m)
    print()