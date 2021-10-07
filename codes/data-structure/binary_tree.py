class Node:
    def __init__(self, val, lch=None, rch=None):
        self.val = val
        self.lch = lch
        self.rch = rch


def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.lch)
        preorder(root.rch)

def postorder(root):
    if root:
        postorder(root.lch)
        postorder(root.rch)
        print(root.val, end=' ')

if __name__ == '__main__':
    root = Node(1, Node(2), Node(3, Node(4), Node(5, Node(6, Node(7)))))
    print('Preorder:', end=' '); preorder(root); print()
    print('Postorder:', end=' '); postorder(root); print()
