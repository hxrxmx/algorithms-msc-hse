from homework_2.stack_vs_queue.stack_n_queue import Queue


def test_queue_basic():
    q = Queue()
    assert q.is_empty()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert not q.is_empty()
    assert q.peek() == 1

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()

    assert q.dequeue() is None

    assert q.peek() is None
