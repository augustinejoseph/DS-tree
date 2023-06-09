class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    

def inOrder(root):
    if root is None:
        return []
    result = []
    result.extend(inOrder(root.left))
    result.append(root.data)
    result.extend(inOrder(root.right))
    return result


root = Node(3)
root.left = Node(6)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(2)
root.right.left= Node(9)
root.right.right= Node(8)
res = inOrder(root)
print(res)

