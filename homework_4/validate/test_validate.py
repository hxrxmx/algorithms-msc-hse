import pytest

from homework_4.bst_w_traversals.bst import BST, Node
from homework_4.validate.validate import validate


@pytest.fixture
def bst_balanced():
    bst = BST()
    bst.append(5)
    bst.append(3)
    bst.append(7)
    bst.append(2)
    bst.append(4)
    bst.append(6)

    return bst


@pytest.fixture
def bst_imbalanced():
    bst = BST()
    bst.append(5)
    bst.append(3)
    bst.append(7)
    bst.append(2)
    bst.append(4)
    bst.append(8)
    bst.append(9)
    bst.append(10)
    bst.append(11)

    return bst


def test_validate_correct(bst_balanced):
    assert validate(bst_balanced.root)


def test_validate_empty():
    assert validate(BST().root)


def test_validate_imbalanced(bst_imbalanced):
    assert validate(bst_imbalanced.root)


def test_incorrect():
    bst = BST()
    bst.root = Node(5)
    bst.append(3)
    bst.append(8)
    bst.root.right.right = Node(7)
    assert not validate(bst.root)

    bst = BST()
    bst.root = Node(5)
    bst.append(3)
    bst.append(8)
    bst.root.left.right = Node(7)
    assert not validate(bst.root)
