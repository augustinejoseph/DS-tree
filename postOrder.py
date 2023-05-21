class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    

def postOrder(root):
    if root is None:
        return []
    result = []
    result.extend(postOrder(root.left))
    result.extend(postOrder(root.right))
    result.append(root.data)
    return result


root = Node(3)
root.left = Node(6)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(2)
root.right.left= Node(9)
root.right.right= Node(8)
res = postOrder(root)
print(res)