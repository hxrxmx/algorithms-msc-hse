class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    #  можно без всяких классов на одном динамич списке
    #  реализовать, но так понагляднее
    def __init__(self):
        self.root = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.root is None:
            self.root = new_node
            return

        node = self.root
        while True:
            if new_value < node.value:
                if node.left is None:
                    node.left = new_node
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = new_node
                    return
                node = node.right

    #  не лучшая идея делать все рекурсией, но так писать быстрее
    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return []
        return [node.value] + self._preorder(node.left) + self._preorder(node.right)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.value]

    def reverse_preorder(self):
        return self._reverse_preorder(self.root)

    def _reverse_preorder(self, node):
        if node is None:
            return []
        return (
            [node.value]
            + self._reverse_preorder(node.right)
            + self._reverse_preorder(node.left)
        )

    def reverse_inorder(self):
        return self._reverse_inorder(self.root)

    def _reverse_inorder(self, node):
        if node is None:
            return []
        return (
            self._reverse_inorder(node.right)
            + [node.value]
            + self._reverse_inorder(node.left)
        )

    def reverse_postorder(self):
        return self._reverse_postorder(self.root)

    def _reverse_postorder(self, node):
        if node is None:
            return []
        return (
            self._reverse_postorder(node.right)
            + self._reverse_postorder(node.left)
            + [node.value]
        )
