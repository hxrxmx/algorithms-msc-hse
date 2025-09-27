from homework_2.stack_vs_queue.stack_n_queue import Stack


def test_stack_basic():
    s = Stack()
    assert s.is_empty()

    s.push(1)
    s.push(2)
    s.push(3)

    assert not s.is_empty()
    assert s.peek() == 3

    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()

    assert s.pop() is None

    assert s.peek() is None
