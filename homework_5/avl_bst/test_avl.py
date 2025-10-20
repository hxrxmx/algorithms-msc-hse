import numpy as np
import pytest

from homework_4.balance.balance import is_balanced
from homework_5.avl_bst.avl import AVL

SEED = 42
BINOM_P = 0.7
SIZE = 10_000


@pytest.fixture
def avl_tree():
    tree = AVL()

    rng = np.random.default_rng(seed=SEED)
    for val in rng.integers(-10_000, 10_000, size=SIZE):
        if rng.binomial(1, BINOM_P):
            tree.append(val)
        else:
            tree.remove(val)

    return tree


def test_values_correctness(avl_tree):
    values_list = []

    rng = np.random.default_rng(seed=SEED)
    for val in rng.integers(-10_000, 10_000, size=SIZE):
        if rng.binomial(1, BINOM_P):
            values_list.append(val)
        else:
            try:
                values_list.remove(val)
            except ValueError:
                pass
    assert sorted(values_list) == sorted(avl_tree.inorder())


def test_balance(avl_tree):
    assert is_balanced(avl_tree)


def test_in_order(avl_tree):
    vals = avl_tree.inorder()
    assert vals == sorted(vals)
