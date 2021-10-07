class Node:
    def __init__(self, val, children=[None]):
        self.val = val
        self.children = children


def preorder(root):
    if root:
        print(root.val, end=' ')
        for child in root.children:
            preorder(child)

def postorder(root):
    if root:
        for child in root.children:
            postorder(child)
        print(root.val, end=' ')

if __name__ == '__main__':
    root = Node(1, [Node(2), Node(3, [Node(4), Node(5)]), Node(6, [Node(7)])])
    print('Preorder:', end=' '); preorder(root); print()
    print('Postorder:', end=' '); postorder(root); print()
