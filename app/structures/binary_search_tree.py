from .tree_node import TreeNode

class BinarySearchTree:
    """Árbol binario de búsqueda genérico."""
    def __init__(self):
        self.root = None
        self.size = 0

    # -------- inserción --------
    def insert(self, data, key_func):
        if self.root is None:
            self.root = TreeNode(data)
            self.size += 1
            return True

        current = self.root
        while True:
            if key_func(data) < key_func(current.data):
                if current.left is None:
                    current.left = TreeNode(data)
                    self.size += 1
                    return True
                current = current.left
            elif key_func(data) > key_func(current.data):
                if current.right is None:
                    current.right = TreeNode(data)
                    self.size += 1
                    return True
                current = current.right
            else:
                return False       # duplicado

    # -------- búsqueda --------
    def search(self, key, key_func):
        current = self.root
        while current:
            current_key = key_func(current.data)
            if key == current_key:
                return current.data
            current = current.left if key < current_key else current.right
        return None

    # -------- recorrido in-order --------
    def inorder_traversal(self):
        result = []
        def _in(node):
            if node:
                _in(node.left)
                result.append(node.data)
                _in(node.right)
        _in(self.root)
        return result
