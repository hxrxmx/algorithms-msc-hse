import pytest

from homework_4.bst_w_traversals.bst import BST


@pytest.fixture
def bst():
    tree = BST()
    for val in [5, 3, 7, 2, 4, 6, 8]:
        tree.append(val)
    #       5
    #      |  \
    #     3    7
    #    | \  | \
    #   2  4  6  8
    return tree


def test_preorder(bst):
    assert bst.preorder() == [5, 3, 2, 4, 7, 6, 8]


def test_inorder(bst):
    assert bst.inorder() == [2, 3, 4, 5, 6, 7, 8]


def test_postorder(bst):
    assert bst.postorder() == [2, 4, 3, 6, 8, 7, 5]


def test_reverse_preorder(bst):
    assert bst.reverse_preorder() == [5, 7, 8, 6, 3, 4, 2]


def test_reverse_inorder(bst):
    assert bst.reverse_inorder() == [8, 7, 6, 5, 4, 3, 2]


def test_reverse_postorder(bst):
    assert bst.reverse_postorder() == [8, 6, 7, 4, 2, 3, 5]
