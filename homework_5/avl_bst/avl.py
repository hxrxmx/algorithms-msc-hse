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
            if new_value > node.value:
                side = "r"
                path.append((node, side))
                if node.right is None:
                    node.right = new_node
                    self._rebalance(path)
                    return
                node = node.right
            else:
                side = "l"
                path.append((node, side))
                if node.left is None:
                    node.left = new_node
                    self._rebalance(path)
                    return
                node = node.left

    def _right_rotate(self, node):
        top_node = node.left
        node.left = top_node.right
        top_node.right = node
        self._update_height(top_node.right)
        self._update_height(top_node)
        return top_node

    def _left_rotate(self, node):
        top_node = node.right
        node.right = top_node.left
        top_node.left = node
        self._update_height(top_node.left)
        self._update_height(top_node)
        return top_node

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.right), self._height(node.left))

    def _rebalance(self, path):
        child = None
        for node, side in path[::-1]:
            if child:
                if side == "r":
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

    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            if not node.left or not node.right:
                node = node.left or node.right
            else:
                successor = self._min_value_node(node.right)
                node.value = successor.value
                node.right = self._remove(node.right, successor.value)

        if not node:
            return None

        self._update_height(node)

        balance = self._height_diff_factor(node)

        if balance > 1:
            if self._height_diff_factor(node.left) < 0:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1:
            if self._height_diff_factor(node.right) > 0:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node
