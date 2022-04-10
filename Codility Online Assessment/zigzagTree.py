class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# Function to print zigzag traversal of binary tree


def zigzagTraversal(root):
    # Base Case
    if root is None:
        return

    # Create two stacks to store current and next level
    currentLevel = []
    nextLevel = []

    # if ltr is true push nodes from left to right else, right to left
    ltr = True

    currentLevel.append(root)

    while len(currentLevel) > 0:
        temp = currentLevel.pop()
        print(temp.data, " ", end="")

        if ltr:
            if temp.left:
                nextLevel.append(temp.left)
            if temp.right:
                nextLevel.append(temp.right)
        else:
            if temp.right:
                nextLevel.append(temp.right)
            if temp.left:
                nextLevel.append(temp.left)

        if len(currentLevel) == 0:
            # reverse ltr to push node in the opposite order
            ltr = not ltr
            # Swapping of stacks
            currentLevel, nextLevel = nextLevel, currentLevel


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
zigzagTraversal(root)
