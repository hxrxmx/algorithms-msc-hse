from homework_4.bst_w_traversals.bst import BST, Node


class AVLNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.height = 1


class AVL(BST):
    def __init__(self):
        super().__init__()

    def append(self, new_value):
        new_node = AVLNode(new_value)
        if self.root is None:
            self.root = new_node
            return

        node = self.root
        path = []
        while True:
            path.append(node)
            if new_value > node.value:
                if node.right is None:
                    node.right = new_node
                    self._rebalance(path)
                    return
                node = node.right
            else:
                if node.left is None:
                    node.left = new_node
                    self._rebalance(path)
                    return
                node = node.left

    def _right_rotate(self, node):
        top_node = node.left
        right_child = node
        right_child.left = node.left.right
        top_node.right = right_child
        self._update_height(top_node.right)
        self._update_height(top_node)
        return top_node

    def _left_rotate(self, node):
        top_node = node.right
        left_child = node
        left_child.right = node.right.left
        top_node.left = left_child
        self._update_height(top_node.left)
        self._update_height(top_node)
        return top_node

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.right), self._height(node.left))

    def _rebalance(self, path):
        child = None
        for node in path[::-1]:
            if child:
                if child.value > node.value:
                    node.right = child
                else:
                    node.left = child

            self._update_height(node)
            hdf = self._height_diff_factor(node)

            if hdf < -1:
                if self._height_diff_factor(node.right) > 0:
                    node.right = self._right_rotate(node.right)
                child = self._left_rotate(node)
            elif hdf > 1:
                if self._height_diff_factor(node.left) < 0:
                    node.left = self._left_rotate(node.left)
                child = self._right_rotate(node)
            else:
                child = node
        self.root = child

    def _height(self, node):
        return node.height if node else 0

    def _height_diff_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0
