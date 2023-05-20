class Tree():
    def __init__(self, data):
        self.left = None 
        self.right = None
        self.data = data


tree = Tree(2)
tree.left = 3
tree.right =4
print(tree.left)