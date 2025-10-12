def is_balanced(tree):
    def height_if_balanced(node):
        if node is None:
            return 0

        left_height = height_if_balanced(node.left)
        right_height = height_if_balanced(node.right)
        if (
            left_height == -1
            or right_height == -1
            or abs(left_height - right_height) > 1
        ):
            return -1

        return max(left_height, right_height) + 1

    return height_if_balanced(tree.root) != -1
