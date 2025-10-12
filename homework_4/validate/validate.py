from numpy import inf

from homework_4.bst_w_traversals.bst import Node


def validate(node: Node, low=-inf, high=inf) -> bool:
    if node is None:
        return True
    if not (low < node.value < high):
        return False
    return validate(node.left, low=low, high=node.value) and validate(
        node.right, low=node.value, high=high
    )
