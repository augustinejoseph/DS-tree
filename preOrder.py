class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    

def preOrder(root):
    if root is None:
        return []
    result = []
    result.append(root.data)
    result.extend(preOrder(root.left))
    result.extend(preOrder(root.right))
    return result


root = Node(3)
root.left = Node(6)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(2)
root.right.left= Node(9)
root.right.right= Node(8)
res = preOrder(root)
print(res)