import pytest

from homework_4.balance.balance import is_balanced
from homework_4.bst_w_traversals.bst import BST


@pytest.fixture
def balanced_tree():
    bst = BST()
    bst.append(10)
    bst.append(5)
    bst.append(15)
    bst.append(3)
    bst.append(7)
    bst.append(12)
    bst.append(17)
    #      10
    #    |     \
    #   5      15
    #  | \    |  \
    #  3  7  12  17
    return bst


def test_balance_empty():
    assert is_balanced(BST())


def test_balance_single_tree():
    bst = BST()
    bst.append(2)
    assert is_balanced(bst)


def test_balance_perfect_balanced(balanced_tree):
    assert is_balanced(balanced_tree)


def test_balance_left_inbalanced(balanced_tree):
    tree = balanced_tree
    tree.append(2)
    tree.append(1)
    assert not is_balanced(tree)


def test_balance_right_inbalanced(balanced_tree):
    tree = balanced_tree
    tree.append(20)
    tree.append(21)
    assert not is_balanced(tree)


def test_balance_imperfect_balanced(balanced_tree):
    balanced_tree.append(1)
    assert is_balanced(balanced_tree)


def test_balanced_complex_unbalanced(balanced_tree):
    tree = balanced_tree
    tree.append(1)
    tree.append(2)
    tree.append(4)
    tree.append(6)
    tree.append(8)
    tree.append(11)
    tree.append(13)
    tree.append(16)
    tree.append(18)
    tree.append(1.5)
    tree.append(0.5)
    #            10
    #         |      \
    #         5       15
    #       | \     |   \
    #      3   7   12   17
    #     | \ | \  | \  |  \
    #    1  4 6 8 11 13 16 18
    #   | \
    # 0.5  2
    #      |
    #    1.5
    assert not is_balanced(tree)
